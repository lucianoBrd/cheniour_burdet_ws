#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class SafeVelCmdCrt:

    def __init__(self):
        rospy.init_node('safe_vel_cmd_crt', anonymous=True)

        # First publisher
        self.pub = rospy.Publisher('/cmd_vel_safe_output', Twist, queue_size=10)

        # Then subscriber
        rospy.Subscriber('/cmd_vel_safe_input', Twist, self.callback)
        

    def callback(self, data):
        #rospy.loginfo(data.data)
        self.pub.publish(data)

if __name__ == '__main__':
    try:
        S = SafeVelCmdCrt()
        rospy.spin() 
    except rospy.ROSInterruptException:
        pass