#!/usr/bin/env python  
# -*- coding: utf-8 -*-  


from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import detect1
class Vihecle(object):
    def connect(self):
        connection_string = '/dev/ttyUSB0'
        print('Connecting to vehicle on: %s' % connection_string) 
        self.vehicle = connect(connection_string,wait_ready=True,baud=57600)
        print (" Channel overrides: %s" , self.vehicle.channels.overrides)

    def arm_and_takeoff(self,aTargetAltitude):
        print("Arming motors")
        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True
        while not self.vehicle.armed:
            print(" Waiting for arming...")
            time.sleep(1)

        print("Taking off!")
        self.vehicle.simple_takeoff(aTargetAltitude)
        while True:
            print(self.vehicle.rangefinder.distance)
            if self.vehicle.rangefinder.distance >= aTargetAltitude * 0.85:
                break
            time.sleep(1)

    def send_body_ned_velocity(self,velocity_x, velocity_y, velocity_z):
        msg = self.vehicle.message_factory.set_position_target_local_ned_encode(
            0,      
            0, 0,    
            mavutil.mavlink.MAV_FRAME_BODY_NED, 
            0b0000111111000111, 
            0, 0, 0, 
            velocity_x, velocity_y, velocity_z, 
            0, 0, 0,
            0, 0)
        for x in range(0,1):
            self.vehicle.send_mavlink(msg)
            time.sleep(1)

    def go_left(self):  
        self.send_body_ned_velocity(0,-0.05,0)
        print('left')

    def go_right(self):
        self.send_body_ned_velocity(0,0.05,0)
        print('right')

    def go_forward(self):
        self.send_body_ned_velocity(0.1,0,0)
        print('forward')

    def go_back(self):
        self.send_body_ned_velocity(-0.1,0,0)
        print('back')

    def go_up(self):
        self.send_body_ned_velocity(0,0,-0.1)
        print('up')

    def go_down(self):
        self.send_body_ned_velocity(0,0,0.1)
        print('down')
        
    def go_zuoqian(self):
        self.send_body_ned_velocity(0.1,-0.2,0)
        print('zuoqian')
    
    def go_youqian(self):
        self.send_body_ned_velocity(0.1,0.1,0)
        print('youqian')        

    def go_zuohou(self):
        self.send_body_ned_velocity(-0.2,-0.1,0)
        print("zuohou")
        
    def go_youhou(self):
        self.send_body_ned_velocity(-0.1,0.1,0)
        print("zuohou")

    def land(self):
        print("Land")
        self.vehicle.mode = VehicleMode("LAND")
        print("Close vehicle object")
        self.vehicle.close()

    def print_info():
        while True:
            print(detect1.label_list)
    
    def seach_target1(self):
        while detect1.label1[0]>50 or detect1.label1[0]<-80 or detect1.label1[1]>80 or detect1.label1[1]<-80:
            print(self.vehicle.rangefinder.distance)
            if detect1.label1[2]!='None':
                if detect1.label1[0]>50:
                    self.go_right()
                elif detect1.label1[0]<-50:
                    self.go_left()
                elif detect1.label1[1]>50:
                    self.go_back()
                elif detect1.label1[1]<-50:
                    self.go_forward()
            else:
                print("1loss Arm")
    def seach_target2(self):
        while detect1.label2[0]>80 or detect1.label2[0]<-80 or detect1.label2[1]>80 or detect1.label2[1]<-80:
            print(self.vehicle.rangefinder.distance)
            if detect1.label2[2]!='None':
                if detect1.label2[0]>50:
                    self.go_right()
                elif detect1.label2[0]<-50:
                    self.go_left()
                elif detect1.label2[1]>50:
                    self.go_back()
                elif detect1.label2[1]<-50:
                    self.go_forward()
            else:
                print("2loss Arm")
                time.sleep(0.5)
                pass
    def seach_target3(self):
        while detect1.label3[0]>80 or detect1.label3[0]<-80 or detect1.label3[1]>80 or detect1.label3[1]<-80:
            print(self.vehicle.rangefinder.distance)
            if detect1.label3[2]!='None':
                if detect1.label3[0]>50:
                    self.go_right()
                if detect1.label3[0]<-50:
                    self.go_left()
                if detect1.label3[1]>50:
                    self.go_back()
                if detect1.label3[1]<-50:
                    self.go_forward()
            else:
                print("3loss Arm")
                time.sleep(0.5)
                pass
    def seach_target4(self):
        while detect1.label4[0]>80 or detect1.label4[0]<-80 or detect1.label4[1]>80 or detect1.label4[1]<-80:
            print(self.vehicle.rangefinder.distance)
            if detect1.label4[2]!='None':
                if detect1.label4[0]>50:
                    self.go_right()
                elif detect1.label4[0]<-50:
                    self.go_left()
                elif detect1.label4[1]>50:
                    self.go_back()
                elif detect1.label4[1]<-50:
                    self.go_forward()
            else:
                print("4loss Arm")
                time.sleep(0.1)
                pass
    def seach_target5(self):
        while detect1.label5[0]>80 or detect1.label5[0]<-80 or detect1.label5[1]>80 or detect1.label5[1]<-80:
            print(self.vehicle.rangefinder.distance)
            if detect1.label5[2]!='None':
                if detect1.label5[0]>50:
                    self.go_right()
                elif detect1.label5[0]<-50:
                    self.go_left()
                elif detect1.label5[1]>50:
                    self.go_back()
                elif detect1.label5[1]<-50:
                    self.go_forward()
            else:
                print("5loss Arm")
                time.sleep(0.5)
                pass
    def seach_target6(self):
        while detect1.label6[0]>80 or detect1.label6[0]<-80 or detect1.label6[1]>80 or detect1.label6[1]<-80:
            print(self.vehicle.rangefinder.distance)
            if detect1.label6[2]!='None':
                if detect1.label6[0]>50:
                    self.go_right()
                elif detect1.label6[0]<-50:
                    self.go_left()
                elif detect1.label6[1]>50:
                    self.go_back()
                elif detect1.label6[1]<-50:
                    self.go_forward()
            else:
                print("6loss Arm")
                time.sleep(0.5)
                pass         

    def servo(self,angle):
        self.vehicle.channels.overrides['6'] = angle
    def putdown1(self):
           print (" Channel overrides: %s" , self.vehicle.channels.overrides)
           self.vehicle.channels.overrides['6'] = 1820
    def putdown2(self):
           print (" Channel overrides: %s" , self.vehicle.channels.overrides)
           self.vehicle.channels.overrides['6'] = 2000    
    def putdown3(self):
           print (" Channel overrides: %s" , self.vehicle.channels.overrides)
           self.vehicle.channels.overrides['6'] = 1000  
def main():
    vehicle1=Vihecle()
    vehicle1.connect()
    vehicle1.arm_and_takeoff(0.8)
    while detect1.label4[2]== 'None':
        print("detect4")
        vehicle1.go_youqian()       
    vehicle1.seach_target4()
    vehicle1.putdown1()
    time.sleep(1)

    while detect1.label3[2]== 'None':
        print("detect3")
        vehicle1.go_zuoqian()    
    vehicle1.seach_target3()
    vehicle1.putdown2()
    time.sleep(1)
    for i in range(2):
        vehicle1.go_back()
        time.sleep(1)
    while detect1.label5[2]== 'None':
        print("detect5")
        vehicle1.go_zuohou()
        time.sleep(1)
    vehicle1.seach_target5()
    vehicle1.land() 
    time.sleep(3)
    vehicle1.putdown3()
    time.sleep(1)
        
    # while detect1.label3[2]=='None':
    #     vehicle1.go_right()
    # vehicle1.seach_target3()
    # vehicle1.putdown2()  

    