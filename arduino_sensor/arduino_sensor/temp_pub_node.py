# !/usr/bin/env/ python3

from sensor_msgs.msg import Temperature
import rclpy
from rclpy.node import Node
from .temperature import ArduinoTemperature

class tempPublisher(Node):
    def __init__(self):
        super().__init__("temp_pub_node")
        self.publisher = self.create_publisher(Temperature, "/sensor_temp", 10)
        timer_period = 0.5 #seconds
        self.timer = self.create_timer(timer_period, self.publish_callback)
        self.get_logger().info(
             'Temperature node Started, get Temperature data from dht11 sensor \n'
        )
        self.ardTemp = ArduinoTemperature()

    def publish_callback(self):
        temp_msg = Temperature()
        temp_msg.temperature = self.ardTemp.getTemperature()
        self.publisher.publish(temp_msg)
    
def main(args=None):
    rclpy.init(args=args)

    temp_publisher = tempPublisher()
    rclpy.spin(temp_publisher)

    temp_publisher.get_logger().info('\n====Stop Publishing====')
    temp_publisher.destroy_node()
    rclpy.shutdown()

