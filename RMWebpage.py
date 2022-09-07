from urllib.parse import urlparse


class RMWebpage:

    url = ""
    root = ""
    subdomains = []
    subsites = []
    externals = []
    emails = []
    def __init__(self,url):
        self.url = url
        self.root = urlparse(url).hostname
    def addLinks(self,links):
        for link in links:
            self.addLink(link)

    def addLink(self,link):
        if link.startswith("https" or link.startswith("http")):
            hostname = urlparse(link).hostname
            if hostname == self.root:
                self.subsites.append(link)
            else:
                self.externals.append(link)

        elif link.startswith("mailto"):
            self.emails.append(link)
        else:
            self.subsites.append(link)