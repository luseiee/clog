from . import main
from flask import request, redirect

@main.route('/')
def index():
	user_agent = request.headers.get('User-agent')
	return '<h1>Hello World! Your browser is %s</h1>' % (user_agent)

@main.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1.' % (name)

@main.route('/baidu')
def baidu():
	return redirect('http://www.baidu.com')