import flask
import flask_api
import logging

from flask_api import status
from spacex_manifest import db_tools
from spacex_manifest import models  # required for visibility over models for SQLA metadata gathering
from spacex_manifest import data_extraction

logging.basicConfig(level=logging.DEBUG)

app = flask_api.FlaskAPI(__name__)
db = db_tools.database.Database('postgres://postgres:postgress@0.0.0.0:5432/postgres', drop_and_recreate_schema=True)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/boosters/', methods=['GET', 'POST'])
def boosters_list():
    if flask.request.method == 'POST':
        booster_name = str(flask.request.data.get('name', ''))  # TODO validate
        booster = models.hardware.BoostStage(name=booster_name)
        with db.managed_session as session:
            session.add(booster)
        return booster.serialise(), flask_api.status.HTTP_201_CREATED

    elif flask.request.method == 'GET':
        with db.managed_session as session:
            return [booster.serialise() for booster in data_extraction.get_boosters(session)]

@app.route('/boosters/<string:key>/', methods=['GET', 'PUT', 'DELETE'])
def boosters_detail(key):
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
