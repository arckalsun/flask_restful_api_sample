#!/usr/bin/python3
# encoding: utf-8

'''
@project: crawler_server
@author: sunkuanwei
@email: arckalsun@gmail.com
@file: app
@time: 2019/3/5 19:53 
'''
from apps import register_blueprints
from flask import Flask
from config import Conf
import logging
from logging.handlers import TimedRotatingFileHandler
import redis
import os


def create_app():
    if not os.path.exists('logs'): os.mkdir('logs')
    handler = TimedRotatingFileHandler('logs/flask.log',when='D')
    logging_format = logging.Formatter(
        '[%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - line:%(lineno)s]: %(message)s')
    handler.setFormatter(logging_format)

    app = Flask(__name__)
    app.config.from_object(Conf)
    app.secret_key = app.config['SECRET_KEY']
    app.redis = redis.StrictRedis(host=app.config['REDIS_HOST'],
                                  port=app.config['REDIS_PORT'],
                                  db=app.config['REDIS_DB'],
                                  password=app.config['REDIS_PASSWORD'],)
    app.debug = app.config['DEBUG']

    app.logger.addHandler(handler)
    register_blueprints(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()