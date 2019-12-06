#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
photo input
photo_input.py
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-06'
import graphene


class PhotoInput(graphene.InputObjectType):
    user_id = graphene.Int(required=True)
    name = graphene.String(required=True)
    description = graphene.String(required=False)
    url = graphene.String(required=True)
    category = graphene.String(required=True)
