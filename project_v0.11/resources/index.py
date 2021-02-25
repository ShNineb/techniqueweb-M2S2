from flask import Blueprint, render_template,request
from . import db
from flask_login import login_required, current_user
from .models import User, Geonames

index = Blueprint('index', __name__)

@index.route('/')
def index_page():
	# if current_user.name:
	# 	return render_template('index.html',name=current_user.name)
	return render_template('index.html')

@index.route('/management', methods=['POST','GET'])
@login_required
def management():
	if request.method == 'POST':
		geoid = request.form['geoid']
		id_search = Geonames.query.filter_by(geonameid=geoid).first()
        # if id doesn't exist, we add a new one
		if not id_search:
			print(f"not found {id_search}")
			return render_template('add.html', name=current_user.name )
        #  if id exist in the database, user can modify or delete it
		else:
			print(f"found {id_search}")
			return render_template('modify_delete.html', name=current_user.name, geonameid=id_search.geonameid)
	else:
		return render_template('management.html', name=current_user.name)


@index.route('/add/<int:id>',methods=['GET','POST'])
@login_required
def add():
	
    return render_template('add.html', name=current_user.name)


