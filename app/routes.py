from flask import render_template, redirect, url_for, request, flash
from app import db
from app.models import User, Question, Option
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/quiz')
@login_required
def quiz():
    questions = Question.query.all()
    return render_template('quiz.html', questions=questions)

@main.route('/submit_quiz', methods=['POST'])
@login_required
def submit_quiz():
    ''' Logic to evaluate the quiz goes here
    Redirect to results page after submitting '''
    return redirect(url_for('main.results'))

@main.route('/results')
@login_required
def results():
    ''' Logic to show results'''
    return render_template('results.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login failed. Check your username and password.')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
