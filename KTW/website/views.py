from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#view for home page
@views.route('/')
@views.route('/home')
def home():
    return  render_template('homepage.html')

@views.route('/parents')
def parents_page():
    return render_template('parents.html')

@views.route('/sign_up')
def sign_up():
    return render_template('signup.html')

@views.route('/about_us')
def about_us():
    return render_template('About_us.html')