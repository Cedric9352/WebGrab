# coding=utf-8


class HtmlOutput(object):
    def __init__(self):
        self.data = list()

    def collect_data(self, data):
        if data is None:
            return
        self.data.append(data)

    def output_html(self):
        output = open(r'E:\output.html', 'w')

        output.write("<html>")
        output.write("<body>")
        output.write("<table>")

        for data in self.data:
            output.write("<tr>")
            output.write("<td>%s</td>" % data['url'])
            output.write("<td>%s</td>" % data['title'].encode('utf-8'))
            output.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            output.write("</tr>")

        output.write("</table>")
        output.write("</body>")
        output.write("</html>")

        output.close()
