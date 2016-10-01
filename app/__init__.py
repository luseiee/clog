# The application constructor.
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
	app = Flask(__name__)
	# this is a method available in Flask's app.config object
	app.config.from_object(config[config_name])

	bootstrap.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	mail.init_app(app)

	# register the blueprint to the application
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app