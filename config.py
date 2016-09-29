# The hierarchy of configuration class.
class Config:
	pass

class DevelopmentConfig(Config):
	pass

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig
}