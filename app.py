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

@app.route("/api/v1.0/precipitation")
def precipitation():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return precipitation data from the last year"""

    # Perform a query to retrieve the data and precipitation scores
    sel = [measurement.date, measurement.prcp]

    prcp_last_year = session.query(*sel).filter(measurement.date < '2017-08-23').filter(measurement.date >= '2016-08-23').order_by(measurement.date).all()

    session.close()

    # Convert into a list 
    prcp_data = dict(prcp_last_year)

    return jsonify(prcp_data)

@app.route("/api/v1.0/stations")
def stations():
    
    # Create our session (;ink) from Python to DB 
    session = Session(engine)

    """Return all station data"""

    # Perform a query to retrieve all stations 
    all_stations = session.query(station.station, station.name).all()

    session.close()

    # Convert this data into a list 
    stn_list = list(np.ravel(all_stations))

    return jsonify(stn_list)



@app.route("/api/v1.0/tobs")
def tobs():
    
    # Create our session (;ink) from Python to DB 
    session = Session(engine)

    """Return temperature observations for most active station in the last year"""

    # Perform a query to retrieve data
    temp_active_stn = session.query(measurement.date, measurement.tobs).filter(measurement.station == "USC00519281").filter(measurement.date >= '2016-08-23').all()

    session.close()

    # Convert this data into a list 
    temp_data = dict(temp_active_stn)

    return jsonify(temp_data)



if __name__ == '__main__':
    app.run(debug = True)