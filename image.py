import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("test.jpg")
dim=img.shape
img_h=dim[0]
img_w=dim[1]
img1=img[450:img_h,0:img_w]
dim1=img1.shape
img1_h=dim1[0]
img1_w=dim1[1]
res_h,res_w=1920,1080
hor_w=int(87*res_w/123)/2
ver_w=int(264*res_h/312)/2
hor_h=int((res_h-ver_w)/2)#148
ver_h=int((res_w-hor_w)/2)#158
src1 = np.float32([[0, img1_h], [img1_w, img1_h], [0, 0], [img1_w, 0]])
dst1 = np.float32([[ver_h, hor_h], [ver_h+hor_w, hor_h], [0, 0], [res_w, 0]])
M1 = cv2.getPerspectiveTransform(src1, dst1)
warped_img1=cv2.warpPerspective(img1,M1,(res_w,hor_h))
src2 = np.float32([[0, img1_h], [img1_w, img1_h], [0, 0], [img1_w, 0]])
dst2 = np.float32([[hor_h, ver_h], [hor_h+ver_w, ver_h], [0, 0], [res_h, 0]])
M2 = cv2.getPerspectiveTransform(src2, dst2)
warped_img2=cv2.warpPerspective(img1,M2,(res_h,ver_h))
img_T=warped_img1
img_L=cv2.rotate(warped_img2, cv2.ROTATE_90_COUNTERCLOCKWISE)
img_R=cv2.rotate(warped_img2, cv2.ROTATE_90_CLOCKWISE)
img_B=cv2.rotate(warped_img2, cv2.ROTATE_180)
bg_T=np.zeros((res_h,res_w,3),np.uint8)
bg_L=np.zeros((res_h,res_w,3),np.uint8)
bg_R=np.zeros((res_h,res_w,3),np.uint8)
bg_B=np.zeros((res_h,res_w,3),np.uint8)
bg_T[0:hor_h,0:res_w]=img_T
bg_L[0:res_h,0:ver_h]=img_L
bg_R=cv2.rotate(bg_L,cv2.ROTATE_180)
bg_B=cv2.rotate(bg_T,cv2.ROTATE_180)
f1=cv2.add(bg_T,bg_B)
f2=cv2.add(bg_L,bg_R)
final=cv2.add(f1,f2)
plt.imshow(cv2.cvtColor(final,cv2.COLOR_BGR2RGB))
#plt.imsave("New_Final.png",final)
plt.show()
#cv2.imshow("New",final)
cv2.waitKey(0)
