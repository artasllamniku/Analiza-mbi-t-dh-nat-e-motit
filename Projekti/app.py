from flask import Flask, render_template, request
from moti import kerko_qytete, merr_te_dhena_per_web_me_id

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    moti = None
    gabim = None
    opsionet = []

    if request.method == 'POST':
        qyteti = request.form.get('city')
        rezultatet = kerko_qytete(qyteti)

        if len(rezultatet) == 0:
            gabim = "Qyteti nuk u gjet."
        elif len(rezultatet) == 1:
            city_id = rezultatet[0]['id']
            moti = merr_te_dhena_per_web_me_id(city_id)
        else:
             opsionet = rezultatet
             
    return render_template('index.html', moti=moti, gabim=gabim, opsionet=opsionet)

if __name__ == "__main__":
    app.run(debug=True)
