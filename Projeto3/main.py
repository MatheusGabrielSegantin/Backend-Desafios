from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperatura', methods=['Post'])
def temperatura():
    celsius = float(request.form['celsius'])
    fahrenheit = (celsius * 1.8) + 32

    return render_template('index.html', fahrenheit=fahrenheit)


if __name__ == '__main__':
    app.run(debug=True)

