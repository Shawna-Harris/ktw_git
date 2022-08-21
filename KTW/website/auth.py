from flask import Blueprint, render_template, request,  redirect, url_for, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('myEmail')
        password = request.form.get('password')

        user1= User.query.filter_by(email=email).first()
        if user1:
            if check_password_hash(user1.password, password):
                flash('Logged in successfully', category = 'success')
                login_user(user1, remember=True)
                return render_template('dashboard_parent.html')
            else:
                flash('Incorrect password, try again.', category ='error')
        else:
            flash('Email does not exist. ', category = 'error')

    return render_template('login.html', user1=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('myEmail')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        
        user= User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category ='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email = email, first_name = first_name, last_name = last_name,  password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Congratulations! The account is created.', category='success')
            return redirect(url_for('auth.login'))
    return render_template('signup.html', user=current_user)
