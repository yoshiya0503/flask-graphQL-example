#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
app.py
アプリケーション本体
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-01'
from inflection import camelize
from flask import Flask
from flask_migrate import Migrate
from flask_graphql import GraphQLView
from app.extensions import db
from app.transactions import Transaction
from app.gql import schema
from app.commands.seed import seed
from app.middlewares import Authentication


def create_app(env='development'):
    """ アプリケーションを作成する
    """
    app = Flask(__name__)
    if env not in ['development', 'production']:
        raise Exception('unkown environment. you should one of the development or production')
    config_path = 'config.{}.{}'.format(env, camelize(env))
    app.config.from_object(config_path)

    transaction = Transaction()

    # init app
    db.init_app(app)
    transaction.init_app(app)
    Migrate(app, db)

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, middleware=[Authentication()]))

    app.cli.add_command(seed)

    return app
