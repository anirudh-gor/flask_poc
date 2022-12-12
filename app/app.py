from flask import Flask, render_template, url_for, request, redirect
import requests, json, urllib.parse, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# @todo get from environment
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://flask_poc:password@localhost:5432/flask_db"

with app.app_context():
    db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'task addition failed'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'task deletion failed'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'task update failed'

    else:
        return render_template('update.html', task=task)

def get_genere():
    url = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
    response = requests.get(url)
    data = response.json()
    return data

def get_song(genere):
    url = 'https://itunes.apple.com/search?'
    params = {'term': genere, 'limit': 1}
    url = url + urllib.parse.urlencode(params)
    response = requests.get(url)
    return response.json()

@app.route('/recommend', methods=['GET'])
def reommend():
    genere = get_genere()
    song = get_song(genere)
    song['recom_genere']=genere
    response = app.response_class(
        response=json.dumps(song),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)
