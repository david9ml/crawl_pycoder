import json
import gc
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import QWebSettings,QWebPage
import time
from pprint import pprint
import sys

app = QApplication(sys.argv)

class Render(QWebPage):
    def __init__(self, url):
        QWebPage.__init__(self)
        # Settings
        s = self.settings()
        s.setAttribute(QWebSettings.AutoLoadImages, False)
        s.setAttribute(QWebSettings.JavascriptCanOpenWindows, False)
        s.setAttribute(QWebSettings.PluginsEnabled, True)
        self.loadFinished.connect(self._loadFinished)
        self.html = None
        self.mainFrame().load(QUrl(url))
        start = time.clock()
        while time.clock() - start < 5.0 and self.html is None:
            app.processEvents()
        #self.app.exec_()
        #self.loadFinished.disconnect()
        #self.deleteLater()
    def _loadFinished(self, result):
        self.html = self.mainFrame().toHtml()
        #self.app.quit()

def get_content_by_link(url=''):
    #print "ok!"
    #print sys.getrefcount(Render)
    #print sys.getrefcount(QWebPage)
    r = Render(url)
    #print "ok!!!"
    result = r.html
    formatted_result = str(result.toAscii())
    return formatted_result


if __name__ == "__main__":
    with open('./links_out.txt') as linkfile:
        data = json.load(linkfile)
        data.reverse()
        pprint(data)
        for i, link in enumerate(data):
            #import sys
            #import render
            #reload(render)
            #from render import *
            #print sys.modules["render"]
            content = get_content_by_link(url=str(link))
            with open('./content/issue_%s.txt' % str(i+1), 'w+') as f:
                f.write(content)
            '''
            if 'render' in sys.modules:
                del sys.modules["render"]
                del render
                print 'delete render module'
                gc.collect()
            '''
            print 'issue_%s saved' % str(i+1)





