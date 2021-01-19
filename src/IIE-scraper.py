import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as Soup
import html
from html.parser import HTMLParser
import re
from pprint import pprint


def main():
    """ Main entry point of the app """
    tree = ET.parse('./IIE.xml')
    root = tree.getroot()

    item = root.find('*/item')
    extags = html.unescape((item[3].text))

    soup = Soup(extags, 'html.parser')
    # headers = soup.find_all("h1")
    # for header in headers:
    #     print(header.get_text())
    # print()
    # aTags = (soup.find_all("a"))
    # for tag in aTags:
    #     print(tag.get_text())
    #     print("")

    content = {}
    count = 0
    for header in soup.find_all('h1'):
        second = {}
        # print(header.get_text())
        li = soup.find_all('td', {'class': 'mcnTextContent'})[count:]

        for l in li:
            children = l.findChildren("a", recursive=False)
            for child in children:
              #      print(child.get('href'))
                second.setdefault(child.get_text(), child.get('href'))
            count += 1
            if(len(children) > 0):
                break

        content.setdefault(header.get_text(), second)
        #print(" ")

    print(content)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
