#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Config.py
設定ファイル基底クラス
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-01'


class Config(object):
    HOST = '0.0.0.0'

    FLASK_ENV = 'test'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@db:3306/example?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
