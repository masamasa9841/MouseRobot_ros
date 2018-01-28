#include <ros.h>
#include <geometry_msgs/Twist.h>

ros::NodeHandle nh;

void messageCb(const geometry_msgs::Twist &joy_msg)
{
  if (joy_msg.linear.x > 0.0)
  {
    digitalWrite(2, HIGH);
    digitalWrite(12, HIGH);
  }
  else if (joy_msg.angular.z > 0.0)
  {
    digitalWrite(2, HIGH);
    digitalWrite(12, LOW);
  }
  else if (joy_msg.angular.z < 0.0)
  {
    digitalWrite(2, LOW);
    digitalWrite(12, HIGH);
  }
  else
  {
    digitalWrite(2, LOW);
    digitalWrite(12, LOW);
  }
}

ros::Subscriber<geometry_msgs::Twist> sub("/cmd_vel", &messageCb);

void setup()
{
  pinMode(2, OUTPUT);
  pinMode(12, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}