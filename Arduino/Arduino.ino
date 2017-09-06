#include <ros.h>
#include <sensor_msgs/Joy.h>

ros::NodeHandle nh;

void messageCb(const sensor_msgs::Joy &joy_msg)
{

  if (joy_msg.axes[1] != 1.0)
  {
    digitalWrite(2, LOW);
    digitalWrite(12, LOW);
  }
  else
  {
    digitalWrite(2, HIGH);
    digitalWrite(12, HIGH);
  }
}

ros::Subscriber<sensor_msgs::Joy> sub("/joy", &messageCb);

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