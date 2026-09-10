from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/idade_pet', methods=['Post'])
def idade_pet():
    pet = int(request.form['pet'])
    humano = 24 + (pet - 2) * 5
    return render_template('index.html', humano=humano)

if __name__ == '__main__':
    app.run(debug=True)