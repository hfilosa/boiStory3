import os, sqlite3, csv, random 

db_name = "archive.db"

def go():
    if (not os.path.exists(db_name)):
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        q = """create table announcements (club text, submitter text, osis text, title text, short_text text, long_text text, date text, id integer);"""
        c.execute(q)
        q = """insert into announcements values ("Dancing Pandas", "Henry Filosa", "208163568", "Announcement Database successfully created", "We did it","This is the long version of this story","2016-05-18",1);"""
        c.execute(q)
        conn.commit()

"""======== Null addAnnouncement(club, submitter, osis, title, short_text, long_text, date, id_num) ==========
Inputs: club        -> The club or team submitting the announcement
        submitter   -> The name of the person who submitted the announcement
        osis        -> The osis of the person who submitted the announcement
        title       -> The title of the announcement
        short_text  -> The short form of the announcement
        long_text   -> The long form of the announcement
        date        -> The time the announcement is logged as YYYY-MM-DD
Returns: 
  Nothing
"""
def addAnnouncement(club, submitter, osis, title, short_text, long_text, date):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    q = """SELECT MAX(id) FROM announcements"""
    res = c.execute(q)
    for r in res:
        id_num=r[0]+1
    q = """insert into announcements values ("%s","%s",%s,"%s","%s","%s","%s","%i");"""
    q = q%(club,submitter,osis,title, short_text, long_text, date, id_num)
    c.execute(q)
    conn.commit()


"""======== Null printArchive() ==========
Inputs: None
Returns: 
  Prints all the archived announcements
"""
def printArchive():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    q = """SELECT * FROM announcements"""
    res = c.execute(q)
    for r in res:
        print r
    
"""======== Array getAnnouncementByDate(required_date) ==========
Inputs: date -> Format "YYYY-MM-DD". Must have leading zeroes for date.
         ex. 2016-05-04 is the 4th of may, 2016
Returns: 
  All archived posts with that date stamp
"""
def getAnnouncementByDate(required_date):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    q = """SELECT * FROM announcements WHERE DATE(date) == DATE('%s');"""
    q = q%(required_date)
    res = c.execute(q)
    ans = []
    for r in c.execute(q):
        ans.append(r)
    return ans

go()    
#printArchive()
#getAnnouncementByDate("2016-05-18");
