#!/usr/bin/env python
import time 
from pyrebase import pyrebase
from SensorManager import *
from datetime import datetime


config = {
  "apiKey": "AIzaSyCqc_mKfuEhivguaieQ3xbFTeiuB3lZtxk",
  "authDomain": "guard-28a03.firebaseapp.com",
  "databaseURL": "https://guard-28a03-default-rtdb.firebaseio.com",
  "storageBucket": "guard-28a03.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def getReadingToAPI():
    
    temperature = str(getTemperature())
    pressure = str(getPressure())
    humidity = str(getHumidity())
    gas = str(getGas())
    lux = str(getlight())
    prox = str(getProximity())
    magnetometer = str(getMagnetometer())
    accelerometer = str(getAaccelerometer())
    rgbc = str(getColour())
 
    return temperature,pressure,humidity,gas, lux, prox, magnetometer, accelerometer, rgbc


if __name__=="__main__":
    
    while True:
        temperature,pressure,humidity,gas, lux, prox, magnetometer, accelerometer, rgbc  = getReadingToAPI()
        now = datetime.now()

        if temperature == '-1' or lux =='-1' or pressure == '-1' or humidity == '-1' or gas == '-1' or prox == '-1' or magnetometer == '-1' or accelerometer == '-1':
            time.sleep(120)
            continue
        else:
            BME680_data = {"Temperature":temperature, "Pressure":pressure , "Humidity": humidity, "Gas":gas, "time":str(now)}     
            db.child("BME680").push(BME680_data)
            print(BME680_data)

            LTR_559_data={"light":lux , "Proximity":prox , "time":str(now) }
            db.child("LTR_559").push(LTR_559_data)
            print(LTR_559_data)

            LSM303D_data={"Magnetometer": magnetometer, "Accelerometer":accelerometer , "time":str(now) }
            db.child("LSM303D").push(LSM303D_data)
            print(LSM303D_data)

            BH1745_data={"RGBC": rgbc, "time":str(now) }
            db.child("BH1745").push(BH1745_data)
            print(BH1745_data)

            time.sleep(120)
  


    
    



