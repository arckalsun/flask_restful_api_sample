#!/usr/bin/python3
# encoding: utf-8

'''
@project: crawler_server
@author: sunkuanwei
@email: arckalsun@gmail.com
@file: config
@time: 2019/3/6 9:46 
'''

class Config(object):
    SECRET_KEY = ''


class DevelopmentConfig(Config):
    DEBUG = True

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6370
    REDIS_DB = 4
    REDIS_PASSWORD = ''

    MONGODB_INFO = ''

class ProductionConfig(Config):
    DEBUG = False

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6370
    REDIS_DB = 4
    REDIS_PASSWORD = ''

    MONGODB_INFO = ''

Conf = DevelopmentConfig