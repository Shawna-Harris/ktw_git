from flask import Flask

#function to initiate flask
def create_app():
    app = Flask(__name__)
   
    #secure cookies and session data for app
    app.config['SECRET_KEY']= 'pick pocket put a pickle in a puddle'

    #alert init of URLs of app
    from .views import views
    from  .auth import auth

    #register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app

