import rclpy
import gps
from rclpy.node import Node

from std_msgs.msg import String
from gps_msgs.msg import GPSFix




class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(GPSFix, 'topic', 10)  # CHANGE
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0.0
        self.gps_objekt = gps.ublox()
        self.first = True

    def timer_callback(self):
        self.gps_objekt.serialReadLine()

        cord = self.gps_objekt.gpscord() #latitude / longitude
        if cord[0] != -999 and self.first is True:                                           # CHANGE
            self.first = False
            msg = GPSFix()        
            msg.latitude = float(cord[0])                                       # CHANGE
            msg.longitude = float(cord[1])                                           # CHANGE
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing : "%s", "%s"' % (msg.latitude, msg.longitude))
        if cord[0] == -999 and self.first is False:
            self.first = True


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
