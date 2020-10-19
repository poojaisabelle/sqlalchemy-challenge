import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup 
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the two tables 
Base.prepare(engine, reflect=True)

# Save reference to measurement and station
measurement = Base.classes.measurement
station = Base.classes.station 

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    return (
        f"Aloha! Welcome to the Honolulu, Hawai'i Climate Analysis Directory.<br/>"
        f"You can explore the following climate analysis : <br/>"
        f"1. Precipitation for the last 12 months: /api/v1.0/precipitation<br/>"
        f"2. List of all stations: /api/v1.0/stations<br/>"
        f"3. Temperature observations of the most active station for the last year of data: /api/v1.0/tobs<br/>"
    )

