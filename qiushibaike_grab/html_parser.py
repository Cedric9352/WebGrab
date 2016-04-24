# coding:utf-8

import urlparse
import re
from bs4 import BeautifulSoup


class HtmlParser(object):

    @staticmethod
    def _next_page(page_url, soup):
        try:
            link = soup.find('span', class_="next").find_parent('a', href=re.compile(r'/hot/page/.*'))
            next_url = link['href']
            next_full_url = urlparse.urljoin(page_url, next_url)
            return next_full_url

        except Exception, e:
            print 'craw failed in getting next page'
            print e.message

    @staticmethod
    def _get_new_data(soup):
        res_lists = list()

        try:
            page_nodes = soup.find_all('div', class_="article block untagged mb15")
            for node in page_nodes:
                res_dict = dict()
                res_dict['author'] = node.find('a', href=re.compile(r'/user/\w+?/')).find('h2').get_text()
                res_dict['content'] = node.find('div', class_="content").get_text()
                res_dict['vote'] = node.find('i', class_="number").get_text()

                if node.find('img', src=re.compile(r'http://.*?\.jpg')) is not None:
                    res_dict['img_url'] = node.find('img', src=re.compile(r'http://.*?\.jpg'))['src']
                else:
                    res_dict['img_url'] = ""

                res_lists.append(res_dict)

            return res_lists

        except Exception, e:
            print "craw failed in getting new data"
            print e.message

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_next_url = self._next_page(page_url, soup)
        new_data = self._get_new_data(soup)

        return new_next_url, new_data
