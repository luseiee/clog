from . import main
from flask import render_template

# Use app_errorhandler to make it callable for every blueprint
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@main.app_errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403