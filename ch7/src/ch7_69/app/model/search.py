# coding: utf-8

from pymongo import MongoClient
from config import MONGODB_HOST, MONGODB_PORT


class ArtistDBClient(object):

    def __init__(self):
        self.DB = None

    def fetch_artist(self, name, alias, tag):
        return self.DB.find({"name": name})

    def connect_db(self):
        # MongoDBへ接続
        client = MongoClient(MONGODB_HOST, MONGODB_PORT)
        db = client.local
        self.DB = db.artist
