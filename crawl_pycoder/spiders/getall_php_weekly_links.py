import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from lxml import html
import json

class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
    self.frame = self.mainFrame()
    self.app.quit()

url = 'http://www.phpweekly.com/archive.html'
#This does the magic.Loads everything
r = Render(url)
#result is a QString.
result = r.frame.toHtml()
#QString should be converted to string before processed by lxml
formatted_result = str(result.toAscii())

#Next build lxml tree from formatted_result
tree = html.fromstring(formatted_result)

archive_links = tree.xpath('//div[@class="archive-d"]/h3/a/@href')
print type(archive_links)
with open('php_weekly_links.txt', 'w+') as outfile:
    json.dump(archive_links, outfile)
