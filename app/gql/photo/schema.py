#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
schema.py
photo schema
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-02'
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.photo import Photo


class PhotoConnection(SQLAlchemyObjectType):
    class Meta:
        model = Photo
        interfaces = (relay.Node, )
