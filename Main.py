from urllib.parse import urlparse
from RMHTMLParser import RMHTMLParser

address = "http://www.pornhub.com"
parser = RMHTMLParser(address)
#hostname = urlparse(address).hostname

print(parser.raw_data)
print(parser.tags)