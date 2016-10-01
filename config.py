import os
basedir = os.path.abspath(os.path.dirname(__file__))


# The hierarchy of configuration class.
class Config:
	# The secret key is used in flask web form to prevent CSRF attack
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	MAIL_SERVER = 'smtp.126.com'
	MAIL_PORT = 25
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'phillu@126.com'
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '7z8i0k33'
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flasky Admin <phillu@126.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or '<phillu@126.com>'

class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')
	pass

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}