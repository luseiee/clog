# The blueprint is dormant until it is registered with an application.
from flask import Blueprint

main = Blueprint('main', __name__)

# We have to import the routers and error handlers to associate them to the blueprint.
from . import views, errors

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)