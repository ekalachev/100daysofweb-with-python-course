from program import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tasks')
def ptasks():
    return render_template('tasks.html')