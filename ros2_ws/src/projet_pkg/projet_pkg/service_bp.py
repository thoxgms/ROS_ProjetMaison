import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class Alarme_Service(Node):

    def __init__(self):
        super().__init__('alarme_service')
        self.srv = self.create_service(SetBool, 'etat_alarme', self.data_etat_alarme)
        self.etat_alarme = False
        self.get_logger().info('Service BP alarme : OK')


    def daata_etat_alarme(self, requete, reponse):
        if requete.data == self.etat_alarme:
            reponse.etat = False
            reponse.message = "Alarme deja dans cet état"
        else:
            self.etat_alarme = requete.data
            reponse.etat = True
            if self.etat_alarme :
                reponse.message = "ALARME ON" 
            else :
                reponse.message = "ALARME OFF"

        self.get_logger().info(reponse.message)
        return reponse


def main():
    rclpy.init()
    alarme_service = Alarme_Service()
    rclpy.spin(alarme_service)
    alarme_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

