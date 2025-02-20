import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class AlarmeClient(Node):
    def __init__(self):
        super().__init__('alarme_client')
        self.client = self.create_client(SetBool, 'etat_alarme')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Attente du service etat_alarme...')

    def envoi_requete(self, state):
        requete = SetBool.Request()
        requete.data = state
        future = self.client.call_async(requete)
        rclpy.spin_until_future_complete(self, future)

        if future.result():
            print(f"Reponse service: {future.result().message}")
        else:
            print("Erreur !")

def main():
    rclpy.init()
    alarme_client = AlarmeClient()

    try:
        while True:
            cmd = input("ON : Activer alarme / OFF Desactiver alarme : ").strip().lower()
            if cmd == "ON":
                alarme_client.envoi_requete(True)
            elif cmd == "OFF":
                alarme_client.envoi_requete(False)
            else:
                print("Erreur !")
    except KeyboardInterrupt:
        pass

    alarme_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

