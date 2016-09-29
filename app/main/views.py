# Use . to call __init__.py 
from . import main

@main.route('/')
def index():
	return '<h1>Hello World!</h1>'