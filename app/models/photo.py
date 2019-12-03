#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
photo.py
photo model
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-02'
from app.extensions import db
from app.models import Model


class Photo(Model):
    """ Photo Model
    """
    __tablename__ = 'photos'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', back_populates='photos')
