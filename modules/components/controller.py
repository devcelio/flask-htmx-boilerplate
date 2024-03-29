from flask import Blueprint, render_template, request
from application import auth
from modules.core.models import Client
from flask_peewee.utils import object_list

blueprint = Blueprint('components', __name__, url_prefix='/components')
PAGE_SIZE = 5

@blueprint.route('/client/table')
def client_table():
    search = request.args.get('search', '')
    queryset = Client.select().where(Client.first_name.contains(search))
    return object_list('components/client/table.html', queryset, paginate_by=PAGE_SIZE)
