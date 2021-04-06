#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Float32
from kobuki_msgs.msg import Sound 

class SoundMinDistFeedback:

    def __init__(self):
        rospy.init_node('sound_min_dist_feedback', anonymous=True)

        # First publisher
        self.pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)

        self.msg_sound = Sound()
        self.msg_sound.value = 2

        self.distance = 1
        
        # Then subscriber
        rospy.Subscriber('/min_dist', Float32, self.callback)
        rospy.spin() 

        self.notifSound()


    def callback(self, data):
        #rospy.loginfo(data.data)
        self.setDistance(data.data)
        
    def setDistance(self, distance):
        self.distance = distance

    def notifSound(self):
        while not rospy.is_shutdown(): 
            self.pub.publish(self.msg_sound)
            time.sleep(self.distance)

if __name__ == '__main__':
    try:
        SoundMinDistFeedback()
    except rospy.ROSInterruptException:
        pass