# config.py

import os

class Config:
    # SQLite database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///login_db.sqlite3'  # This will create a SQLite file named login_db.sqlite3 in the current directory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
