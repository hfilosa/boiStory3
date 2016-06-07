# stuynounce

#Deployment Guide

##Introduction:
This guide is written with the intention of setting up the stuyvesant announcements page to run as a server. 
The server will use Nginx, Gunicorn, Flask, and SQLITE.
To follow this instruction manual the user will need SUDO privileges. 

##Preliminary Installations:
The following packages must be installed to proceed. Execute these commands in order
1. sudo apt-get update
2. sudo apt-get install python-pip python-dev nginx

##Setup a virtual eviroment:
1. virtualenv venv
2. source venv/bin/activate

##Pip Install:
1. pip install gunicorn flask

##Setup Nginx files:
1. Replace #path_to_repo in announcement_server with objective path to this repository
2. Place announcement_server file in /etc/nginx/sites-enabled/ & /etc/nginx/sites-available/
3. Test if nginx works with: sudo nginx -t
4. Restart nginx server: sudo service nginx restart

##A NOTE ON PORTS:
1. The server is configured to run on port 8002
2. If port 8002 is taken, simply change the port in announcement_server to a free port
3. After completing step 2, change the port number at the bottom of the app.py file

##Add domain to droplet networking
1. Add stuy.announce.ro as an A record for the droplet with the IP being the server

##Final run command
1. CD to the boistory3 folder
2. enter: gunicorn -D -p pidfile -b localhost:8000 app:app
3. The pidfile file holds the id of the process. Use this id to kill the server

If there are issues, consult this guide: 
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04
These procedures were based off of this.

###V0.1 Goals:
  * Mary: Frontend pages -> Submission page and frontpage. Use JS to make pages look nice 
  * Andrew: Flask routing. Set up system to determine date
  * Henry: SQLITE backend
