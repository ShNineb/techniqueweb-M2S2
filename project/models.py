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
	geoid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(1000))
	langtitude = db.Column(db.Float)



    	