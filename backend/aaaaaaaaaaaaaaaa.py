from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER
@app.route('/', methods=['GET', 'POST'])
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img.png')
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
        return render_template('calculatorr.html', result=result, image=full_filename)
    else:
        return render_template('calculatorr.html',image=full_filename)

if __name__ == '__main__':
    app.run(debug=True)
