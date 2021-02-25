from . import db
from flask_login import UserMixin
from datetime import datetime

# le tableux user 
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
    	return '<Name %r>' % self.id

# le tableux geonames 
class Geonames(db.Model):
    geonameid=db.Column(db.Integer, primary_key=True, unique=True)
    name=db.Column(db.String(200), nullable=False)
    asciiname=db.Column(db.String(200))
    alternatenames=db.Column(db.String(10000))
    latitude=db.Column(db.Float)
    longitude=db.Column(db.Float)
    feature_class=db.Column(db.String(1))
    feature_code=db.Column(db.String(10))
    country_code=db.Column(db.String(2))
    cc2=db.Column(db.String(200))
    admin1_code=db.Column(db.String(20))
    admin2_code=db.Column(db.String(80))
    admin3_code=db.Column(db.String(20))
    admin4_code=db.Column(db.String(20))
    population=db.Column(db.Integer)
    elevation=db.Column(db.Integer)
    dem=db.Column(db.Integer)
    timezone=db.Column(db.String(40))
    modification=db.Column(db.Date)
    modified_by=db.Column(db.String)



    	