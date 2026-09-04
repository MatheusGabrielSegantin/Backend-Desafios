from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_imc', methods=['POST'])
def calcular_imc():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])

    imc = round(peso / (altura ** 2), 2)

    if imc < 18.5:
        diagnostico = "Abaixo do peso"

    elif imc >= 18.5 and imc <= 25:
        diagnostico = "Peso normal"

    elif imc >= 25 and imc <=30:
        diagnostico = "Sobrepeso"

    else:
        diagnostico = "Obesidade"

    return render_template('index.html', imc=imc, diagnostico=diagnostico)



if __name__ == '__main__':
    app.run(debug=True)