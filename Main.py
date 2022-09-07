import RMWebpage
from RMDatabase import RMDatabase
import os

from RMHTMLParser import RMHTMLParser

ROOT_DIR = os.path.abspath(os.curdir)

address = "http://www.aftonbladet.se"
con = RMDatabase()

aftonbladet = RMHTMLParser(address).parse()
for external in aftonbladet.externals:
    print(external)
    with open("out.txt","w", encoding="utf-8") as o:
        for page in RMHTMLParser(external).parse().externals:
            #con.addDomain(RMWebpage.getHostnameForPage(page))
            o.write(page)

stop = True
