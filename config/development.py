#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Development.py
development 環境の設定
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-01'


class Development(object):
    HOST = '0.0.0.0'

    FLASK_ENV = 'test'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@db:3306/example?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
