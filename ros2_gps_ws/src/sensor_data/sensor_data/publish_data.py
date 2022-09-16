#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
import gps

class PublishDataNode(Node):
    def __init__(self):
        super().__init__("publish_data")
        
        self.get_logger().info("Publishing Started.")



def main(args=None):
    rclpy.init(args=args)
    rclpy.shutdown()



