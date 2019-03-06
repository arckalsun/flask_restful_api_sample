#!/usr/bin/python3
# encoding: utf-8

'''
@project: crawler_server
@author: sunkuanwei
@email: arckalsun@gmail.com
@file: crawl
@time: 2019/3/5 19:34 
'''
from flask import request,current_app
from flask_restful import Resource
from ..decorator import sign_check


class ArticleCrawlAPI(Resource):
    '''爬取作者文章，返回文章信息'''

    @sign_check(app=current_app)
    def get(self):
        ret = {
            "code": 0,
            "msg": "success"
        }
        current_app.logger.info('get crawl')
        ret['data'] = 'data'
        return ret

    @sign_check(app=current_app)
    def post(self):
        ret = {
            "code": 0,
            "msg": "success"
        }
        current_app.logger.info('post crawl')
        ret['data'] = 'data'
        return ret