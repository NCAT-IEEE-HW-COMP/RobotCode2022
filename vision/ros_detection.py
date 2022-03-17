#!/usr/bin/env python3
#subscribe to realsense and get cameraCB
import rospy 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
class AggiebotDetection(object):

  def __init__(self):
    ##init
    print ("AggiebotDetection")

    self.env_name = rospy.get_param("/env","comp")
    if self.env_name == "robot":
      from dualshock4 import DualShock4robot
      self.controller = DualShock4robot()
      rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback, queue_size=1)
      rospy.Subscriber("/camera/depth/image_rect_raw", Image, self.depth_callback, queue_size=1)
    else:
      from dualshock4 import DualShock4
      self.controller = DualShock4()
      rospy.Subscriber("/usb_cam/image_raw", Image, self.image_callback, queue_size=5)
      
      
    bridge = CvBridge()
    #publishers and subscribers
    rospy.Subscriber("/camera_depth_image_rect_raw", Image, self.image_callback, queue_size=5)
    #/camera/color/image_raw
    self.imageCB_pub = rospy.Publisher("/tbd", Image, queue_size = 1) 
    
    #setup rosnode 
    rospy.init_node ('aggiebot_detection',anonymous=False)

  # Receives an image does something with it, publish new image
  def image_callback(self, image):
    opencv_image = self.bridge.imgmsg_to_cv2(image, desired_encoding='passthrough')
    ros_image_message = self.bridge.cv2_to_imgmsg(opencv_image, encoding="passthrough")
    self.imageCB_pub.publish(ros_image_message)  

  def depth_callback(self, depth):
    opencv_image = self.bridge.imgmsg_to_cv2(depth, desired_encoding='passthrough')
    ros_image_message = self.bridge.cv2_to_imgmsg(opencv_image, encoding="passthrough")
    self.imageCB_pub.publish(ros_image_message)  

if __name__ == '__main__':
    try:
        AggiebotDetection()
    except rospy.ROSInterruptException:
        pass