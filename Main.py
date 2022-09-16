import RMWebpage
from RMDatabase import RMDatabase
import os
from RMHTMLParser import RMHTMLParser

from pathlib import Path
#Path("/my/directory").mkdir(parents=True, exist_ok=True)



address = "http://www.aftonbladet.se"
con = RMDatabase()

aftonbladet = RMHTMLParser(address).parse()
RMWebpage.writeWebpageToFile(aftonbladet,"aftonbladet")
RMWebpage.writeWebpageToFolderStructure(aftonbladet)
"""for external in aftonbladet.externals:
    print(external)
    with open("out.txt","w", encoding="utf-8") as o:
        for page in RMHTMLParser(external).parse().externals:
            #con.addDomain(RMWebpage.getHostnameForPage(page))
            o.write(page)
            print("page:" + page)
"""
stop = True
