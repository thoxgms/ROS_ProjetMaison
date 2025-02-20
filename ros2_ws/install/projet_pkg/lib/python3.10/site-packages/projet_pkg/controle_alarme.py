import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool


class Alarme_Subscriber(Node):

    def __init__(self):
        super().__init__('alarme_subscriber')

        self.subscription = self.create_subscription(
            Bool,
            '/capteur/bouton',
            self.subscribe_bouton,
            10)
        self.get_logger().info('Alarme Subscriber Node : OK')


    def subscribe_bouton(self, msg):
        if msg.data:  # Si BP pressé
            self.alarme_on()
        else:  # Si BP relâché
            self.alarme_off()


    def alarme_on(self):
            self.get_logger().info('Alarme : ON')


    def alarme_off(self):
            self.get_logger().info('Alarme : OFF')




def main(args=None):
    rclpy.init(args=args)
    alarme_subscriber = Alarme_Subscriber()
    rclpy.spin(alarme_subscriber)
    alarme_subscriber.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()

