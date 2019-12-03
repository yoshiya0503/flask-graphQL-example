#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
query.py
user query
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-02'
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from app.gql.user.schema import UserConnection


class UserQuery(graphene.ObjectType):

    users = SQLAlchemyConnectionField(UserConnection)
