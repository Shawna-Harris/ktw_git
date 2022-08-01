from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "databas1.db"


def create_app():
    app = Flask(__name__)
    #secure cookies and session data for app
    app.config['SECRET_KEY'] = 'pick pocket put a pickle in a puddle'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    db.init_app(app)

    #alert init of URLs of app
    from .views import views
    from  .auth import auth

    #register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note

    def create_database(app):
        if not path.exists('website/' + DB_NAME):
            db.create_all(app=app)
            print('Created Database!')

    create_database(app)
    return app

    
