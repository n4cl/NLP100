# coding: utf-8

from ConfigParser import SafeConfigParser
from abc import ABCMeta, abstractmethod
"""
設定ファイルを読み込む
"""


class ConfigReader(object):
    """
    コンフィグを読み取る
    """
    __metaclass__ = ABCMeta

    def __init__(self, path):
        self.__path = path
        self.__config_path = path
        self.__config = SafeConfigParser()
        self.__config.read(self.__config_path)

    def get_config(self):
        return self.__config

    @abstractmethod
    def read_config(self):
        pass


class RedisConfig(ConfigReader):
    """
    Redisのコンフィグを読み取る
    """
    def __init__(self, path):
        super(RedisConfig, self).__init__(path)

    def read_config(self):
        config = super(RedisConfig, self).get_config()
        section = "redis"
        host = config.get(section, "host")
        port = config.get(section, "port")
        db = config.get(section, "db")
        return host, port, db


class MongoDBConfig(ConfigReader):
    """
    MongoDBのコンフィグを読み取る
    """
    def __init__(self, path):
        super(MongoDBConfig, self).__init__(path)

    def read_config(self):
        config = super(MongoDBConfig, self).get_config()
        section = "mongodb"
        host = config.get(section, "host")
        port = config.get(section, "port")
        return host, port

if __name__ == '__main__':
    redis = RedisConfig("config.ini")
    mongodb = MongoDBConfig("config.ini")
    print redis.read_config()
    print mongodb.read_config()
