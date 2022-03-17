import cv2 
import numpy as np 

thresh = 50000


def check(img,b,t,mul):
    ret = False
    val = np.sum(img[b:t,0:w])*mul
    print(val)
    if(val <= thresh):
        ret = True
    return ret 


image = cv2.imread('C:\\Users\\mcser\\Documents\\scoo\\NCAT 2021-22\\IEEEHWCOMP\\RobotCode\\pole-vision\\depth.png')

h = image.shape[0]
w = image.shape[1]

const = 40


bottomL = round((h/2)-(h/const))
topL = round((h/2)+(h/const))


cv2.line(image,[0,topL],[w,topL],[0,0,255], 2 )

cv2.line(image,[0,bottomL],[w,bottomL],[0,0,255], 2 )

while(True):
    detect = check(image,bottomL,topL,1)
    if(detect):
        cv2.rectangle(image,[0,topL],[w,bottomL],[255,0,0],-1)
    cv2.imshow("frame",image)
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        cv2.destroyAllWindows()


#take image feed
#check if pole is close
#(by taking slice of image, lloking for specific numerical value)
#pic x, pic y, theta = dist x
#pole height, depth of pole




