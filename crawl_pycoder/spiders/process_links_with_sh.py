import json
from pprint import pprint
import gc
import sh
from bs4 import BeautifulSoup
#from render import *


if __name__ == "__main__":
    with open('./links_out.txt') as linkfile:
        data = json.load(linkfile)
        data.reverse()
        pprint(data)
        for i, link in enumerate(data):
            content = sh.python('./render.py', str(link))
            content_str = str(content)
            content_str = content_str.replace('\\t', '').replace('\\n', '')
            soup = BeautifulSoup(content_str)
            content_formatted = unicode(soup.prettify()).encode('utf-8')
            with open('./content/issue_%s.html' % str(i+1), 'w+') as f:
                f.write(content_formatted)
            print 'issue_%s saved' % str(i+1)





