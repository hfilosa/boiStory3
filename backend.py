import os, sqlite3, csv, random 

db_name = "archive.db"

def go():
    if (not os.path.exists(db_name)):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        q = """create table announcements (club text, submitter text, osis integer, title text, short_text text, long_text text, date text, id integer);"""
        c.execute(q)
        q = """insert into announcements values ("Dancing Pandas", "Henry Filosa", 208163568, "Announcement Database successfully created", "We did it","This is the long version of this story","2016-05-18 09:30:0",1);"""
        c.execute(q)
        conn.commit()


def addAnnouncement(club, submitter, osis, title, short_text, long_text, date, id_num):

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    i = iterate()
    q = """insert into announcements values ("%s","%s",%i,"%s","%s","%s","%s","%i");"""
    q = q%(club,submitter,osis,title, short_text, long_text, date, id_num)
    c.execute(q)
    conn.commit()


def check():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    q = """SELECT * FROM announcements"""
    res = c.execute(q)
    for r in res:
        print r
    
def getAnnouncementByDate(start_date,end_date):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    q = """SELECT * FROM announcements where DATE(date) between '%s' and '%s'; """
    #q = """SELECT * FROM announcements where 'date' >= '%s' and 'date' <= '%s'"""
    q = q%(start_date,end_date)
    res = c.execute(q)
    for r in res:
        print r

go()    
#check()
getAnnouncementByDate("2016-05-17","2016-05-20");
