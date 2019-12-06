#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
muation.py
photo mutations
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-06'
import graphene
from app.extensions import db
from app.gql.photo.schema import PhotoConnection
from app.models.photo import Photo


class PhotoInput(graphene.InputObjectType):
    user_id = graphene.Int(required=True)
    name = graphene.String(required=True)
    description = graphene.String(required=False)
    url = graphene.String(required=True)
    category = graphene.String(required=True)


class CreatePhoto(graphene.Mutation):

    photo = graphene.Field(lambda: PhotoConnection)

    class Arguments:
        input = PhotoInput(required=True)

    def mutate(self, info, input=None):
        photo = Photo(**input)
        db.session.add(photo)
        return CreatePhoto(photo=photo)

class UpdatePhoto(graphene.Mutation):

    photo = graphene.Field(lambda: PhotoConnection)

    class Arguments:
        input = PhotoInput(required=True)

    def mutate(self, info, input=None):
        photo = Photo(**input)
        db.session.add(photo)
        return CreatePhoto(photo=photo)


class PhotoMutation(graphene.ObjectType):
    createPhoto = CreatePhoto.Field()
    updatePhoto = UpdatePhoto.Field()
