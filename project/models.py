from . import db
from flask_login import UserMixin


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
    name=db.Column(db.String)
    asciiname=db.Column(db.String)
    alternatenames=db.Column(db.String)
    latitude=db.Column(db.Float)
    longitude=db.Column(db.Float)
    feature_class=db.Column(db.String)
    feature_code=db.Column(db.String)
    country_code=db.Column(db.String)
    cc2=db.Column(db.Char(2))
    admin1_code=db.Column(db.Integer)
    admin2_code=db.Column(db.Integer)
    admin3_code=db.Column(db.Integer)
    admin4_code=db.Column(db.Integer)
    population=db.Column(db.Integer)
    elevation=db.Column(db.Integer)
    dem=db.Column(db.Integer)
    timezone=db.Column(db.String)
    modification=db.Column(db.String)
    modified_by=db.Column(db.String)



    	