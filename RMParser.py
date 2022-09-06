import urllib.request


class RMParser:
    raw_data = ""

    def __init__(self, url):
        self.raw_data = getWebsiteAsString(url)


def getWebsiteAsString(url) -> str:
    req = urllib.request.urlopen(url)
    mybytes = req.read()
    return mybytes.decode("utf8")
