#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


class KeyTwist(object):
    def __init__(self):
        self._twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=100)

    def main(self):
        while not rospy.is_shutdown():
            twist = Twist()
            direction = raw_input('f: foward, l: left, r: right > ')
            if 'f' in direction:
                twist.linear.x = 0.5
            elif 'l' in direction:
                twist.angular.z = 0.5
            elif 'r' in direction:
                twist.angular.z = -0.5
            elif 'q' in direction:
                break
            else:
                twist.linear.x = 0.0
                twist.angular.z = 0.0
            self._twist_pub.publish(twist)


if __name__ == '__main__':
    rospy.init_node('keyboard_cmd_vel')
    keyboard_cmd_vel = KeyTwist()
    keyboard_cmd_vel.main()
