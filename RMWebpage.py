from urllib.parse import urlparse


class RMWebpage:

    url = ""
    root = ""
    subroot = ""
    subdomains = []
    internals = []
    externals = []
    emails = []
    metawords = []
    metatext = []
    filtered = []
    def __init__(self,url):
        self.url = url
        self.root = urlparse(url).hostname
        domainls = self.root.split(".")
        self.subroot = "." + domainls[-2].replace("\n","") + "." + domainls[-1].replace("\n","")


    def addIfNotExists(self,item,ls:list):
        if item in ls:
            return ls.append(item)
        else:
            return ls
    def addLinks(self,links):
        for link in links:
            self.addLink(link)

    def addLink(self,link):


        state = False

        if self.subroot in link[0:(50 + len(self.subroot))]:
            print("Subdomain:" + link)
            targetlist = self.subdomains
            pass

        #if external
        if link.startswith("https" or link.startswith("http")):
            hostname = urlparse(link).hostname
            if hostname == self.root:
                pass #self.internals.append(link)
            else:
                self.addIfNotExists(link,self.externals)

        #if mail address
        elif link.startswith("mailto"):
            self.emails = self.addIfNotExists(link,self.emails)

        #if subsite
        else:
            self.internals = self.addIfNotExists(link,self.internals)


def getHostnameForPage(url):
    return urlparse(url).hostname

def printList(ls,prefix):
    res = ""
    for item in ls:
        res += prefix + item + "\n"
    return res

def writeWebpageToFile(webpage:RMWebpage, name:str):
    with open(name + ".txt","w",encoding="utf-8") as po:
        po.write(" url: " + webpage.url + "\n")
        po.write("root: " + webpage.root + "\n")

        po.write("\tsubdomain:" + "\n")
        po.write(printList(webpage.subdomains,"\t\t"))

        po.write("\tinternals:" + "\n")
        po.write(printList(webpage.internals,"\t\t"))

        po.write("\texternal:" + "\n")
        po.write(printList(webpage.externals,"\t\t"))

        po.write("\tmail:" + "\n")
        po.write(printList(webpage.emails,"\t\t"))

        po.write("\tmeta:" + "\n")
        po.write("\t\twords:" + "\n")
        po.write("\t\ttext:" + "\n")

        po.write("\tfiltered:" + "\n")
        po.write(printList(webpage.filtered,"\t"))
