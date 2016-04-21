import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

post_data = urllib.urlencode({'j_username': '21150911087',
             'pwd': 'cyj19920409'})


url = 'http://graduate.ouc.edu.cn/'
opener.open(url, post_data)
cookie.save(ignore_discard=True, ignore_expires=True)
result = opener.open('http://graduate.ouc.edu.cn/frameset.jsp')
print result.read()