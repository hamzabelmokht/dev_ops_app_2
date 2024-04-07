from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hamza'
app.config['MYSQL_DB'] = 'DevOpsProject2'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        data = request.form['data']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO your_table_name (column_name) VALUES (%s)", [data])
        mysql.connection.commit()
        cur.close()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)