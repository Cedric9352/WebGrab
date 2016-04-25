# coding=utf-8


class TextOutput(object):

    def __init__(self):
        self.data = list()

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def text_output(self):
        output = open(r'E:\jokes.txt', 'w')

        for joke_lists in self.data:
            for joke in joke_lists:
                output.write("%s\t" % joke['author'].encode('utf-8'))
                output.write("%d\t" % int(joke['vote']))
                output.write("%s\n" % joke['img_url'])
                output.write("%s\n\n" % joke['content'].encode('utf-8'))

        output.close()
