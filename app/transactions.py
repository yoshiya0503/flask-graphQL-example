#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
transactions.py
トランザクションをリクエスト単位で行う
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-02'
from flask import current_app
from app.extensions import db


class Transaction(object):

    def init_app(self, app):
        """ トランザクションを定義する
        """
        @app.after_request
        def transaction_400(response):
            if current_app.testing:
                return response
            if response.status_code >= 400:
                db.session.rollback()
            return response

        @app.teardown_request
        def transaction_500(exceptions):
            if current_app.testing:
                return
            if exceptions:
                db.session.rollback()
            else:
                db.session.commit()
