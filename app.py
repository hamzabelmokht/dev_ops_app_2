from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hamza@mysql/DevOpsProject2'
db = SQLAlchemy(app)

class AppList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        data = request.form['data']
        new_list = AppList(list=data)
        db.session.add(new_list)
        db.session.commit()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)