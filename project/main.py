from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/management')
@login_required
def management():
    return render_template('management.html', name=current_user.name)





