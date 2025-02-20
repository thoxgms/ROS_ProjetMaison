from flask import Flask, render_template
from flask_socketio import SocketIO
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool, String
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Stocker les valeurs des capteurs
capteur_data = {
    "temperature": 0.0,
    "luminosity": 0.0,
    "presence_exterieur": False,
    "presence_interieur": False
}

class capteurSubscriber(Node):
    def __init__(self):
        super().__init__('capteur_subscriber')

        # Souscription aux différents topics ROS 2
        self.create_subscription(Float32, '/capteur/temperature', self.temperature_callback, 10)
        self.create_subscription(Float32, '/capteur/luminosity', self.luminosity_callback, 10)
        self.create_subscription(Bool, '/capteur/presence/interieur', self.presence_exterieur_callback, 10)
        self.create_subscription(Bool, '/capteur/presence/exterieur', self.presence_interieur_callback, 10)
        self.create_subscription(String, '/capteur/time', self.time_callback, 10)
        self.create_subscription(Bool, '/capteur/bouton', self.bouton_callback, 10)

    def temperature_callback(self, msg):
        capteur_data["temperature"] = msg.data
        socketio.emit('update_data', capteur_data)

    def luminosity_callback(self, msg):
        capteur_data["luminosity"] = msg.data
        socketio.emit('update_data', capteur_data)

    def presence_exterieur_callback(self, msg):
        capteur_data["presence_exterieur"] = msg.data
        socketio.emit('update_data', capteur_data)

    def presence_interieur_callback(self, msg):
        capteur_data["presence_interieur"] = msg.data
        socketio.emit('update_data', capteur_data)
        
    def time_callback(self, msg):
        capteur_data["time"] = msg.data
        socketio.emit('update_data', capteur_data)
        
    def bouton_callback(self, msg):
        capteur_data["bouton"] = msg.data
        socketio.emit('update_data', capteur_data)

# Fonction pour exécuter ROS 2 en parallèle
def ros2_thread():
    rclpy.init()
    node = capteurSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Lancer ROS 2 dans un thread séparé
    threading.Thread(target=ros2_thread, daemon=True).start()
    
    # Lancer Flask avec WebSockets
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

