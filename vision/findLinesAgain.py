# Python program to illustrate HoughLine
# method for line detection
import numpy as np
import cv2
print(cv2.__version__)
cap = cv2.VideoCapture("kickit.avi")



while(cap.isOpened()):
    ret, frame = cap.read()

    img = frame
# Convert the img to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   # cv2.imwrite('gray.jpg', gray)

# Apply edge detection method on the image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
  #  cv2.imwrite('edges.jpg', edges)

# This returns an array of r and theta values

    lines = cv2.HoughLines(edges, 1, np.pi/180, 150)


#  i = 0
# idontknowhowtouseforloopsinpython = (len(lines));
# The below for loop runs till r and theta values
# are in the range of the 2d array

#   while(i < idontknowhowtouseforloopsinpython):
    img = p.__find_lines(lines)

    # cMax = max(contours, key = cv2.contourArea) python's indent system is crap :)
 #   cMax = max(contours, key=cv2.contourArea)
#    cv2.rectangle(dst2, (x, y), (x + w, y + h), (0, 0, 255), 2)
  #  rect = cv2.minAreaRect(cMax)
   # box = cv2.boxPoints(rect)
  #  box = np.int0(box)

   # for c in contours:
    #    rect = cv2.boundingRect(c)
     #   x, y, w, h = rect
      #  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('frame', img)
    cv2.waitKey(30)
