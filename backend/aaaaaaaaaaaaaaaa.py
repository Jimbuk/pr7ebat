from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        methodd = request.form['method']
        if methodd == 'plus':
            result = int(num1) + int(num2)
        if methodd == 'minus':
            result = int(num1) - int(num2)
        if methodd == 'multiplication':
            result = int(num1) * int(num2)
        if methodd == 'division':
            result = int(num1) / int(num2)
        return render_template('calculatorr.html', result=result)
    else:
        return render_template('calculatorr.html')

if __name__ == '__main__':
    app.run(debug=True)
