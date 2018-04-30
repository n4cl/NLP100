# coding: utf-8

from pymongo import MongoClient
from config import MONGODB_HOST, MONGODB_PORT


class ArtistDBClient(object):

    def __init__(self, name, alias, tag):
        self.name = name
        self.alias = alias
        self.tag = tag
        self.DB = None

    def fetch_artist(self):
        return self.DB.find({"name": self.name})

    def connect_db(self):
        # MongoDBへ接続
        client = MongoClient(MONGODB_HOST, MONGODB_PORT)
        db = client.local
        self.DB = db.artist
