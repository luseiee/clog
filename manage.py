# Launch the script
import os
from app import create_app
# Flask-script is an extension for Flask that adds a command-line
# parser to your Flask application.
from flask_script import Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
	manager.run()