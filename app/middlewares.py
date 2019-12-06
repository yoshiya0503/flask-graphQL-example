#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
middlewares.py
GraphQL Middlewares
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '1.0.0'
__date__ = '2019-12-06'


class Authentication(object):
    def resolve(self, next, root, info, **args):
        if root is None:
            print('check authentication')
            return next(root, info, **args)
