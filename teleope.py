#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Joy


class JoyTwist(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber(
            '/joy', Joy, self.joy_callback, queue_size=1)

    def joy_callback(self, joy_msg):
        # up -> joy_msgs.axes[1] = 1
        # down -> joy_msgs.axes[1] = -1
        # left -> joy_msgs.axes[0] = 1
        # right -> joy_msgs.axes[0] = -1
        print(joy_msg.axes[0])


if __name__ == '__main__':
    rospy.init_node('logicool_cmd_vel')
    logicool_cmd_vel = JoyTwist()
    rospy.spin()
