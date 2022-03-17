
from pyexpat.model import XML_CQUANT_PLUS
import cv2 
import numpy as np 
import matplotlib.pyplot as mpl
import sys


def printf(format, *args):
    sys.stdout.write(format % args)


def log(image,clr,color,off):
	font = cv2.FONT_HERSHEY_SIMPLEX
	org = (5, 30+off)
	fontScale = 1
#	color = (255, 0, 0)
	thickness = 2
	image = cv2.putText(image, str(clr), org, font, 
					fontScale, color, thickness, cv2.LINE_AA)

def check(chan,img,mul):
    ret = False
    if( round( (np.sum(chan[0:h,x_l:x_r])/(np.sum(img[0:h,x_l:x_r]))) *mul) == 1) : ret =  True
    return ret  




cap = cv2.VideoCapture(0)







while(cap.isOpened()):
    ret, image = cap.read()
    #image = cv2.imread('1.jpg')
    (B, G, R) = cv2.split(image)

    h = image.shape[0]
    w = image.shape[1]
    #print(image.shape)
    
    #cropped_image = image[0:h,80:280]
    #cv2.imshow("cropped", cropped_image)
    

    interval = 100

    xinterval  = (int)(w/interval)

    img_list =[]
    columns = []

    x_l = 0
    x_r = xinterval

    r = False
    g = False 
    b = False

    

    for x in range(interval):
        cup = False 
        #img_list.append(np.sum(R[0:h,x_l:x_r]))
        #img_list.append(round( (np.sum(R[0:h,x_l:x_r])/(np.sum(image[0:h,x_l:x_r]))) *1.36))
        columns.append(x_l)

        #printf("value=%d, x_l=%d, x_r=%d\n",img_list[x],x_l,x_r)
        r=check(R,image,1.3)
        g=check(G,image,1.3)
        b=check(B,image,1.6)

        printf("%d,%d,%d\n",r,g,b)

        if(r and not g and not b):
            cup = True

        img_list.append(cup)



        x_l = x_r
        x_r+=xinterval 

    #img_list.sort()
    log(image,img_list.index(max(img_list)),[0,0,255],60)	

    #print("\n")
    #print(check(R,image))
    #print(check(G,image))
    #print(check(B,image))


    
    
    mpl.cla()
    mpl.plot(columns,img_list)

    mpl.pause(0.02)

        


# show each channel individually

    cv2.imshow("Red",image)
    cv2.waitKey(40)

mpl.show()