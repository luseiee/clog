# Launch the script
import os
from app import create_app
# Flask-script is an extension for Flask that adds a command-line
# parser to your Flask application.
from flask_script import Manager, Shell
from app import db
from app.models import User, Role
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
	manager.run()