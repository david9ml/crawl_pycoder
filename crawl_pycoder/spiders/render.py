from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import QWebSettings,QWebPage
from pprint import pprint
#from PyQt4.QtWebKit import *
#from lxml import html
import sys
arg =  sys.argv[1]
#print arg

class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        # Settings
        s = self.settings()
        s.setAttribute(QWebSettings.AutoLoadImages, False)
        s.setAttribute(QWebSettings.JavascriptCanOpenWindows, False)
        s.setAttribute(QWebSettings.PluginsEnabled, True)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        #self.loadFinished.disconnect()
        #self.deleteLater()
    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()

def get_content_by_link(url=''):
    #print "ok!"
    #print sys.getrefcount(Render)
    #print sys.getrefcount(QWebPage)
    r = Render(url)
    #print "ok!!!"
    result = r.frame.toHtml()
    formatted_result = str(result.toAscii())
    return formatted_result

pprint(get_content_by_link(str(arg)))


