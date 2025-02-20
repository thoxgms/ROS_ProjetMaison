import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
import random


class PresenceInt_Publisher(Node):

    def __init__(self):
        super().__init__('presence_Int_publisher')
        
        self.publisher_ = self.create_publisher(Bool, '/capteur/presence/interieur', 10)
        timer_period = 5.0 # secondes
        self.timer = self.create_timer(timer_period, self.publisher_presence_Int)
        self.get_logger().info('Noeud PresenceInt Publisher : OK')


    def publisher_presence_Int(self):
        msg = Bool()
        msg.data = random.choice([True, False])  
        self.publisher_.publish(msg)
        self.get_logger().info(f'Intérieur : {msg.data}')
        # if msg.data :
        # 	state = "DETECTION" 
        # else :
        # 	state = "R.A.S"
        # self.get_logger().info(f'Intérieur : {state}')




def main(args=None):
    rclpy.init(args=args)
    presenceInt_publisher = PresenceInt_Publisher()
    rclpy.spin(presenceInt_publisher)
    presenceInt_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

