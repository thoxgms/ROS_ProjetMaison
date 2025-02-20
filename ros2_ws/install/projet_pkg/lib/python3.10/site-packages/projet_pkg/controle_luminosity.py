import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool, Float32


class Luminosity_Subscriber(Node):

    def __init__(self):
        super().__init__('luminosity_subscribeur')

        self.subscription = self.create_subscription(
            Float32,
            '/capteur/luminosity',
            self.subscriber_luminosity,
            10)
        self.get_logger().info('Noeud Luminosity Control : OK')


    def subscriber_luminosity(self, msg):
        self.get_logger().info('Résultat luminosité : "%s"' % msg.data)

    #     self.luminosite_min = 0.0
    #     self.luminosite_max = 1000.0
    
    #     if msg.data < self.luminosite_min:
    #         self.lumiere_on()
    #     elif msg.data > self.luminosite_max:
    #         self.lumiere_off()

    # def lumiere_on(self):
    #         self.get_logger().info('LUMIERE : ON')

    # def lumiere_off(self):
    #         self.get_logger().info('LUMIERE : OFF')




def main(args=None):
    rclpy.init(args=args)
    luminosity_subscribeur = Luminosity_Subscriber()
    rclpy.spin(luminosity_subscribeur)
    luminosity_subscribeur.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

