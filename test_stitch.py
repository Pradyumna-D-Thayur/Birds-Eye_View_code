import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
img1=cv2.imread("1.jpg")
img2=cv2.imread("2.jpg")
Img1=cv2.resize(img1,(0,0),None,0.5,0.5)
Img2=cv2.resize(img2,(0,0),None,0.5,0.5)
images=[Img1,Img2]
t1=time.time()
stitcher=cv2.Stitcher.create()
(status,result)=stitcher.stitch(images)
t2=time.time()
if(status==cv2.STITCHER_OK):
    print("done")
else:
    print('No')
#cv2.imshow("original",img)
cv2.imshow("left",Img1)
cv2.imshow("right",Img2)
cv2.waitKey(0)
#cv2.imshow("Result",result)
print(stitcher.stitch(images))
print(t2-t1)
cv2.waitKey(0)
