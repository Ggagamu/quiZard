''' The routes where the logic for each page is found'''

from flask import render_template, redirect, url_for, request, flash
from . import app, db
from .models import User, Question, Option
from flask_login import login_user, login_required, logout_user, current_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
@login_required
def quiz():
    questions = Question.query.all()
    return render_template('quiz.html', questions=questions)

@app.route('/submit_quiz', methods=['POST'])
@login_required
def submit_quiz():
    # Logic to evaluate the quiz goes here
    # Redirect to results page after submitting
    return redirect(url_for('results'))

@app.route('/results')
@login_required
def results():
    # Logic to show results
    return render_template('results.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your username and password.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

