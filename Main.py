from urllib.parse import urlparse
from RMHTMLParser import RMHTMLParser


address = "http://www.aftonbladet.se"

aftonbladet = RMHTMLParser(address).parse()

for external in aftonbladet.externals:
    print(RMHTMLParser(external).parse().root)

stop = True