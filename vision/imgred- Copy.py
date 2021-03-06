# Python program to illustrate HoughLine 
# method for line detection 
import cv2 
import numpy as np 
  
# Reading the required image in  
# which operations are to be done.  
# Make sure that the image is in the same  
# directory in which this python program is 


cap = cv2.VideoCapture(1);


while(cap.isOpened()):
	ret, image = cap.read()
	boundaries = [
	([0, 0, 100], [50, 50, 200])
]

	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(image, lower, upper)
		img= cv2.bitwise_and(image, image, mask = mask)
		
		# Convert the img to grayscale 
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
		cv2.imwrite('gray.jpg', gray)
		  
		# Apply edge detection method on the image 
		edges = cv2.Canny(gray,50,150,apertureSize = 3) 
		cv2.imwrite('edges.jpg', edges)
		  
		# This returns an array of r and theta values 
		lines = cv2.HoughLines(edges,1,np.pi/180, 360) 
		

		
		ret, thresh = cv2.threshold(edges, 215, 255, cv2.THRESH_BINARY)
		contours, hierarchy = cv2.findContours(thresh, 1, 2)  
    
		if(len(contours) > 0): 
			cMax = max(contours, key=cv2.contourArea)
			rect = cv2.minAreaRect(cMax)
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			cv2.drawContours(image, [box], cv2.FILLED, (255,0,127), 3)
			
			circleRect = cv2.boundingRect(cMax)
			x,y,w,h = circleRect
		  
			cv2.circle(image,(int(x+(w/2)), int(y+(h/2))), 6, (0,255,0), 2)
			
		cv2.imshow('frame',img)
		cv2.waitKey(40)

			
			
  

  

