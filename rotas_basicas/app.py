from turtle import right
from flask import Flask
from os import getenv
from datetime import datetime

app = Flask(__name__)

@app.get('/')
def Home(): 
    return {"data": "Hello Flask!"}


@app.get('/current_datetime')
def current_datetime():

    time_right_now = int(datetime.now().strftime('%H'))
    message = ""

    if time_right_now < 12:
        message = "Bom dia!"
    elif time_right_now <18:
        message = "Boa tarde!"
    else:
        message = "Boa noite!"
    
    year = (f"{datetime.now().strftime('%d')}/{datetime.now().strftime('%m')}/{datetime.now().strftime('%Y')}")    
    hour = (f"{datetime.now().strftime('%I')}{str(datetime.now().time())[2:8]} {datetime.now().strftime('%p')}")
    
    final=(f'{year} {hour}')
    return {"current_datetime": final,
    "message": message}