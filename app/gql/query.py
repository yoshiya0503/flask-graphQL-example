#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
query.py
root query
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-02'
import graphene
from app.gql.photo.query import PhotoQuery
from app.gql.user.query import UserQuery

class Query(
    UserQuery,
    PhotoQuery,
    graphene.ObjectType):
    pass
