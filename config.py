''' Module for the app's configuration'''
import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///quiz.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGIN_VIEW = 'login'