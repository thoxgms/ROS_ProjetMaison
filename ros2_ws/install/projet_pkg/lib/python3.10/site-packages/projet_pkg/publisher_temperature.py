import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
import random


class Temperature_Publisher(Node):

    def __init__(self):
        super().__init__('temperature_publisher')
        
        self.publisher_ = self.create_publisher(Float32, '/capteur/temperature', 10)
        timer_period = 5.0 # secondes
        self.timer = self.create_timer(timer_period, self.publisher_temperature)
        self.get_logger().info('Noeud Temperature Publisher : OK')


    def publisher_temperature(self):
        msg = Float32()
        msg.data = round(random.uniform(-10.0, 45.0), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Temperature : {msg.data} °C')




def main(args=None):
    rclpy.init(args=args)
    temperature_publisher = Temperature_Publisher()
    rclpy.spin(temperature_publisher)
    temperature_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

