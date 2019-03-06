#!/usr/bin/python3
# encoding: utf-8

'''
@project: crawler_server
@author: sunkuanwei
@email: arckalsun@gmail.com
@file: add
@time: 2019/3/6 10:26 
'''
from flask import request
from flask_restful import Resource
from ..decorator import sign_check
from flask import current_app


class ArticleAddAPI(Resource):
    '''添加文章'''

    @sign_check(app=current_app)
    def post(self):
        ret = {
            "code": 0,
            "msg": "success"
        }
        current_app.logger.info('add article')
        # 业务逻辑

        current_app.logger.info('add article finish')
        ret['data'] = 'add article finish'
        return ret
