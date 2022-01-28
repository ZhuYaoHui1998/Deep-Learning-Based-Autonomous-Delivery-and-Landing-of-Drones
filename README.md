# Yolov5 with pixhawk
This project uses Yolov5 target detection algorithm and Jetsonnano to carry out uav target tracking, delivery and landing on Pixhawk UAV
Hardware parameters：Jetson nano B01、Pixhawk2.4.8
Communication protocol：Mavlink
Yolov5 training datasets are in the datasets folder
Yolov5 target detection(detect1.py) and uav flight control(takeoff.py), Python multi-threaded programs(main.py) in the Code folder
The Yolov5 output layer is modified and the target point coordinate system is improved to takeoff.py
The final demonstration video of the drone is in the experiment folder
Email: 510677932@qq.com
