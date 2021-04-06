#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

class MinDistDetection:

    def __init__(self):
        rospy.init_node('min_dist_detection', anonymous=True)

        # First publisher
        self.pub = rospy.Publisher('/min_dist', Float32, queue_size=1)
        
        # Then subscriber
        rospy.Subscriber('/scan', LaserScan, self.callback)
        rospy.spin() 


    def callback(self, data):
        #rospy.loginfo(self.computeMin(data.ranges))
        self.pub.publish(self.computeMin(data.ranges))

    def computeMin(self, arr):
        return np.nanmin(arr)

if __name__ == '__main__':
    try:
        MinDistDetection()
    except rospy.ROSInterruptException:
        pass