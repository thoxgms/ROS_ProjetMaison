import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool


class PresenceOut_Subscriber(Node):

    def __init__(self):
        super().__init__('presenceOut_subscriber')
        
        self.subscription = self.create_subscription(
            Bool,
            '/capteur/presence/exterieur',
            self.subcriber_presenceOut,
            10)
        self.get_logger().info('Noeud presenceOut Subscriber : OK')
        

    def subcriber_presenceOut(self, msg):
            self.get_logger().info('Résultat presenceOut : "%s"' % msg.data)

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
    presenceOut_subscriber = PresenceOut_Subscriber()
    rclpy.spin(presenceOut_subscriber)
    presenceOut_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

