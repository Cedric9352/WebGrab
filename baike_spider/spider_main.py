# coding=utf-8
from baike_spider import url_manager, html_downloader, html_parser, html_output


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()    # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # html下载器
        self.parser = html_parser.HtmlParser()  # html解析器
        self.output = html_output.HtmlOutput()    # html输出器

    def craw(self, root):   # 调度程序
        count = 1
        try:
            self.urls.add_new_url(root)  # 入口url
            while self.urls.has_new_url():  # 当有url时
                new_url = self.urls.get_new_url()   # 获取该url
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)   # 下载该url内容
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 当前爬取的url和下载数据
                self.urls.add_new_urls(new_urls)    # 加入现在的urls
                self.output.collect_data(new_data)    # 收集数据

                if count == 20:
                    break

                count += 1
        except Exception, e:
            print e.message
            print 'craw failed'

        self.output.output_html()  # 输出

if __name__ == '__main__':
    url = open("url.txt")
    url_full = "".join(url.readlines())
    root_url = url_full
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
