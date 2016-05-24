from flask import Flask,render_template, session, request, redirect, url_for 
import backend
import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    year=str(datetime.date.today().year)
    month=str(datetime.date.today().month)
    if month<10:
        month="0"+month
    day=str(datetime.date.today().day)
    if day<10:
        day="0"+day
    currentDate=year+"-"+month+"-"+day
    displayDate=month+"/"+day+"/"+year
    announcements=backend.getAnnouncementByDate(currentDate)
    return render_template("home.html",a=announcements,todayDate=displayDate)

@app.route("/submit",methods=["GET","POST"])
def submit():
    errors=[]
    if request.method == "POST":
        
        club1=request.form["club"]
        submitter1=request.form["submitter"]
        osis1=request.form["osis"]
        short1=request.form["short"]
        long_form1=request.form["long"]

        if club1  == "Club/Team Name" or club1 is None:
            errors.append("No Club/Team name given")
            club1 = "Club/Team Name"
        if submitter1 == "Name" or submitter1 is None:
            errors.append("No name given for who is submitting this announcement")
            submitter1 = "Name"
        if osis1 == "9-Digit OSIS" or osis1 is None:
            errors.append("No OSIS given for who is submitting this announcement")
            osis1 = "9-Digit OSIS"
        elif len(osis) != 9:
            errors.append("An OSIS must be 9 digits long")
        if short1=="Short form of your announcement. 200 characters maximum" or short1 is None:
            errors.append("No announcement given")
            short1="Short form of your announcement. 200 characters maximum"
        if long_form1 is None:
            long_form="Optional longer form of your announcement"
        if len(errors)>0:    
            return render_template("submit.html",error=errors,club=club1,submitter=submitter1,osis=osis1,short_form=short1,long_form=long_form1)
        else:
            year=str(datetime.date.today().year)
            month=str(datetime.date.today().month)
            if month<10:
                month="0"+month
            day=str(datetime.date.today().day)
            if day<10:
                day="0"+day
            currentDate=year+"-"+month+"-"+day
            backend.addAnnouncement(club1,submitter1,osis1,title1,short_form1,long_form1,currentDate);
            return redirect("/");
    return render_template("submit.html",error=errors,club="Club/Team Name",submitter="Name",osis="9-Digit OSIS",short_form="Short form of your announcement. 200 characters maximum",long_form="Optional longer form of your announcement")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Don't store this on github"
    app.run(host="0.0.0.0", port=8000)
