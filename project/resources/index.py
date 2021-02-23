from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user

index = Blueprint('index', __name__)

@index.route('/')
def index_page():
    return render_template('index.html')

@index.route('/management')
@login_required
def management():
    return render_template('management.html', name=current_user.name)





