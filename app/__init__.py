from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions outside the create_app function
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_pyfile('config.py')

    # Initialize extensions
    db.init_app(app)

    with app.app_context():
        # Import parts of your application here
        from .models import Book, Student  # Import your models

        # Create the database tables
        db.create_all()

    return app
