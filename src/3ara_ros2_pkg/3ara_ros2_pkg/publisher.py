
import os
import sys
import rclpy
import time
import std_msgs
from sensor_msgs.msg import JointState
from numpy import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from rclpy.node import Node

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi("/home/cipo/Documents/ROS2_Tutorials/ros2_ws/src/3ara_ros2_pkg/3ara_ros2_pkg/MainWindow.ui", self)   #Full path to .ui file
        
        # Create a node
        self.publisher = MinimalPublisher()
        self.publisher_ = self.publisher.create_publisher(JointState, 'setpoint_angles', 10)
        
        self.joints = JointState()
        self.joints.name = ['angle_1', 'angle_2', 'angle_3']
      
        # Enables go to home position
        self.goToHomeButton.setEnabled(True)

        # Enables move button
        self.InverseKinematics.setEnabled(True)

        # goToHomeButton callback function
        self.goToHomeButton.clicked.connect(self.goToHomeMsg)

        # Set routineButton callback function
        self.routineButton.clicked.connect(self.executeRoutine1)

        # InverseKinematics callback function
        self.InverseKinematics.clicked.connect(self.moveToPosition)
        
        # Callbacks function when sliders changes it's values
        self.jointOneSlider.valueChanged[int].connect(self.slideValueChanged)
        self.jointTwoSlider.valueChanged[int].connect(self.slideValueChanged)
        self.jointThreeSlider.valueChanged[int].connect(self.slideValueChanged)

        self.IKJointOne.valueChanged[int].connect(self.rightSlideValueChanged)
        self.IKJointTwo.valueChanged[int].connect(self.rightSlideValueChanged)
        self.IKJointThree.valueChanged[int].connect(self.rightSlideValueChanged)

        # Style for LCD numbers
        self.showLCD_1.setDigitCount(3)
        self.showLCD_2.setDigitCount(3)
        self.showLCD_3.setDigitCount(3)

        self.showIKJointOne.setDigitCount(4)
        self.showIKJointTwo.setDigitCount(4)
        self.showIKJointThree.setDigitCount(4)

    def goToHomeMsg(self):
        self.jointOneSlider.setValue(0)
        self.jointTwoSlider.setValue(0)
        self.jointThreeSlider.setValue(0)
        self.joints.position = [self.jointOneSlider.value(), self.jointTwoSlider.value(), self.jointThreeSlider.value()]
        self.pub.publish(self.joints) 
        
    def executeRoutine1(self):
        execution_time = 8000                   # Time to reach the next position
        for i in range(2):                      # Number of times to execute the routine   
            self.jointOneSlider.setValue(45)
            self.jointTwoSlider.setValue(45)
            self.jointThreeSlider.setValue(45)
            delayLoop = QEventLoop()
            QTimer.singleShot(execution_time, delayLoop.quit)
            delayLoop.exec_()
            self.jointOneSlider.setValue(25)
            self.jointTwoSlider.setValue(25)
            self.jointThreeSlider.setValue(25)
            delayLoop = QEventLoop()
            QTimer.singleShot(execution_time, delayLoop.quit)
            delayLoop.exec_()
            print(i)
    
    def moveToPosition(self):
        self.joints.position = [self.IKJointOne.value(), self.IKJointTwo.value(), self.IKJointThree.value()]
        self.pub.publish(self.joints) 
        

    def slideValueChanged(self):
        self.showLCD_1.display(self.jointOneSlider.value())
        self.showLCD_2.display(self.jointTwoSlider.value())
        self.showLCD_3.display(self.jointThreeSlider.value())
        #self.joints.position = [self.jointOneSlider.value(), self.jointTwoSlider.value(), self.jointThreeSlider.value()]
        self.joints.position = [float(self.jointOneSlider.value()), float(self.jointTwoSlider.value()), float(self.jointThreeSlider.value())]
        self.publisher_.publish(self.joints)

    def rightSlideValueChanged(self):
        self.showIKJointOne.display(self.IKJointOne.value())
        self.showIKJointTwo.display(self.IKJointTwo.value())
        self.showIKJointThree.display(self.IKJointThree.value())


def main(arg=None):
    
    app = QApplication(sys.argv)
    rclpy.init(args=sys.argv)
    
    controlWindow = Window()
    controlWindow.show()
    app.exec_()
    

if __name__ == '__main__':
    main()

    