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

