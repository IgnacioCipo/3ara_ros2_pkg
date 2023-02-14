import rclpy
#import serial
import threading
import sys
from std_msgs.msg import Float32
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import struct
from rclpy.node import Node

'''
class SerialCommunication():
    def __init__(self):
        #self.device_port = rospy.get_param('~port', '/dev/ttyS0')           # COM PORT - Default -> 
        #self.baudrate = rospy.get_param('~baudrate', '57600')               # Baudrate 
        #self.timeout = float( rospy.get_param('~timeout', '10'))            # 10 Hz 
        #self.angles_topic = rospy.get_param('~angles_topic', 'angles')
        #self.comm_freq = float(rospy.get_param('~comm_freq', '15'))         # 15 Hz for communication
        self.device_port = node.declare_parameter('port', '/dev/ttyS0')
        assert isinstance(port, str), 'port parameter must be a str'

        self.baudrate = node.declare_parameter('baudrate', 57600).value
        assert isinstance(baudrate, int), 'baudrate parameter must be an integer'

        self.data_ready = False
        self.data_ok = False
        self.serial = serial.Serial()
        self.thread_stop = threading.Event()

        try:
            self.serial = serial.Serial(self.device_port, self.baudrate, timeout=self.timeout)
        except:
            self.serial.close()
            sys.exit(0)

        self.publisher = node.create_publisher(String, 'angles_topic')
        
        # Subscriber definition to get the desires angles from the GUI
        self.subscriber = node.create_subscription(String, 'angles_topic', self.sendToSTM)

        # Send info to STM32f407
    def sendToSTM(self, joints):
        angle_1 = joints.position[0]
        angle_2 = joints.position[1]
        angle_3 = joints.position[2]
        print("Angle 1: ", angle_1)
        print("Angle 2: ", angle_2)
        print("Angle 3: ", angle_3)
     
        angle_1_bytes = struct.pack('f', angle_1)
        angle_2_bytes = struct.pack('f', angle_2)
        angle_3_bytes = struct.pack('f', angle_3)
        tx_buffer = [0xA1, angle_1_bytes[0], angle_1_bytes[1], angle_1_bytes[2], angle_1_bytes[3], 
            angle_2_bytes[0], angle_2_bytes[1], angle_2_bytes[2], angle_2_bytes[3],
            angle_3_bytes[0], angle_3_bytes[1], angle_3_bytes[2], angle_3_bytes[3], 0xB1]

        self.serial.write(tx_buffer)
        print("Package sent")
'''
class Subscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscriber = self.create_subscription(JointState, 'setpoint_angles', self.my_callback, 10)
        self.subscriber

    def my_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.position)


def main(arg=None):
    rclpy.init(args=sys.argv)

    my_subscriber_node = Subscriber()

    rclpy.spin(my_subscriber_node)

    print("Shutting down")
    
    #Comms.serial.close()
    #rclpy.signal_shutdown("End")

if __name__ == '__main__':
    main()