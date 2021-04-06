#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Float32
from kobuki_msgs.msg import Sound, Led

class SoundMinDistFeedback:

    def __init__(self):
        rospy.init_node('sound_min_dist_feedback', anonymous=True)

        # First publisher
        self.pub_sound = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)
        self.pub_led = rospy.Publisher('/mobile_base/commands/led1', Led, queue_size=10)

        self.msg_sound = Sound()
        self.msg_sound.value = 2

        self.msg_led = Led()
        self.msg_led.value = 0

        self.distance = 1
        
        # Then subscriber
        rospy.Subscriber('/min_dist', Float32, self.callback)

        self.notifSound()
        

    def callback(self, data):
        #rospy.loginfo(data.data)
        self.setDistance(data.data)
        
    def setDistance(self, distance):
        self.distance = distance

    def notifSound(self):
        while not rospy.is_shutdown(): 
            self.pub_sound.publish(self.msg_sound)
            self.pub_led.publish(self.msg_led)
            time.sleep(self.distance / 2)

            if self.msg_led.value == 0:
                self.msg_led.value = 1
            else
                self.msg_led.value = 0

if __name__ == '__main__':
    try:
        S = SoundMinDistFeedback()
        rospy.spin() 
    except rospy.ROSInterruptException:
        pass