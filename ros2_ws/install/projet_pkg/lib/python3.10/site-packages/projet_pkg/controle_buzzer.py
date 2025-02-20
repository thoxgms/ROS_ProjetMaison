import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool


class Buzzer_Subscriber(Node):

    def __init__(self):
        super().__init__('buzzer_subscriber')
        
        self.presence_int_sub = self.create_subscription(
            Bool,
            '/capteur/presence/interieur',
            self.subcribe_presenceInt,
            10)
        self.get_logger().info('Buzzer Subscriber Node : OK')
        

    def subcribe_presenceInt(self, msg):
            if msg.data:
                self.buzzer_on()
            else: 
                self.buzzer_off()


    def buzzer_on(self):
            self.get_logger().info('Buzzer : ON')


    def buzzer_off(self):
            self.get_logger().info('Buzzer : OFF')




def main(args=None):
    rclpy.init(args=args)
    buzzer_subscriber = Buzzer_Subscriber()
    rclpy.spin(buzzer_subscriber)
    buzzer_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

