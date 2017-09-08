#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class JoyTwist(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber(
            '/joy', Joy, self.joy_callback, queue_size=1)
        self._twist_pub = rospy.Publisher(
            '/cmd_vel', Twist, queue_size=100)

    def joy_callback(self, joy_msg):
        twist = Twist()
        twist.linear.x = joy_msg.axes[1] * 0.2
        twist.angular.z = joy_msg.axes[0] * 3.14 / 32
        self._twist_pub.publish(twist)


if __name__ == '__main__':
    rospy.init_node('logicool_cmd_vel')
    logicool_cmd_vel = JoyTwist()
    rospy.spin()
