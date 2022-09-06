
from RMParser import RMParser
from urllib.parse import urlparse
parser = RMParser("https://www.youtube.com")
hostname = urlparse("http://www.techcrunch.com/").hostname

print(hostname)
print(parser.raw_data)