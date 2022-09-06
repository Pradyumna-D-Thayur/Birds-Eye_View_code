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
src = np.float32([[0, img1_h], [img1_w, img1_h], [0, 0], [img1_w, 0]])
dst = np.float32([[569, img1_h], [711, img1_h], [0, 0], [img1_w, 0]])
M = cv2.getPerspectiveTransform(src, dst)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
plt.imsave("1.png",img1)
plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
plt.show()
#print(dim1)
#cv2.imshow("Test img",img)
warped_img=cv2.warpPerspective(img1,M,(img1_w,img1_h))
img_top=warped_img
img_left=cv2.rotate(img_top, cv2.ROTATE_90_COUNTERCLOCKWISE)
img_right=cv2.rotate(img_top, cv2.ROTATE_90_CLOCKWISE)
img_bot=cv2.rotate(img_top, cv2.ROTATE_180)
dim_top=img_top.shape
dim_left = img_left.shape
dim_right= img_right.shape
dim_bot= img_bot.shape
fin_h,fin_w,fin_ch =dim_top[1],dim_left[0],3
#print(fin_h)
bg1=np.zeros((fin_h,fin_w,fin_ch),np.uint8)
bg2=np.zeros((fin_h,fin_w,fin_ch),np.uint8)
bg3=np.zeros((fin_h,fin_w,fin_ch),np.uint8)
bg4=np.zeros((fin_h,fin_w,fin_ch),np.uint8)
bg1[0:dim_top[0],0:dim_top[1]]= img_top
bg2[0:dim_left[0],0:dim_left[1]]= img_left
bg3[0:dim_right[0],(dim_right[0]-dim_right[1]):dim_right[0]]=img_right
bg4[(dim_bot[1]-dim_bot[0]):dim_bot[1],0:dim_bot[1]]=img_bot
#print(img_top)
#print(bg1)
fin1=cv2.add(bg1,bg2)
fin2=cv2.add(bg3,bg4)
fin=cv2.add(fin1,fin2)
#res=cv2.cvtColor(fin,cv2.COLOR_BGR2RGB)
#cv2.imshow("bg1",bg1)
#cv2.imshow("bg2",bg2)
#cv2.imshow("bg3",bg3)
plt.imshow(cv2.cvtColor(fin,cv2.COLOR_BGR2RGB))
plt.show()
#cv2.imshow("bg4",bg4)
#cv2.imshow("roi",img1)
#cv2.imshow("warp",warped_img)
#cv2.imshow("res", fin)
cv2.waitKey(0)
