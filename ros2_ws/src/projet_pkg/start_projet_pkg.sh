#!/bin/bash


echo "START PROJET_PKG"
pkill -f ros2

echo "Configuration ROS2 avant lancement projet ? (Y/N) : "
read -r user_input

if [[ "$user_input" == "Y" || "$user_input" == "y" ]]; then
    echo "Configuration ROS 2..."
    cd ~/ros2_ws
    colcon build
    source install/setup.bash
    echo "ROS2 configuré !"
fi

mkdir src/projet_pkg/log

echo ">> Start Projet ROS <<"

echo "[projet_pkg] > Start : publisher_temperature"
ros2 run projet_pkg publisher_temperature > src/projet_pkg/log/log_publisher_temperature.txt 2>&1 &

echo "[projet_pkg] > Start : publisher_luminosity"
ros2 run projet_pkg publisher_luminosity > src/projet_pkg/log/log_publisher_luminosity.txt 2>&1 &

echo "[projet_pkg] > Start : publisher_time"
ros2 run projet_pkg publisher_time > src/projet_pkg/log/log_publisher_time.txt 2>&1 &


echo "[projet_pkg] > Start : publisher_presenceInt"
ros2 run projet_pkg publisher_presenceInt > src/projet_pkg/log/log_publisher_presenceInt.txt 2>&1 &

echo "[projet_pkg] > Start : publisher_presenceout"
ros2 run projet_pkg publisher_presenceOut > src/projet_pkg/log/log_publisher_presenceOut.txt 2>&1 &

echo "[projet_pkg] > Start : service_bp"
ros2 run projet_pkg service_bp > src/projet_pkg/log/log_service_bp.txt 2>&1 &

echo "[projet_pkg] > Start : client_bp"
ros2 run projet_pkg client_bp > src/projet_pkg/log/log_client_bp.txt 2>&1 &


python3 src/projet_pkg/projet_pkg/info_web.py


echo ">> Exécution terminée <<"







