import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool, Float32


class Temperature_Subscriber(Node):

    def __init__(self):
        super().__init__('temperature_subscripber')

        self.subscription = self.create_subscription(
            Float32,
            '/capteur/temperature',
            self.subscriber_temperature,
            10)
        self.get_logger().info('Noeud Temperature Subscriber : OK')


    def subscriber_temperature(self, msg):
        self.get_logger().info('Résultat temperature : "%s"' % msg.data)

    #     self.temperature_min = 18.0
    #     self.temperature_max = 25.0
    
    #     if msg.data < self.temperature_min:
    #         self.chauffage_on()
    #     elif msg.data > self.temperature_max:
    #         self.chauffage_off()

    # def chauffage_on(self):
    #         self.get_logger().info('CHAUFFAGE : ON')

    # def chauffage_off(self):
    #         self.get_logger().info('CHAUFFAGE : OFF')




def main(args=None):
    rclpy.init(args=args)
    temperature_subscripber = Temperature_Subscriber()
    rclpy.spin(temperature_subscripber)
    temperature_subscripber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

