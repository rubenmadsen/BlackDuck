import sqlite3 as sl

class RMDatabase:
    dbPath = "db/my-test.db"
    def addSubdomainForDomain(self,subdomain,domain):
        pass

    def addDomain(self,domain):
        con = sl.connect(self.dbPath)
        with con:
            #con.execute("""INSERT INTO `Domain`(`Domain`) values(10000001) ON DUPLICATE KEY UPDATE `EmployeeID` = 10000001""")
            #con.execute("""INSERT INTO `Domain`(`hostname`) values('""" + domain + """') """)
            con.execute("INSERT INTO `Domain`(`hostname`) values('" + domain + "') ON CONFLICT(hostname) DO UPDATE SET 'hostname' = '" + domain + "'")
            #query = "INSERT INTO `Domain`(`hostname`) values(" + domain + ")"
            #con.execute(query)


db = RMDatabase()
db.addDomain("www.rubenmadsen.com")
