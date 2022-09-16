import rclpy
import gps
from rclpy.node import Node

from std_msgs.msg import String
from gps_msgs.msg import GPSFix

import ipdb


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(GPSFix, 'ublox_gps_fix', 10)  # CHANGE
        timer_period = 0.001
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0.0
        self.gps_objekt = gps.ublox()
        self.first = True
        self.msg = GPSFix()

    
    
    def timer_callback(self):
        if(self.serialPort.in_waiting > 0):
            self.gps_objekt.serialReadLine()
            op = self.gps_objekt.output
            if op.contains("GNGLL"):
                if self.first is False:
                    self.get_logger().info('Speed: "%s ", Cord: "%s  %s"'% (speed, self.msg._latitude, self.msg._longitude))
                    self.publisher_.publish(self.msg)     
                else:
                    self.first = True
                gpsd = self.gps_objekt.gpscord()
                self.msg.longitude = gpsd[0]
                self.msg.latitude = gpsd[1]
                time = self.gps_objekt.getTime(2)
                seperator = ''
                self.msg.time = float(seperator.join(time))   
            if op.contains("GPGSV"):
                speed = self.gps_objekt.speedParseGNVTG()
                self.msg.speed = speed
                
                
        
            
        '''
        while(self.gps_objekt.serialReadLine()):
            msg = GPSFix()       
            msg.header.stamp = self.get_clock().now().to_msg()
            speed = self.gps_objekt.speedParseGNVTG()
            if speed is not None:
                msg.speed = float(speed)
                self.get_logger().info('Publishing Speed: "%s"' % (speed))
                #out=self.gps_objekt.serialReadLine()
                #print(out)
                   
            time = self.gps_objekt.getTime(2)
            print(time)
            if time is not None:
                self.get_logger()
                #msg = String()
                seperator = ''
                msg.time = float((seperator.join(time)))            
                #self.publisher_.publish(msg)

            cord = self.gps_objekt.gpscord() #latitude / longitude
            print(cord)
            if cord[0] != -999 and self.first is True:                                           # CHANGE
                self.first = False
     
                msg.latitude = float(cord[0])                                       # CHANGE
                msg.longitude = float(cord[1])  
                self.get_logger().info('Publishing : "%s", "%s"' % (msg.latitude, msg.longitude))
            
            if cord[0] == -999 and self.first is False:
                self.first = True
            
            self.publisher_.publish(msg)     

        '''
        
def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
