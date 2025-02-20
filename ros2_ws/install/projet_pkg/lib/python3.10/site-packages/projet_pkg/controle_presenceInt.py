import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool


class PresenceInt_Subscriber(Node):

    def __init__(self):
        super().__init__('presenceInt_subscriber')
        
        self.subscription = self.create_subscription(
            Bool,
            '/capteur/presence/interieur',
            self.subcriber_presenceInt,
            10)
        self.get_logger().info('Noeud presenceInt Subscriber : OK')
        

    def subcriber_presenceInt(self, msg):
            self.get_logger().info('Résultat presenceInt : "%s"' % msg.data)

    #         if msg.data:
    #             self.buzzer_on()
    #         else: 
    #             self.buzzer_off()

    # def buzzer_on(self):
    #         self.get_logger().info('Buzzer : ON')

    # def buzzer_off(self):
    #         self.get_logger().info('Buzzer : OFF')




def main(args=None):
    rclpy.init(args=args)
    presenceInt_subscriber = PresenceInt_Subscriber()
    rclpy.spin(presenceInt_subscriber)
    presenceInt_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

