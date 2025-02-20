import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
import random


class Bouton_Publisher(Node):

    def __init__(self):
        super().__init__('bouton_publisher')
        
        self.publisher_ = self.create_publisher(Bool, '/capteur/bouton', 10)
        timer_period = 2.0 # seconds
        self.timer = self.create_timer(timer_period, self.publish_bouton)
        self.get_logger().info('Bouton Publisher Node : OK')


    def publish_bouton(self):
        msg = Bool()
        msg.data = random.choice([True, False])  
        self.publisher_.publish(msg)
        if msg.data :
        	state = "BP ON" 
        else :
        	state = "BP OFF"
        self.get_logger().info(f'Bouton state : {state}')




def main(args=None):
    rclpy.init(args=args)
    bouton_publisher_node = Bouton_Publisher()
    rclpy.spin(bouton_publisher_node)
    bouton_publisher_node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()

