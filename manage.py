# Launch the script
import os
from app import create_app
# Flask-script is an extension for Flask that adds a command-line
# parser to your Flask application.
from flask_script import Manager, Shell
from app import db
from app.models import User, Role, Post
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import upgrade
    from app.models import Role, User

    upgrade()

    Role.insert_roles()

    User.add_self_follows()

@manager.command
def newdeploy():
    """Run deployment tasks."""
    from flask_migrate import init, migrate, upgrade
    from app.models import Role, User, Post

    upgrade()

    Role.insert_roles()

    User.add_self_follows()

    User.generate_fake()

    Post.generate_fake()

    import forgery_py
    u = User(email='clogadm@outlook.com',
                     username='Admin',
                     password='1',
                     confirmed=True,
                     name=forgery_py.name.full_name(),
                     location=forgery_py.address.city(),
                     about_me=forgery_py.lorem_ipsum.sentence(),
                     member_since=forgery_py.date.date(True))
    db.session.add(u)

    u2 = User(email='phillu@126.com',
                     username='Lu Xuchao',
                     password='1',
                     confirmed=True,
                     name=forgery_py.name.full_name(),
                     location=forgery_py.address.city(),
                     about_me=forgery_py.lorem_ipsum.sentence(),
                     member_since=forgery_py.date.date(True))
    db.session.add(u2)

    u3 = User(email='674951896@qq.com',
                     username='Omnipresent',
                     password='123321',
                     role_id=2,
                     confirmed=True,
                     name=forgery_py.name.full_name(),
                     location=forgery_py.address.city(),
                     about_me=forgery_py.lorem_ipsum.sentence(),
                     member_since=forgery_py.date.date(True))
    db.session.add(u3)

    db.session.commit()

@manager.command
def revise():
    """Run deployment tasks."""
    from flask_migrate import init, migrate, upgrade
    from app.models import Role, User, Post

    init()
    migrate()
    upgrade()

    Role.insert_roles()

    User.add_self_follows()

    User.generate_fake()

    Post.generate_fake()

    import forgery_py
    u = User(email='clogadm@outlook.com',
                     username='Admin',
                     password='1',
                     confirmed=True,
                     name=forgery_py.name.full_name(),
                     location=forgery_py.address.city(),
                     about_me=forgery_py.lorem_ipsum.sentence(),
                     member_since=forgery_py.date.date(True))
    db.session.add(u)

    u2 = User(email='phillu@126.com',
                     username='Lu Xuchao',
                     password='1',
                     confirmed=True,
                     name=forgery_py.name.full_name(),
                     location=forgery_py.address.city(),
                     about_me=forgery_py.lorem_ipsum.sentence(),
                     member_since=forgery_py.date.date(True))
    db.session.add(u2)

    db.session.commit()

if __name__ == '__main__':
    manager.run()