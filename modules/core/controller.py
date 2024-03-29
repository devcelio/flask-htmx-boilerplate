from flask import Blueprint, render_template


blueprint = Blueprint('core', __name__)

@blueprint.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/settings')
def settings():
    return render_template('settings.html')
