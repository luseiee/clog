import os
basedir = os.path.abspath(os.path.dirname(__file__))

# The hierarchy of configuration class.
class Config:
	# The secret key is used in flask web form to prevent CSRF attack
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')
	pass

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}