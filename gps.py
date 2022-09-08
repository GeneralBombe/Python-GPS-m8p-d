##%%
a=0
a+=1
print(a)
##%%
from copyreg import constructor
from math import degrees
from queue import Empty
import serial
import logging
import time
import datetime as dt
import ipdb
from math import radians, cos, sin, asin, sqrt
##%%
#lmfao
logging.basicConfig(filename="log2.txt", level=logging.DEBUG)

class imu:
    def __init__(self, serialPort):
        self.serialPort = serialPort
    
    def serialOutput(self):
        output = ""
        if(self.serialPort.in_waiting > 0):
            output = self.serialPort.readline()
            output = output.decode('Ascii')

            print("op: " + output)

class ublox:
    def __init__(self, serialPort):
        self.serialPort = serialPort
        self.output = ""
        
        if(self.serialPort.in_waiting > 0):
            self.output = self.serialPort.readline()
            self.output = self.output.decode('Ascii')
    
    def serialReadLine(self):
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
            self.serialReadLine()
            if(self.output[0:6] == "$GNGLL"):
                #Example output: ['$GNGLL', '4805.45917', 'N', '01138.80482', 'E', '074351.00', 'A', 'A*79\r\n']
                liste = self.output.split(",")
                
                longitude = 0.0
                latitude = 0.0
                geo = [0.0, 0.0] #latitude / longitude
                latPositive = False
                longPositive = False
                if liste and liste[1]:
                    
                    if liste[2] == 'N':
                        latPositive = True
                    if liste[4] == 'E':
                        longPositive = True
                    
                    if latPositive == True:
                       # ipdb.set_trace()
                        buffer = (self.decimal_degrees(*self.dm(float(liste[1]))))
                       # geo[0] = format(buffer, ".8f")
                        geo[0] = buffer
                    else:
                        buffer = (self.decimal_degrees(*self.dm(float(liste[1])))) * -1 
                        geo[0] = format(buffer, ".8f")
                   # ipdb.set_trace()
                    if longPositive == True:
                        buffer = (self.decimal_degrees(*self.dm(float(liste[3]))))
                        #geo[1] = format(buffer, ".8f")
                        geo[1] = buffer

                    else:
                        buffer = (self.decimal_degrees(*self.dm(float(liste[3])))) * -1
                        #geo[1] = format(buffer, ".8f")
                        geo[1] = buffer
                    return geo
                else: 
                    geo = (-999, -999)
                    return geo
            else: 
                    geo = (-999, -999)
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
            
    


    def haversine(self, lon1, lat1, lon2, lat2):
        R = 6372.8 

        dLat = radians(float(lat2) - float(lat1))
        dLon = radians(float(lon2) - float(lon1))
        lat1 = radians(float(lat1))
        lat2 = radians(float(lat2))

        a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
        c = 2*asin(sqrt(a))

        return R * c
    
    def Speed(self):
        print("Drinn")
        retr = ""
        firstLoopTime = True
        firstTime = (1, 1, 1)
        finishTime = (1, 1, 1)
        firstGPS = (1, 2)
        lastGPS = (1, 2)
        running = True
        intervall = 3
        Location = (0, -999)
        looplastgps = (1, 1)
        while running: 

            self.serialReadLine()

            Location = self.gpscord()
            if Location[0] != -999:

                

                Zeit = self.getTime(2)

                
                if looplastgps != Location:
                    print(Zeit)
                    print(Location)

                looplastgps = Location


                
                h = Zeit[0]
                m = Zeit[1]
                s = Zeit[2]
                CurrentTime = dt.time(h, m, s)
                time_change = dt.timedelta(seconds=intervall)
                if firstLoopTime is True:
                    firstTime = CurrentTime
                    firstLoopTime = False
                    logging.debug("First TIme set: " + str(firstTime))
                    firstGPS = Location
                    
                
                else: 
                    finishTime = (dt.datetime.combine(dt.date(1,1,1),firstTime) + time_change).time()
                    if CurrentTime == finishTime:
                        lastGPS = Location
                        break

                Location = (-999, -999)
            
        Kmh = format(self.haversine(firstGPS[0], firstGPS[1], lastGPS[0], lastGPS[1]) / intervall, ".5f")

        retr = ("Location 1: " + str(firstGPS) + " Location 2: " + str(lastGPS) + "\nZeit 1:     " + str(firstTime)+ " Zeit 2:     " + str(finishTime) + 

        #Speed Calculation

        "\nDistance: " +  format((self.haversine(firstGPS[0], firstGPS[1], lastGPS[0], lastGPS[1])), ".5f") + 
        "\nKmh: " + str(Kmh))
        return retr

serPort = serial.Serial(port = "/dev/ttyACM0", baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serPort2 = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1,
                       xonxoff=False, rtscts=False, dsrdtr=True)

#Objekt = ublox(serPort)
#buffer = Objekt.Speed()

while True:
    Objekt2 = imu(serPort2)
    Objekt2.serialOutput()
    


   


