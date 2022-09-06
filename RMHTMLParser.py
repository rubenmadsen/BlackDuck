import urllib.request


class Tag:
    type = ""
    attr = ""
    startIndex = 0
    length = 0

class RMHTMLParser:
    tagnames = []
    cursor = 0
    raw_data = ""
    tags = []

    def __init__(self, url):
        self.tagnames = self.getTagNamesFromFile()
        self.raw_data = getWebsiteAsString(url)
        self.refactorFile()
        self.parse(self.cursor,self.raw_data)
    def refactorFile(self):
        #self.raw_data = self.raw_data.replace("\n","")
        print(self.raw_data)

    def parse(self,start,data):
        for pos in range(start, len(data)):
            if data[pos] == '<':
                pos += 1
                tag = self.extraxtTag(data,pos)
                self.cursor += tag.length
                self.tags.append(tag)
            self.cursor += 1

    def extraxtTag(self,data,index):
        tag = Tag()
        tag.startIndex = index
        length = 0
        pos = index
        t = data[pos]
        attr = ""
        while(data[pos] != '>'):
            attr += data[pos]
            pos += 1
        tag.length = pos-tag.startIndex
        tag.attr = data
        for t in self.tagnames:
            if data.startswith(t):
                tag.type = t
        return tag

    def extractAttributes(self,data,index):
        pass

    def getTagNamesFromFile(this):
        names = []
        with open("htmltags.txt","r") as fi:
            for line in fi:
                names.append(line.replace("\n",""))

        #print(names)
        return names

def getWebsiteAsString(url) -> str:
    req = urllib.request.urlopen(url)
    mybytes = req.read()
    stringData = mybytes.decode("utf8")
    return mybytes.decode("utf8")



address = "http://www.pornhub.com"
parser = RMHTMLParser(address)
stop = True