from flask import Flask, render_template,request
import requests


app = Flask(__name__)
valor=0

@app.route('/')
def hello_world():
    return render_template('forms.html')

@app.route('/',methods=['POST'])
def saldo():
    try:
        numero1 = request.form['text']
        pagina = "http://bip-servicio.herokuapp.com/api/v1/solicitudes.json?bip=" + str(numero1)
        response = requests.get(pagina)
        numero = response.json()
        resultado = ("Su saldo es : " + str(numero['saldoTarjeta']) + "  "+" Su numero de tarjeta es: " + str(numero['id']))
        #return render_template('forms2.html',resultado=resultado)
        #return resultado
        return render_template('forms2.html',resultado=resultado)
    except:
        return render_template('forms2.html',resultado='error')



if __name__ == '__main__':
    app.run()
