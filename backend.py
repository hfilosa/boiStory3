import os, sqlite3, csv, random 

db_name = "archive.db"

def go():
    if (not os.path.exists(db_name)):

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        q = """create table members (club text, submitter text, osis integer, title text, short_text text, long_text text, date text, id integer);"""
        c.execute(q)

        q = """insert into members values ("Dancing Pandas", "Henry Filosa", 208163568, "Announcement Database successfully created", "We did it",
        "This is the long version of this story","2016-05-18 09:30:0",1);"""
        
        c.execute(q)
        c.execute(w)

        conn.commit()


def addAnnouncement(club, submitter, osis, title, short_text, long_text,):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    i = iterate()
    q = """insert into members values ("%s","%s",%i);"""
    q = q%(u,p,i)
    c.execute(q)
    conn.commit()
        
def check():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    x = """SELECT * FROM members"""
    res = c.execute(x)
    for r in res:
        print r

def filterUname(uname):
    
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    
    q = """select user from members"""

    for i in c.execute(q):
        if i[0] == uname:
            return False
        
    return True
    
def iterate():

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    q = """select id from members;"""
    num = random.randint(100,999)
    for a in c.execute(q):
        if num == a:
            iterate()
    return num    

def checkPass(uname, passwd):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    q = """ select pwd from members where user = "%s" """ 
    q = q%(uname)

    for line in c.execute(q):
        print passwd
        print line[0]
        if line[0] == passwd:
            print "true"
            return True
        else:
            print "false"
            return False

go()    
check()
