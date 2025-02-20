import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
import random


class PresenceOut_Publisher(Node):

    def __init__(self):
        super().__init__('presence_Out_publisher')
        
        self.publisher_ = self.create_publisher(Bool, '/capteur/presence/exterieur', 10)
        timer_period = 5.0 # secondes
        self.timer = self.create_timer(timer_period, self.publisher_presence_Out)
        self.get_logger().info('Noeud PresenceOut Publisher : OK')


    def publisher_presence_Out(self):
        msg = Bool()
        msg.data = random.choice([True, False])  
        self.publisher_.publish(msg)
        self.get_logger().info(f'Exterieur : {msg.data}')
        # if msg.data :
        # 	state = "DETECTION" 
        # else :
        # 	state = "R.A.S"
        # self.get_logger().info(f'Exterieur : {state}')


def main(args=None):
    rclpy.init(args=args)
    presenceOut_publisher = PresenceOut_Publisher()
    rclpy.spin(presenceOut_publisher)
    presenceOut_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

