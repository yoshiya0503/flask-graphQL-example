#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
create_photo.py
photo mutation
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-06'
import graphene
from app.extensions import db
from app.gql.photo.schema import PhotoConnection
from app.gql.photo.input import PhotoInput
from app.models.photo import Photo


class CreatePhoto(graphene.Mutation):

    photo = graphene.Field(lambda: PhotoConnection)

    class Arguments:
        input = PhotoInput(required=True)

    def mutate(self, info, input=None):
        photo = Photo(**input)
        db.session.add(photo)
        return CreatePhoto(photo=photo)
