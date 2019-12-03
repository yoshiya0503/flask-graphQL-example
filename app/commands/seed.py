#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
seed.py
seed data
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-03'
import click
from flask.cli import with_appcontext, AppGroup
from app import db
from app.models import User
from app.models import Photo

seed = AppGroup('seed', help='シードデータ関連')

@seed.command('sample')
@with_appcontext
def sample():
    """ create sample data
    """
    users = [
        User(name='test1', github_id='yoshiya0503', avatar=''),
        User(name='test2', github_id='yoshiya0503', avatar=''),
        User(name='test3', github_id='yoshiya0503', avatar=''),
        User(name='test4', github_id='yoshiya0503', avatar=''),
        User(name='test5', github_id='yoshiya0503', avatar=''),
    ]

    for user in users:
        user.photos = [
            Photo(name='photo 1', url='https://avatars1.githubusercontent.com/u/5334715?s=460&v=4', description='desc', category='category1'),
            Photo(name='photo 2', url='https://avatars1.githubusercontent.com/u/5334715?s=460&v=4', description='desc', category='category2'),
            Photo(name='photo 3', url='https://avatars1.githubusercontent.com/u/5334715?s=460&v=4', description='desc', category='category3'),
        ]
    db.session.add_all(users)
    db.session.commit()
