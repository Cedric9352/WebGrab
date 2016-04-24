# coding:utf-8


class TextOutput(object):

    def __init(self):
        self.data = list()

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def output_html(self):
        output = open(r'E:\jokes.txt', 'w')

        for joke_lists in self.data:
            for joke in joke_lists:
                output.write(joke['author']+"\t")
                output.write(joke['vote']+"\t")
                output.write(joke['img_url']+"\n")
                output.write(joke['content']+"\n\n")

        output.close()
