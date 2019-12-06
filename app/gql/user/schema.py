#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
schema.py
user schema
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-02'
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.user import User


class UserConnection(SQLAlchemyObjectType):
    class Meta:
        model = User
        # interfaces = (relay.Node, )
