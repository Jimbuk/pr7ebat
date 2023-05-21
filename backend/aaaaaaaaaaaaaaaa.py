from flask import Flask, request, jsonify, render_template
import os
import psycopg2

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

# Функция для установления соединения с базой данных
def create_connection():
    connection = psycopg2.connect(
        host="127.0.0.1",
        port='5432',
        user="postgres",
        password="postgresql",
        database="dbcalculate"
    )
    return connection

# Функция для создания таблицы, если она еще не существует
def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    # SQL-запрос для создания таблицы
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS calculations (
            id SERIAL PRIMARY KEY,
            num1 INTEGER,
            num2 INTEGER,
            method VARCHAR(10),
            result FLOAT
        )
    '''

    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

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

        # Запись результата в базу данных
        connection = create_connection()
        cursor = connection.cursor()

        insert_query = '''
            INSERT INTO calculations (num1, num2, method, result)
            VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (num1, num2, methodd, result))

        connection.commit()
        cursor.close()
        connection.close()

        return render_template('calculatorr.html', result=result, image=full_filename)
    else:
        return render_template('calculatorr.html', image=full_filename)

if __name__ == '__main__':
    create_table()  # Создание таблицы перед запуском приложения
    app.run(debug=True)
