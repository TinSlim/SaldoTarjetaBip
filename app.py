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
        resultado = ("saldo: " + str(numero['saldoTarjeta']) + "   numero: " + str(numero['id']))
        return render_template('forms2.html',numerosaldo=resultado)
    except:
        return 'error'



if __name__ == '__main__':
    app.run()
