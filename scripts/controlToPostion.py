#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Pose, Twist
import tf

global goal_pose
global pub_twist

goal_pose=Pose()
pub_twist=0

def calculate_vel(distance, angle):
	global pub_twist
	speed=Twist()
	loop=rospy.Rate(10)

	print "angle: "+str(angle)
	print "distance: "+str(distance)
	#CHANGE THIS CONSTANTS FOR YOUR APPLICATION
	linear_vel_k=.1
	anglular_vel_k=.1

	if(distance==0 and angle==0):
		speed.linear.x=0
		speed.linear.y=0
		speed.linear.z=0
		speed.angular.x=0
		speed.angular.y=0
		speed.angular.z=0
	else:
		#Set these variables for your application

		speed.linear.x=linear_vel_k*distance
		speed.linear.y=0
		speed.linear.z=0
		speed.angular.x=0
		speed.angular.y=0
		speed.angular.z=-anglular_vel_k*(angle/10)

	#This line publishes the motion command to the base
	pub_twist.publish(speed)
	loop.sleep()


def callback_goal_pose(msg):
	#global goal_pose
	persons_centroid=msg

	##set the parameters to operational values for your application
	distance_th=.5  
	angle_th=.50

	##type(persons_centroid) = geometry_msgs.msg.Pose
	#persons_centroid.position.x
	#persons_centroid.position.y
	#persons_centroid.position.z
	#
	#quaternion = (
	#    persons_centroid.orientation.x,
	#    persons_centroid.orientation.y,
	#    persons_centroid.orientation.z,
	#    persons_centroid.orientation.w)
	#euler = tf.transformations.euler_from_quaternion(quaternion)
	#roll = euler[0]
	#pitch = euler[1]
	#yaw = euler[2]

	#calculate distance and angle from the current pose to the goal pose

	distance=0 #distance of the robot wrt the person should be in meter
	angle=0 #orientation of the robot wrt the person should be in degrees


	#DO NOT FORGET TO CHANGE THE VELOCITY CONSTANTS IN THE calculate_vel FUNCTION
	if abs(distance)>distance_th and abs(angle)>angle_th:
		calculate_vel(distance,angle)
	elif abs(distance)>distance_th:
		calculate_vel(distance,0)
	elif abs(angle)>angle_th: 
		calculate_vel(0,angle)
	else:
		calculate_vel(0,0)



def main():
	global pub_twist
	print "Initializing control to position"
	rospy.init_node('control_to_position', anonymous=True)

	#Subscribers (sources)
	rospy.Subscriber("/persons_centroid", Pose , callback_goal_pose)

	#Publishers (results)
	pub_twist = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)

	loop=rospy.Rate(10)
	while not rospy.is_shutdown():
		loop.sleep()



if __name__=='__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
