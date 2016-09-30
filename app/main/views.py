from . import main
from flask import session, redirect, render_template, url_for, flash
from datetime import datetime
from .forms import NameForm

@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name!=form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		# use redirect to avoid form resubmit warning
		# the url_for must include the blueporint name
		return redirect(url_for('main.index'))
	return render_template('index.html', current_time=datetime.utcnow(), name=session.get('name'), form=form)

@main.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@main.route('/baidu')
def baidu():
	return redirect('http://www.baidu.com')