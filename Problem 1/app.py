
from flask import Flask, render_template
from datetime import datetime
import calendar

    
app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now() # current date and time
    date_time = now.strftime("%B %d %Y %H:%M:%S")
    return render_template('index.html', date_time= calendar.day_name[now.weekday()] + ', ' +date_time)