from flask import Flask,render_template, session, request, redirect, url_for 
import backend
import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    year=str(datetime.date.today().year)
    month=str(datetime.date.today().month)
    displayDate=month+"/"
    if int(month)<10:
        month="0"+month
    day=str(datetime.date.today().day)
    displayDate=displayDate+day+"/"+year[2:]
    if int(day)<10:
        day="0"+day
    currentDate=year+"-"+month+"-"+day
    print currentDate
    #currentDate="2016-06-08"
    #displayDate="6/8/16"
    
    announcements=backend.getAnnouncementByDate(currentDate)
    return render_template(os.path.dirname(__file__)+"/"+"home.html",anonce=announcements,todayDate=displayDate)

@app.route("/submit",methods=["GET","POST"])
def submit():
    errors=[]
    if request.method == "POST":
        
        club1=request.form["club"]
        submitter1=request.form["submitter"]
        osis1=request.form["osis"]
        title1=request.form["title"]
        short_form1=request.form["short"]
        long_form1=request.form["long"]
        print "Before pull"
        dates=request.form["date"] 
        print dates

        if club1  == "Club/Team Name" or club1 is None:
            errors.append("No Club/Team name given")
            club1 = "Club/Team Name"
        if submitter1 == "Name" or submitter1 is None:
            errors.append("No name given for who is submitting this announcement")
            submitter1 = "Name"
        if osis1 == "9-Digit OSIS" or osis1 is None:
            errors.append("No OSIS given for who is submitting this announcement")
            osis1 = "9-Digit OSIS"
        if title1 == "Announcement title" or title1 is None:
            errors.append("No title given for this announcement")
            title1 = "Announcement title"
        elif len(osis1) != 9:
            errors.append("An OSIS must be 9 digits long")
        if short_form1=="Short form of your announcement. 200 characters maximum" or short_form1 is None:
            errors.append("No announcement given")
            short_form1="Short form of your announcement. 200 characters maximum"
        if long_form1 is None:
            long_form="Optional longer form of your announcement"
        if len(errors)>0:    
            return render_template("submit.html",error=errors,club=club1,submitter=submitter1,osis=osis1,title=title1,short_form=short1,long_form=long_form1)
        else:
            print "success"
            dates=dates.split(",")
            for date in dates:
                print date
                date=date.strip()
                split=date.split("/")
                currentDate=split[2]+"-"+split[0]+"-"+split[1]
                backend.addAnnouncement(club1,submitter1,osis1,title1,short_form1,long_form1,currentDate)
            return redirect("/")
    return render_template(os.path.dirname(__file__)+"/"+"submit.html",error=errors,club="Club/Team Name",submitter="Name",osis="9-Digit OSIS",title="Announcement title",short_form="Short form of your announcement. 200 characters maximum",long_form="Optional longer form of your announcement")

@app.route("/about")
def about():
    return render_template(os.path.dirname(__file__)+"/"+"about.html")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Don't store this on github"
    app.run(host="0.0.0.0", port=8002)
