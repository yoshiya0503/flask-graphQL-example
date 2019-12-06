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
from app.gql.photo.create_photo import CreatePhoto
from app.gql.photo.update_photo import UpdatePhoto



class PhotoMutation(graphene.ObjectType):
    createPhoto = CreatePhoto.Field()
    updatePhoto = UpdatePhoto.Field()
