#!/usr/bin/python3
# encoding: utf-8

'''
@project: crawler_server
@author: sunkuanwei
@email: arckalsun@gmail.com
@file: __init__.py
@time: 2019/3/5 17:51 
'''
from flask import Blueprint
from flask_restful import Api
from .articles.crawl import ArticleCrawlAPI
from .articles.add import ArticleAddAPI

def register_views(app):
    api = Api(app)
    api.add_resource(ArticleCrawlAPI,'/article/crawl')
    api.add_resource(ArticleAddAPI,'/article/add')

def create_blueprint_v1():
    '''
    注册蓝图->v1版本
    '''
    bp_v1 = Blueprint('v1',__name__)
    register_views(bp_v1)
    return bp_v1