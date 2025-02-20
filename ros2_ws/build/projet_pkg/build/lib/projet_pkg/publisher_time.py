import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from datetime import datetime
import random

class Time_Publisher(Node):

    def __init__(self):
        super().__init__('time_publisher')
        
        self.publisher_ = self.create_publisher(String, '/capteur/time', 10)
        timer_period = 5.0 # secondes
        self.timer = self.create_timer(timer_period, self.publisher_time)
        self.get_logger().info('Noeud Time Publisher : OK')
        
        
    def publisher_time(self):
        #temps = datetime.now().strftime('%H:%M')  
        
        H = random.randint(0, 24)
        M = random.randint(0, 60)
        temps = str(H) + ":" + str(M)
        
        #temps = datetime.now().strftime('7:00')  
        
        msg = String()
        msg.data = temps
        self.publisher_.publish(msg)
        self.get_logger().info(f'Horaire : {temps}')


def main(args=None):
    rclpy.init(args=args)
    time_publisher = Time_Publisher()
    rclpy.spin(time_publisher)

    time_publisher.destroy_node()
    rclpy.shutdown()
        

if __name__ == '__main__':
    main()

