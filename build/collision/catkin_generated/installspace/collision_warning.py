#!/usr/bin/env python3
import rospy
from kobuki_msgs.msg import Sound 
from kobuki_msgs.msg import BumperEvent

class CollisionWarning:

    def __init__(self):
        rospy.init_node('collision_warning', anonymous=True)

        self.pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)

        self.msg_sound = Sound()
        self.msg_sound.value = 6
        
        rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, self.callback)
        rospy.spin() 


    def callback(self,data):
        if data.state == 1:
            rospy.loginfo("Bumper est enfoncé")
            self.pub.publish(self.msg_sound)


if __name__ == '__main__':
    try:
        CollisionWarning()
    except rospy.ROSInterruptException:
        pass