# coding:utf-8

import urllib2


class HtmlDownloader(object):

    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def download(self, url):
        if url is None:
            return None

        try:
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            return response.read()

        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print '连接糗事百科失败，错误原因：', e.reason()
                return None

