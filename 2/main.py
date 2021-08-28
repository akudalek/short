# -*- coding: utf-8 -*-
import json
import math
from base64 import b64encode

import flask
from flask import request, send_from_directory
from flask_cors import cross_origin, CORS

from src.database.model import Cats
from src.database.service import count_cats, read_cat
from src.functions import get_list_sheets, get_cats_image
from src.getenvironment import *


def set_json(data):
    return json.dumps(data, ensure_ascii=False)


def resp(code, data):
    return flask.Response(
        mimetype="application/json",
        status=code,
        response=set_json(data)
    )


app = flask.Flask(__name__,
                  template_folder='static/templates')
CORS(app)

@app.route('/root')
@app.route('/login')
def root():
    return flask.redirect('/')


@app.errorhandler(400)
def page_not_found(e):
    return resp(400, {})


@app.errorhandler(404)
def page_not_found(e):
    return resp(400, {})


@app.errorhandler(405)
def page_not_found(e):
    return resp(405, {})


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/templates'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET'])
@app.route('/<sheet>', methods=['GET'])
@cross_origin()
def index(sheet: int = 0):
    return flask.render_template('index.html', list_sheets=get_list_sheets(count_sheets=math.ceil(count_cats()/show_pagination),
                                                                           number_sheets=int(sheet)),
                                 cats=get_cats_image()[int(sheet)*show_pagination:int(sheet)*show_pagination+5])


@app.route('/cat/<id>', methods=['GET'])
@cross_origin()
def cat_page(id):

    cat: Cats = read_cat(id=id)
    return flask.render_template('cat.html',
                                 id=cat.id,
                                 name=cat.name,
                                 breed=cat.breed,
                                 age=cat.age,
                                 description=cat.description,
                                 img=b64encode(cat.img).decode("utf-8"))


@app.route('/search', methods=['GET'])
@cross_origin()
def search():
    tmp = request
    cat: Cats = read_cat(id=id)
    return flask.render_template('cat.html',
                                 id=cat.id,
                                 name=cat.name,
                                 breed=cat.breed,
                                 age=cat.age,
                                 description=cat.description,
                                 img=b64encode(cat.img).decode("utf-8"))


if __name__ == '__main__':
    app.config.update(
        JSON_AS_ASCII=False)
    app.config['DEBUG'] = False
    app.run(host=host, port=port)
