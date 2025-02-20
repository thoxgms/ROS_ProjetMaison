import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Volet_Subscriber(Node):

    def __init__(self):
        super().__init__('time_subscribeur')

        self.subscription = self.create_subscription(
            String,
            '/capteur/time',
            self.subscriber_time,
            10)
        self.get_logger().info('Noeud Time Subscriber : OK')


    def subscriber_time(self, msg):
        self.get_logger().info('Résultat time : "%s"' % msg.data)

    #     self.open_time = "7:00"
    #     self.close_time = "20:00"
        
    #     if msg.data == self.open_time:
    #         self.volet_on()
    #     elif msg.data == self.close_time:
    #         self.volet_off()    

    # def volet_on(self):
    #         self.get_logger().info('Volet : OUVERT')
            
    # def volet_off(self):
    #         self.get_logger().info('Volet : FERME')




def main(args=None):
    rclpy.init(args=args)
    volet_subscribeur = Volet_Subscriber()
    rclpy.spin(volet_subscribeur)
    volet_subscribeur.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

