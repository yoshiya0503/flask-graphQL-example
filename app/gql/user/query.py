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

    # users = SQLAlchemyConnectionField(UserConnection)
    # user = graphene.Field(UserConnection, id=graphene.Int())
    users = graphene.List(UserConnection)
    user = graphene.Field(UserConnection, id=graphene.Int())

    def resolve_user(self, info, id):
        query = UserConnection.get_query(info)
        return query.filter_by(id=id).first()

    def resolve_users(self, info):
        query = UserConnection.get_query(info)
        return query.all()
