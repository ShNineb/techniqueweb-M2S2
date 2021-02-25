from flask import Blueprint, render_template, url_for, request, redirect, flash
from . import db
from flask_login import login_required, current_user
from .models import User, Geonames


from datetime import datetime
from sqlalchemy import desc
import datetime

index = Blueprint('index', __name__)

@index.route('/')
def index_page():
    if current_user.is_authenticated:
        return render_template('index.html',name=current_user.name)
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
		
		geos = Geonames.query.order_by(desc(Geonames.modification)).limit(5).all()
        #geos = Geonames.query.order_by(desc(Geonames.modification)).all()
        #return render_template('add.html', geos=geos)
		return render_template('management.html', name=current_user.name, geos=geos)


#@index.route('/add')
#@login_required
#def add():
#   return render_template('add.html', name=current_user.name)

@index.route('/add', methods=['POST', 'GET'])
@login_required
def add():
    if request.method == 'POST':
        add_geonameid = request.form['geonameid']
        add_name = request.form['name']
        add_asciiname = request.form['asciiname']
        add_alternatenames = request.form['alternatenames']
        add_latitude = request.form['latitude']
        add_longitude = request.form['longitude']
        add_feature_class = request.form['feature_class']
        add_feature_code = request.form['feature_code']
        add_country_code = request.form['country_code']
        add_cc2 = request.form['cc2']
        add_admin1_code = request.form['admin1_code']
        add_admin2_code = request.form['admin2_code']
        add_admin3_code = request.form['admin3_code']
        add_admin4_code = request.form['admin4_code']
        add_population = request.form['population']
        add_elevation = request.form['elevation']
        add_dem = request.form['dem']
        add_timezone = request.form['timezone']
        #add_modification = request.form['modification_date']
        add_modification = request.form['modification_date']
        # 2021-02-27
        date_time = datetime.datetime.strptime(add_modification,'%Y-%m-%d')
        add_modified_by = current_user.username

        #new_item = Geonames(geonameid=add_geonameid, name=add_name, asciiname=add_asciiname, alternatenames=add_alternatenames, latitude=add_latitude, longitude=add_longitude, feature_class=add_feature_class, feature_code=add_feature_code)
 
        new_item = Geonames(geonameid=add_geonameid, name=add_name, asciiname=add_asciiname, alternatenames=add_alternatenames, \
                    latitude=add_latitude, longitude=add_longitude, feature_class=add_feature_class, feature_code=add_feature_code, \
                    country_code=add_country_code, cc2=add_cc2, admin1_code=add_admin1_code, admin2_code=add_admin2_code, \
                    admin3_code=add_admin3_code, admin4_code=add_admin4_code, population=add_population, elevation=add_elevation, \
                    dem=add_dem, timezone=add_timezone, modification=date_time, modified_by=add_modified_by)
        try:
            db.session.add(new_item)
            db.session.commit()
            #flash("New Item Added Successfully")
            return redirect('/management')

        except:
            return 'There was a problem adding that item'
    else:
        geos = Geonames.query.order_by(desc(Geonames.geonameid)).limit(10).all()
        #geos = Geonames.query.order_by(desc(Geonames.modification)).all()
        return render_template('add.html', geos=geos, name=current_user.name)

@index.route('/delete/<int:geonameid>')
@login_required
def delete(geonameid):
    item_to_delete = Geonames.query.get_or_404(geonameid)

    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        #flash("New Item Deleted Successfully")
        return redirect('/management')
    
    except:
        return 'There was a problem deleting that item'

@index.route('/update/<int:geonameid>', methods=['POST', 'GET'])
def update(geonameid):
    update_geo = Geonames.query.get_or_404(geonameid)
    if request.method == 'POST':
        update_geo.geonameid = request.form['geonameid']
        update_geo.name = request.form['name']
        update_geo.asciiname = request.form['asciiname']
        update_geo.alternatenames = request.form['alternatenames']
        update_geo.latitude = request.form['latitude']
        update_geo.longitude = request.form['longitude']
        update_geo.feature_class = request.form['feature_class']
        update_geo.feature_code = request.form['feature_code']
        update_geo.country_code = request.form['country_code']
        update_geo.cc2 = request.form['cc2']
        update_geo.admin1_code = request.form['admin1_code']
        update_geo.admin2_code = request.form['admin2_code']
        update_geo.admin3_code = request.form['admin3_code']
        update_geo.admin4_code = request.form['admin4_code']
        update_geo.population = request.form['population']
        update_geo.elevation = request.form['elevation']
        update_geo.dem = request.form['dem']
        update_geo.timezone = request.form['timezone']
        #update_geo.modification = request.form['modification_date']
        date_time = request.form['modification_date']
        date_time = datetime.datetime.strptime(date_time,'%Y-%m-%d')
        update_geo.modification = date_time
        update_geo.modified_by = current_user.username

        try:
            db.session.commit()
            #flash("New Item Updated Successfully")
            return redirect('/management')
    
        except:
            return 'There was a problem updating that item'

    else:
        return render_template('update.html', geo=update_geo)



#this route is for inserting data to mysql database via html forms
@index.route('/insert', methods = ['POST'])
@login_required
def insert():

    if request.method == 'POST':
        add_geonameid = request.form['geonameid']
        add_name = request.form['name']
        add_asciiname = request.form['asciiname']
        add_alternatenames = request.form['alternatenames']
        add_latitude = request.form['latitude']
        add_longitude = request.form['longitude']
        add_feature_class = request.form['feature_class']
        add_feature_code = request.form['feature_code']
        add_country_code = request.form['country_code']
        add_cc2 = request.form['cc2']
        add_admin1_code = request.form['admin1_code']
        add_admin2_code = request.form['admin2_code']
        add_admin3_code = request.form['admin3_code']
        add_admin4_code = request.form['admin4_code']
        add_population = request.form['population']
        add_elevation = request.form['elevation']
        add_dem = request.form['dem']
        add_timezone = request.form['timezone']
        #add_modification = request.form['modification_date']
        add_modified_by = request.form['modified_by']

        #new_item = Geonames(geonameid=add_geonameid, name=add_name, asciiname=add_asciiname, alternatenames=add_alternatenames, latitude=add_latitude, longitude=add_longitude, feature_class=add_feature_class, feature_code=add_feature_code)
 
        new_item = Geonames(geonameid=add_geonameid, name=add_name, asciiname=add_asciiname, alternatenames=add_alternatenames, \
                    latitude=add_latitude, longitude=add_longitude, feature_class=add_feature_class, feature_code=add_feature_code, \
                    country_code=add_country_code, cc2=add_cc2, admin1_code=add_admin1_code, admin2_code=add_admin2_code, \
                    admin3_code=add_admin3_code, admin4_code=add_admin4_code, population=add_population, elevation=add_elevation, \
                    dem=add_dem, timezone=add_timezone, modification=add_modification, modified_by=add_modified_by)
        try:
            db.session.add(new_item)
            db.session.commit()
            #flash("New Item Added Successfully")
            return redirect('/management') #url_for('Index')

        except:
            return 'There was a problem adding that item'
    
