#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
from sensor_msgs.msg import Image, PointCloud2
import cv2
from cv_bridge import CvBridge
#import pcl
import ros_numpy
import numpy as np
import tf

global persons_centroid
global rgb_mat
global depth_mat
global display

rgb_mat=0
depth_mat=0
display =False
persons_centroid=Pose()

def callback_rgb_rect(msg):
	global rgb_mat
	#print "rgb rows: " +str(msg.height)
	#print "rgb columns: "+str(msg.width)
	#print "rgb encoding: "+str(msg.encoding)
	bridge_rgb=CvBridge()
	rgb_mat=bridge_rgb.imgmsg_to_cv2(msg,msg.encoding)

def callback_depth_rect(msg):
	global depth_mat
	global display
	#print "depth rows: "+str(msg.height)
	#print "depth columns: "+str(msg.width)
	#print "depth encoding: "+str(msg.encoding)
	display=True
	bridge_depth=CvBridge()
	depth_mat=bridge_depth.imgmsg_to_cv2(msg,msg.encoding)

def callback_point_cloud(msg):
	global persons_centroid
	pc = ros_numpy.numpify(msg)

	#pc[j][i] => (x, y, z)
	#i: 0...619 ~ width
	#j: 0...479 ~ height
	#x, positive from the center of the camera to the right
	#y, positive from the center of the camera to the bottom
	#z, positive from the center of the camera to the front

	#Example to read a point in the point_cloud
	i = 320 
	j = 240 

	p = [pc[j][i][0], pc[j][i][1], pc[j][i][2]]

	print "central point" 
	print p

	#Find the centroid of the closest object
	#Insert your code here

	##type(persons_centroid) = geometry_msgs.msg.Pose
	#persons_centroid.position.x
	#persons_centroid.position.y
	#persons_centroid.position.z
	#
	#quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
	#persons_centroid.orientation.x = quaternion[0]
	#persons_centroid.orientation.y = quaternion[1]
	#persons_centroid.orientation.z = quaternion[2]
	#persons_centroid.orientation.w = quaternion[3]

def main():
	global persons_centroid
	global rgb_mat
	global depth_mat
	global display

	print "Initializing rgbd_reader"
	rospy.init_node('rgbd_reader', anonymous=True)

	#Subscribers (sources)
	rospy.Subscriber("/camera/rgb/image_rect_color", Image , callback_rgb_rect)
	rospy.Subscriber("/camera/depth_registered/image", Image, callback_depth_rect)
	rospy.Subscriber("/camera/depth_registered/points", PointCloud2, callback_point_cloud)

	#Publishers (results)
	pub_centroid=rospy.Publisher('/persons_centroid', Pose, queue_size=1)

	#Initialising the pub_centroid data to be published to /persons_centroid
	persons_centroid.position.x=0
	persons_centroid.position.y=0
	persons_centroid.position.z=0
	persons_centroid.orientation.x=0
	persons_centroid.orientation.y=0
	persons_centroid.orientation.z=0
	persons_centroid.orientation.w=0

	loop=rospy.Rate(10)
	while not rospy.is_shutdown():
		#print display
		if(display):
			cv2.imshow("rgb", rgb_mat)
			cv2.imshow("depth", depth_mat)
			cv2.waitKey(1)

		#Publishing to /persons_centroid
		#In this example, the pub_centroid is updated in the callback_point_clod function
		pub_centroid.publish(persons_centroid)
		loop.sleep()



if __name__=='__main__':
	try:
		main()
		cv2.destroyAllWindows()
	except rospy.ROSInterruptException:
		pass
