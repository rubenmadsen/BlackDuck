import urllib.request
import RMSeeker

class Tag:
    type = ""
    attr = []
    data = ""
    isEndTag = False

class RMHTMLParser():
    tagnames = []
    cursor = -1
    raw_data = ""
    tags = []

    def __init__(self, url):
        self.tagnames = self.getTagNamesFromFile()
        self.raw_data = getWebsiteAsString(url)
        self.refactorRawData()
        self.parse(self.cursor,self.raw_data)

    def refactorRawData(self):
        self.raw_data = self.raw_data.replace('\n','').replace('\r','').replace('\t','')
        #print(self.raw_data)

    def getNext(self):
        if self.hasNext():
            self.cursor += 1
            char = self.raw_data[self.cursor]
            return char
    def peekNext(self):
        if self.hasNext():
            return self.raw_data[(self.cursor+1)]
    def hasNext(self) -> bool:
        if self.cursor < len(self.raw_data)-1:
            return True
        else:
            return False

    def parse(self,start,data):
        #print(self.raw_data)
        while(self.hasNext()):
            char = self.getNext()
            while(char != '<'):
                char = self.getNext()
            self.extractTag()


    def extractTag(self):
        tag = Tag()
        data = ""
        char = self.getNext()

        while (char != '>'):
            data += char
            char = self.getNext()

        if(len(data) != 0):
            if (data[0] == "/"):
                tag.isEndTag = True
                data = data[1:0]
        end = data.find(" ")
        tag.type = data[0:end]
        stop = 1

        for tagname in self.tagnames:
            if(tag.type == tagname):
                tag.data = data[end+1:]

                #if( tag.type.startswith("</")):
                    #tag.isEndTag = True
                #print(tagname)
                break

        tag.type = "<" + tagname + ">"
        self.extractAttributes(tag)
        self.tags.append(tag)
        #print((tag.type))
        #print((tag.data))


    def extractAttributes(self,tag):
        tag.attr = tag.data.split(" ")
        stop = 1

    def getAllTagsOfType(self,type):
        ls = []
        for tag in self.tags:
            if tag.type == type:
                ls.append(tag)
        return ls

    def getTagNamesFromFile(this):
        names = []
        with open("htmltags.txt","r") as fi:
            for line in fi:
                names.append(line.replace("\n",""))

        #print(names)
        return names
    def writeTagsToFile(self):
        with open("structuredtags.txt","w", encoding="utf-8") as fo:
            level = 0
            for tag in self.tags:
                out = tag.type
                if(tag.isEndTag):
                    out = "*" + out
                fo.write(out + "\n")
                for att in tag.attr:
                    fo.write("\t" + att + "\n")

def getWebsiteAsString(url) -> str:
    req = urllib.request.urlopen(url)
    mybytes = req.read()
    stringData = mybytes.decode("utf8")
    add = "<meta http-equiv='Content-type' content='text/html; charset=UTF-8' />"
    #stringData = add + stringData
    return stringData



address = "http://www.pornhub.com"
parser = RMHTMLParser(address)
parser.writeTagsToFile()
ls = parser.getAllTagsOfType("<a>")
atts = []
for tag in ls:
    for att in tag.attr:
        if att.startswith("href"):
            atts.append(att)
            printatt = att.lstrip("href=")
            print(printatt)
print(str(len(ls) )+ " links found.")
print(str(len(atts) )+ " atts found.")
stop = True