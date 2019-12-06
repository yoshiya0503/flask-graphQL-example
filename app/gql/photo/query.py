#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
query.py
photo query
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-02'
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from app.gql.photo.schema import PhotoConnection


class PhotoQuery(graphene.ObjectType):

    photos = SQLAlchemyConnectionField(PhotoConnection)
    photo_count = graphene.Int(required=True)

    def resolve_photo_count(self, info, **args):
        query = PhotoConnection.get_query(info)
        return query.count()
