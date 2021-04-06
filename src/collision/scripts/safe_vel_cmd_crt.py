#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class SafeVelCmdCrt:

    def __init__(self):
        rospy.init_node('safe_vel_cmd_crt', anonymous=True)

        # First publisher
        self.pub = rospy.Publisher('/cmd_vel_safe_output', Twist, queue_size=10)

        self.distance = 1

        # Then subscriber
        rospy.Subscriber('/cmd_vel_safe_input', Twist, self.callbackTwist)
        rospy.Subscriber('/min_dist', Float32, self.callbackFloat)
        

    def callbackTwist(self, data):
        data.linear.x = data.linear.x * (self.distance / 2)
        self.pub.publish(data)
    
    def callbackFloat(self, data):
        self.setDistance(data.data)
        
    def setDistance(self, distance):
        self.distance = distance

if __name__ == '__main__':
    try:
        S = SafeVelCmdCrt()
        rospy.spin() 
    except rospy.ROSInterruptException:
        pass