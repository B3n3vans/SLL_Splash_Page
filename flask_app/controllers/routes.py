from datetime import datetime, timedelta
import json
from flask_app import app,render_template,bcrypt,redirect,request,session,flash
from flask import get_flashed_messages
from flask import after_this_request
from pytz import timezone
from flask import after_this_request
# from StudentLoanLotto.flask_app.models.draw import Draw

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import os
from PIL import Image
from flask import after_this_request
import time
from threading import Thread

######### Global Variables ############
# Global dictionary to track last activity for each user
user_activity = {}
######### Routes ############
### This route is the home route
### This page will be our landing page before the user logs in or signs  up for an account
### If the user is already logged in, it will redirect the user to the dashboard



@app.route('/')
def landing_page():
    return prelaunch_splash_page()

@app.route('/prelaunch_splash_page')
def prelaunch_splash_page(): 
    return render_template('prelaunch_splash_page.html')



