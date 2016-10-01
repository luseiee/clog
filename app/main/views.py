from . import main
from flask import current_app, session, redirect, render_template, url_for, flash
from datetime import datetime
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_email

@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			session['known'] = False
			if current_app.config['FLASKY_ADMIN']:
				send_email(current_app.config['FLASKY_ADMIN'], 'New User',
						   'mail/new_user', user=user)
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		# use redirect to avoid form resubmit warning
		# the url_for must include the blueporint name
		return redirect(url_for('main.index'))
	return render_template('index.html', current_time=datetime.utcnow(), 
						   known=session.get('known', False), name=session.get('name'), form=form)

@main.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@main.route('/baidu')
def baidu():
	return redirect('http://www.baidu.com')