# Quiz App

This is a Flask-based quiz application where users can take quizzes, and answers are stored and managed in a SQLite database. The app features user authentication and a responsive design with a red, black, yellow, and white color scheme, along with simple animations.

## Features

- User authentication (login)
- Multiple-choice quizzes
- Scoring system (coming soon)
- Responsive design
- Animation effects for a better user experience
- RESTful structure for adding quiz questions
- SQLite database integration

## Tech Stack

- Python (Flask)
- Flask-SQLAlchemy (Database ORM)
- Flask-Login (User authentication)
- HTML, CSS (Frontend)
- SQLite (Database)

## Installation and Setup

### Step 1: Clone the repository

git clone https://github.com/your-repository/quiz_app.git
cd quiz_app

### Step 2: Set up a virtual environment
python -m venv venv
venv\Scripts\activate

### Step 3: Install dependencies
pip install -r requirements.txt

### Step 4: Set up the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

### Step 5: Run the application
flask run
