# -*- coding:utf-8 _*-
"""
@file: configs.py
    ENV = 'dev'  # 开发环境
    ENV = 'test'  # 测试环境
    ENV = 'prehub'  # 预发布环境
    ENV = 'prod'  # 生产环境
"""
import json


class Config(object):
    ENV_DEV = False
    ENV_TEST = False
    ENV_PREHUB = False
    ENV_PROD = False


class ProdConfig(Config):
    '''
    生产环境配置
    '''
    ENV_PROD = True


class PrehubConfig(Config):
    '''
    预发布环境配置
    '''
    ENV_PREHUB = True


class DevelopmentConfig(Config):
    '''
    开发环境配置
    '''
    ENV_DEV = True


class TestingConfig(Config):
    '''
    测试环境配置
    '''
    ENV_TEST = True


def load_json_file(file_json):
    with open(file_json, 'r') as load_f:
        s = json.load(load_f)
    return s


def dump_json_file(data, file_json):
    with open(file_json, 'w', encoding='utf-8') as dump_f:
        json.dump(data, dump_f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print(__file__)
    data = load_json_file(r"E:\Development\1-Pre-Alpha\sound_animation\tests\test_config\configs.json")
    print(data["ENV"])
