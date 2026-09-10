from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_idade', methods=['Post'])
def calcular_idade():

    data = int(request.form['data'])
    idade = (2026 - data)

    return render_template('index.html', idade=idade)

if __name__ == '__main__':
    app.run(debug=True)
