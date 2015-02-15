from bs4 import BeautifulSoup


html_doc = None
with open ("./issue_1.html", "r") as myfile:
    html_doc=myfile.read()

soup = BeautifulSoup(html_doc)
#print unicode(soup.prettify()).encode('utf-8')
print soup.find_all('a')
