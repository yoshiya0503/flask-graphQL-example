#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
user.py
user model
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-02'
from app.extensions import db
from app.models import Model


class User(Model):
    """ User Model
    """
    __tablename__ = 'users'

    name = db.Column(db.String(255), nullable=False)
    github_id = db.Column(db.String(255), nullable=False)
    avatar = db.Column(db.String(255), nullable=True)

    photos = db.relationship('Photo', back_populates='user')
