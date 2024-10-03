# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Anumula%40123%24@localhost:3306/login_db'  # Ensure correct port for MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False