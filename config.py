import os

# The hierarchy of configuration class.
class Config:
	# The secret key is used in flask web form to prevent CSRF attack
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

class DevelopmentConfig(Config):
	pass

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}