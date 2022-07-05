# -*- coding:utf-8 _*-
"""
@file: raw_main.py
"""

import sys

import flask

import test_configs as config

if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 2 else 'dev'

    app = flask.Flask(__name__)

    if env == 'dev':
        app.config = config.DevelopmentConfig
    elif env == 'test':
        app.config = config.TestingConfig
    elif env == "prehub":
        app.config = config.ProdConfig
    elif env == 'prod':
        app.config = config.ProdConfig
    else:
        raise ValueError('Invalid environment name')