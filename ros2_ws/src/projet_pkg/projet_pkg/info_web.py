import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32, Bool, String
from std_srvs.srv import SetBool

from flask import Flask, render_template
from flask_socketio import SocketIO
import threading


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

capteur_data = {
    "temperature": 0.0,
    "luminosite": 0.0,
    "presence_exterieur": False,
    "presence_interieur": False,
    "alarme": "OFF",
    "chauffage": "OFF",
    "lumiere": "OFF",
    "volet": "FERME",
    "time": "00:00"
}

class Capteur_Subscriber(Node):
    def __init__(self):
        super().__init__('capteur_subscriber')
        self.create_subscription(Float32, '/capteur/temperature', self.subscriber_temperature, 10)
        self.create_subscription(Float32, '/capteur/luminosity', self.subscriber_luminosity, 10)
        self.create_subscription(Bool, '/capteur/presence/interieur', self.subscriber_presence_interieur, 10)
        self.create_subscription(Bool, '/capteur/presence/exterieur', self.subscriber_presence_exterieur, 10)
        self.create_subscription(String, '/capteur/time', self.subscriber_time, 10)

    def subscriber_temperature(self, msg):
        if capteur_data["alarme"] == "OFF":
            capteur_data["temperature"] = msg.data
            if msg.data < 18.0 :
                capteur_data["chauffage"] = "ON"
            else :
                capteur_data["chauffage"] = "OFF"
            socketio.emit('etat_data', capteur_data)

    def subscriber_luminosity(self, msg):
        if capteur_data["alarme"] == "OFF":
            capteur_data["luminosite"] = msg.data
            if msg.data < 400.0 :
                capteur_data["lumiere"] = "ON" 
            else :
                capteur_data["lumiere"] = "OFF"
            socketio.emit('etat_data', capteur_data)

    def subscriber_presence_interieur(self, msg):
        if capteur_data["alarme"] == "ON":
            capteur_data["presence_interieur"] = msg.data
            if msg.data or capteur_data["presence_exterieur"] :
                capteur_data["buzzer"] = "ON"
            else :
                capteur_data["buzzer"] = "OFF"
            socketio.emit('etat_data', capteur_data)

    def subscriber_presence_exterieur(self, msg):
        if capteur_data["alarme"] == "ON":
            capteur_data["presence_exterieur"] = msg.data
            if msg.data or capteur_data["presence_interieur"] :
                capteur_data["buzzer"] = "ON" 
            else :
                capteur_data["buzzer"] = "OFF"
            socketio.emit('etat_data', capteur_data)

    def subscriber_time(self, msg):
        if capteur_data["alarme"] == "OFF":
            capteur_data["time"] = msg.data
            if msg.data > "07:00" and msg.data < "19:00" :
                capteur_data["volet"] = "OUVERT" 
            else :
                capteur_data["volet"] = "FERME"
            socketio.emit('etat_data', capteur_data)


class Alarme_Client(Node):
    def __init__(self):
        super().__init__('alarme_client')
        self.client = self.create_client(SetBool, 'etat_alarme')

    def envoi_requete(self, state):
        requete = SetBool.Request()
        requete.data = state
        future = self.client.call_async(requete)
    
        execution = rclpy.executors.SingleThreadedExecutor()
        execution.add_node(self)
        execution.spin_until_future_complete(future)
        execution.shutdown()

        if future.result():
            if state :
                capteur_data["alarme"] = "ON" 
            else :
                capteur_data["alarme"] = "OFF"
            socketio.emit('update_alarme', {'alarme': capteur_data["alarme"]})


@socketio.on('etat_alarme')
def etat_alarme(data):
    etat = capteur_data["alarme"]
    if etat == "ON" :
        new_etat = "OFF" 
    else :
        new_etat = "ON"
    alarme_client.envoi_requete(new_etat == "ON") 


@app.route('/')
def index():
    return render_template('index.html')


def thread():
    global alarme_client
    rclpy.init()
    alarme_client = Alarme_Client()
    capteur_subscriber = Capteur_Subscriber()
    rclpy.spin(capteur_subscriber)
    capteur_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    threading.Thread(target=thread, daemon=True).start()
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)

