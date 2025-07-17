import json
import requests

API_KEY = "8d969eda6ac8cd235e8391b3b8b53e5f"

with open("city.list.json", encoding="utf-8") as f:
    qytetet = json.load(f)

def kerko_qytete(emri):
    emri = emri.strip().lower()

    rezultatet_sakta = [q for q in qytetet if q['name'].lower() == emri]

    if rezultatet_sakta:
       
        return [rezultatet_sakta[0]]

   
    rezultatet_aferta = [q for q in qytetet if emri in q['name'].lower()]


    return rezultatet_aferta[:1]



def merr_moti_me_id(city_id):
    url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("cod") != 200:
        return None
    return {
        "qyteti": data["name"],
      "temperatura": int(data["main"]["temp"]),
        "lageshtia": data["main"]["humidity"],
        "pershkrimi": data["weather"][0]["description"]
    }

def ikonat_e_motit(pershkrimi):
    pershkrimi = pershkrimi.lower()
    if "clear" in pershkrimi or "diell" in pershkrimi:
        return "☀️"
    elif "cloud" in pershkrimi or "re" in pershkrimi:
        return "☁️"
    elif "rain" in pershkrimi or "shi" in pershkrimi:
        return "🌧️"
    elif "snow" in pershkrimi or "borë" in pershkrimi:
        return "❄️"
    elif "storm" in pershkrimi or "stuhi" in pershkrimi:
        return "⛈️"
    else:
        return "🌡️"

def merr_te_dhena_per_web_me_id(city_id):
    moti = merr_moti_me_id(city_id)
    if not moti:
        return None
    moti['ikona'] = ikonat_e_motit(moti['pershkrimi'])
    return moti

def ndreq_emrin(qyteti):
    qyteti = qyteti.replace("Komuna e ", "Komunën e ")

    rregullime = {
        "Gjakove": "Gjakovës",
        "Ferizaj": "Ferizajit",
        "Prishtine": "Prishtinës"
    }

    for orig, ndrequr in rregullime.items():
        if qyteti.endswith(orig):
            qyteti = qyteti.replace(orig, ndrequr)
    return qyteti

def merr_te_dhena_per_web_me_id(city_id):
    moti = merr_moti_me_id(city_id)
    if not moti:
        return None
    moti['qyteti'] = ndreq_emrin(moti['qyteti'])  
    moti['ikona'] = ikonat_e_motit(moti['pershkrimi'])
    return moti
