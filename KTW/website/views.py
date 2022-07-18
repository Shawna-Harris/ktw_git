from flask import Blueprint

views = Blueprint('views', __name__)

#view for home page
@views.route('/')
def home():
    return "<h1> Test </h1>"