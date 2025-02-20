import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
import random


class Luminosity_Publisher(Node):

    def __init__(self):
        super().__init__('luminosity_publisher')
        
        self.publisher_ = self.create_publisher(Float32, '/capteur/luminosity', 10)
        timer_period = 5.0 # secondes
        self.timer = self.create_timer(timer_period, self.publisher_luminosity)
        self.get_logger().info('Noeud Luminosity Publisher : OK')


    def publisher_luminosity(self):
        msg = Float32()
        msg.data = round(random.uniform(0, 1000), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Luminosité : {msg.data} lux')




def main(args=None):
    rclpy.init(args=args)
    luminosity_publisher = Luminosity_Publisher()
    rclpy.spin(luminosity_publisher)
    luminosity_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

