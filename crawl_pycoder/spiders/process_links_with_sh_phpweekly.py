import json
from pprint import pprint
import sh
from bs4 import BeautifulSoup
#from render import *


if __name__ == "__main__":
    with open('./php_weekly_links.txt') as linkfile:
        data = json.load(linkfile)
        data.reverse()
        pprint(data)
        for i, link in enumerate(data):
            content = sh.python('./render.py', 'http://www.phpweekly.com' + str(link))
            content_str = str(content)
            linkname = map(lambda x : x.split('/')[2], [str(link)])[0]
            content_str = content_str.replace('\\t', '').replace('\\n', '')
            soup = BeautifulSoup(content_str)
            content_formatted = unicode(soup.prettify()).encode('utf-8')
            with open('./php_weekly_dump/issue_%s.html' % str(linkname), 'w+') as f:
                f.write(content_formatted)
            print 'issue_%s saved' % str(link)





