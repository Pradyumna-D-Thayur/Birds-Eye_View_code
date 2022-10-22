import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
im=input("2/m?\n")
img=cv2.imread("test.jpg")
rsz_Img=cv2.resize(img,(0,0),None,0.5,0.5)
dim=rsz_Img.shape
img_h=dim[0]
img_w=dim[1]
images=list()
if (im=="2"):
    img1=rsz_Img[0:img_h,0:int(2*img_w/3)]
    img2=rsz_Img[0:img_h,int(img_w/6):img_w]
    images=[img1,img2]
    cv2.imshow("left",img1)
    cv2.imshow("right",img2)
    cv2.waitKey(0)
elif(im=="m"):
    n=5
    for i in range(n):
        ih=img_w/(2*n)
        ir=ih
        if i==0:
            ih=0
        elif(i==(n-1)):
            ir=0
        i1=int((i*img_w/(n))-ih)
        i2=int(((i+1)*img_w/n)+ir)
        currImg=rsz_Img[0:img_h,i1:i2]
        images.append(currImg)
        cv2.imshow(f"{i}",currImg)
        cv2.waitKey(0)
t1=time.time()
stitcher=cv2.Stitcher.create()
(status,result)=stitcher.stitch(images)
t2=time.time()
if(status==cv2.STITCHER_OK):
    print("done")
else:
    print('No')
#cv2.imshow("original",img)
cv2.imshow("rsz",rsz_Img)
cv2.imshow("Result",result)
print(t2-t1)
cv2.waitKey(0)
#plt.imsave("Rsz.png",cv2.cvtColor(rsz_Img,cv2.COLOR_BGR2RGB))
#plt.imsave("Left.png",cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
#plt.imsave("Right.png",cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
#plt.imsave("Result.png",cv2.cvtColor(result,cv2.COLOR_BGR2RGB))
