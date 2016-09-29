from . import main
from flask import request, redirect, render_template

@main.route('/')
def index():
	user_agent = request.headers.get('User-agent')
	return render_template('index.html')

@main.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@main.route('/baidu')
def baidu():
	return redirect('http://www.baidu.com')