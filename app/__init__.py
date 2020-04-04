#!/usr/bin/env python

import os
import re

from flask import Flask, request, redirect, make_response, g
from flask_migrate import Migrate

from config import config
from db import database as db

migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)

    # config app
    app.config.from_object(config[config_name])
    # app.config.from_mapping(
    #     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI'],
    # )
    # app.config['SQLALCHEMY_ECHO'] = True
    # config[config_name].init_app(app)

    # initialize other plug-ins
    db.init_app(app)
    migrate.init_app(app, db)

    public_url_patterns = map(re.compile, [
        '/static/',
        '/favicon.ico',
        '/logout',
        '/authorization_response',
        '/health-check',
    ])
    json_url_patterns = map(re.compile, [
        '/whoami',
        '/api'
    ])

    from app.api import api_1_0
    app.register_blueprint(api_1_0, url_prefix='/api/1.0/')

    @app.before_request
    def authenticate_request():
        for p in public_url_patterns:
            if p.match(request.path):
                return None
        # TODO: authenticate incoming request
        # if authenticated, set g.current_user and return None
        g.current_user = object()
        return None


    @app.route('/logout')
    def logout():
        return redirect(location='/')


    @app.route('/authorization_response')
    def authorization_response():
        original_url = request.args['r']
        response = redirect(location=original_url)
        return response


    @app.route('/health-check')
    def health_check():
        return make_response('OK', 200, {'Content-Type': 'text/plain'})

    return app
