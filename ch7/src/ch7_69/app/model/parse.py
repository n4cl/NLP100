# coding: utf-8

from urlparse import urlparse, parse_qs


class URLParser(object):

    def __init__(self, url):
        self.url = url
        self.parse_result = {}
        self.parm = {}

    def parse(self):
        self.parse_result = urlparse(self.url)
        # 未入力のクエリーも一応返す
        self.parm = parse_qs(qs=self.parse_result.query, keep_blank_values=True)

    def get_parm(self):
        return self.parm

if __name__ == '__main__':
    URL = URLParser("http://localhost:5000/search?artist=xxx&tag=zzz")
    URL.parse()
    assert URL.get_parm() == {"artist": ["xxx"], "tag": ["zzz"]}
