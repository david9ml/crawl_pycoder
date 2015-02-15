import json
from pprint import pprint
import gc
import sh
import sys
from bs4 import BeautifulSoup
#from render import *

link = sys.argv[1]
file_name = sys.argv[2]

if __name__ == "__main__":
    content = sh.python('./render.py', str(link))
    content_str = str(content)
    content_str = content_str.replace('\\t', '').replace('\\n', '')
    soup = BeautifulSoup(content_str)
    content_formatted = unicode(soup.prettify()).encode('utf-8')
    with open('./content/%s' % str(file_name), 'w+') as f:
        f.write(content_formatted)
        print '%s saved' % str(file_name)


