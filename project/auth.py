from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User, Geonames
import sqlite3

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    if request.form.get('remember'):
        remember = True 
    else: 
        remember = False
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    login_user(user, remember=remember)
    return redirect(url_for('main.management'))

# @auth.route('/management', methods=['POST'])
# def search():
#     keyword = request.form.get('geoid')
#     geoid = Geonames.query.filter_by(geoid=keyword).first()
#     # if geoid:
#     print(f"id is : {geoid}")
#     return redirect(url_for('res.html',items=geoid))



