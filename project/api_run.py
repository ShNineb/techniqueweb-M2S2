from flask import Flask
from flask_login import LoginManager
import resources


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources/db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SERVER_NAME'] = 'digidata.api.localhost:80'
app.config['SERVER_NAME'] = 'localhost:5000'


resources.db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    # return userid
    return resources.User.query.get(int(user_id))


# blueprint for auth routes in our app
from resources.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from resources.index import index as index_blueprint
app.register_blueprint(index_blueprint)


if __name__ == '__main__':
	app.run(debug=True)
