##%%
a=0
a+=1
print(a)
##%%
from copyreg import constructor
from math import degrees
from queue import Empty
from turtle import speed
from types import NoneType
import serial
import logging
import time
import datetime as dt
import ipdb
from math import radians, cos, sin, asin, sqrt
##%%
serPort = serial.Serial(port = "ttyS0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

class ublox:
    def __init__(self, serialPort):
        self.serialPort = serialPort
        self.output = ""
        
        if(self.serialPort.in_waiting > 0):
            self.output = self.serialPort.readline()
            self.output = self.output.decode('Ascii')
    
    def dm(self, x):
        degrees = int(x) // 100
        minutes = x - 100*degrees

        return degrees, minutes

    def decimal_degrees(self, degrees, minutes):
        return degrees + minutes/60 
                
        
    def getTime(self, utcplus):
        
           
            if(self.output[0:6] == "$GNGLL"):
                #Example output: ['$GNGLL', '4805.45917', 'N', '01138.80482', 'E', '074351.00', 'A', 'A*79\r\n']
                liste = self.output.split(",")
                Zeit = liste[5]
                if Zeit:
                    Stunde = int(Zeit[0:2]) + utcplus
                    Minute = int(Zeit[2:4])
                    Sekunde = int(Zeit[4:6])
                    rueck = (Stunde % 24), (Minute), (Sekunde)
                    return rueck
            
        
    
    def gpscord(self): 
        
            if(self.output[0:6] == "$GNGLL"):
                #Example output: ['$GNGLL', '4805.45917', 'N', '01138.80482', 'E', '074351.00', 'A', 'A*79\r\n']
                liste = self.output.split(",")
                
                longitude = 0.0
                latitude = 0.0
                geo = [0.0, 0.0] #latitude / longitude
                latPositive = False
                longPositive = False
                if liste[1]:
                    
                    if liste[2] == 'N':
                        latPositive = True
                    if liste[4] == 'E':
                        longPositive = True
                    
                    if latPositive == True:
                       # ipdb.set_trace()
                        buffer = (self.decimal_degrees(*self.dm(float(liste[1]))))
                        geo[0] = format(buffer, ".5f")
                    else:
                        buffer = (self.decimal_degrees(*self.dm(float(liste[1])))) * -1 
                        geo[0] = format(buffer, ".5f")
                   # ipdb.set_trace()
                    if longPositive == True:
                        buffer = (self.decimal_degrees(*self.dm(float(liste[3]))))
                        geo[1] = format(buffer, ".5f")
                    else:
                        buffer = (self.decimal_degrees(*self.dm(float(liste[3])))) * -1
                        geo[1] = format(buffer, ".5f")
                        
                    return geo
                    
    
    
    def serialOutput(self):
        output = ""
        if(self.serialPort.in_waiting > 0):
            output = self.serialPort.readline()
            output = output.decode('Ascii')
            
            if(output[0]== "$"):
                #Example output: ['$GNGLL', '4805.45917', 'N', '01138.80482', 'E', '074351.00', 'A', 'A*79\r\n']
                liste = output.split(",")
                return liste
            
    


def haversine(lon1, lat1, lon2, lat2):
    R = 6372.8 

    dLat = radians(float(lat2) - float(lat1))
    dLon = radians(float(lon2) - float(lon1))
    lat1 = radians(float(lat1))
    lat2 = radians(float(lat2))

    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))

    return R * c

     
speed = ublox(serPort)  
firstLoopTime = True
firstTime = (1, 1, 1)
finishTime = (1, 1, 1)
firstGPS = (1, 2)
lastGPS = (1, 2)
'''
while True:
    objekt = ublox(serPort)
    t = objekt.getTime(2)
    gps = objekt.gpscord()
    if t is not None:
        print(t)
        print(gps)
'''



while True: 
    
    objekt = ublox(serPort) 
    
    Zeit = objekt.getTime(2)
    Location = objekt.gpscord()
    
    if Zeit is not None:
        Zeit = objekt.getTime(2)
        print(Zeit)
        print(Location)
        CurrentTime = dt.time(Zeit[0], Zeit[1], Zeit[2])
        time_change = dt.timedelta(seconds=5)
        if firstLoopTime is True:
            firstTime = CurrentTime
            firstLoopTime = False
            print("First TIme set: " + str(firstTime))
            firstGPS = Location
        else: 
            finishTime = (dt.datetime.combine(dt.date(1,1,1),firstTime) + time_change).time()
            if CurrentTime == finishTime:
                print("5 Sekunden Vorbei")
                lastGPS = Location
                break

print("Location 1: " + str(firstGPS) + " Location 2: " + str(lastGPS))
print("Zeit 1:     " + str(firstTime)+ " Zeit 2:     " + str(finishTime))

#Speed Calculation

print("Distance: " +  str(haversine(firstGPS[0], firstGPS[1], lastGPS[0], lastGPS[1])))
Kmh = haversine(firstGPS[0], firstGPS[1], lastGPS[0], lastGPS[1]) / 5
print("Kmh: " + str(Kmh))