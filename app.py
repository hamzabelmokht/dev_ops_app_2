from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)

app.config['MYSQL_HOST'] = '172.17.0.2'
app.config['MYSQL_PORT'] = 3306  
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hamza'
app.config['MYSQL_DB'] = 'DevOpsProject2'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT `list` FROM app_list")
    items = cur.fetchall()  
    cur.close()
    
    return render_template('index.html', items=items)

@app.route('/data', methods=['POST'])
def add_data():
    data = request.form['data']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO app_list (list) VALUES (%s)", [data])
    mysql.connection.commit()
    cur.close()
    
    return index()

@app.route('/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT `list` FROM app_list")
    items = cur.fetchall()  
    cur.close()
    
    print("Received items:", items)  

    return jsonify(items=items)

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=5000)