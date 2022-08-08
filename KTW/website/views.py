from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

#view for home page
@views.route('/')
@views.route('/home')
def home():
    return  render_template('homepage.html')

@views.route('/parents')
def parents_page():
    return render_template('parents.html') 
"""
@views.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('myEmail')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        contact_num = request.form.get('contactNumber')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif len(contact_num) < 9:
            flash('The contact number must be 9 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Congratulations! The account is created.', category='success')
    return render_template('signup.html') """

@views.route('/about_us')
def about_us():
    return render_template('About_us.html')

@views.route('/dashboard_parent')
def dash_parent():
    return render_template('dashboard_parent.html')

@views.route('/dashboard_student')
def dash_student():
    return render_template('dashboard_student.html')

@views.route('/dash_layouts')
def dash_layouts():
    return render_template('dashboard_layouts.html')