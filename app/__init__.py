# The application constructor.
from flask import Flask
from config import config

def create_app(config_name):
	app = Flask(__name__)
	# this is a method available in Flask's app.config object
	app.config.from_object(config[config_name])
	# register the blueprint to the application
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app