import cv2
import numpy as np
import imutils
import time
import pyautogui
# object tracking video 

cap=cv2.VideoCapture(0)
cnt=None
while(1):
	_,img=cap.read()
	img=cv2.flip(img,1)
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	height, width = img.shape[:2]
	# res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
	# define range of blue color in HSV
	lower_red = np.array([161, 155, 84])
	upper_red = np.array([179, 255, 255])
	low_blue = np.array([94, 80, 2])
	high_blue = np.array([126, 255, 255])
	threshold=cv2.inRange(hsv,lower_red,upper_red)
	threshold2=cv2.inRange(hsv,low_blue,high_blue)
	cv2.line(img,(0,int(height/2)),(int(width),int(height/2)),(0,255,0),5)
	cv2.line(img,(int(width/2),0),(int(width/2),int(height)),(255,0,0),5)
	contours,hierarchy=cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	maximum=0
	if contours:

		for i in contours:
			area = cv2.contourArea(i)
			if area > maximum:
				maximum = area
				cnt=i

		x,y,w,h = cv2.boundingRect(cnt)
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		centroid_x = (x + x+w)/2
		centroid_y = (y + y+h)/2			
		
		temp=(height/2)-centroid_y
		if temp>h:
			print("up")
			pyautogui.press('up')
		elif temp<(-h):
			pyautogui.press('down')	
			

	contours2,hierarchy=cv2.findContours(threshold2,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	maximum2=0		
	if contours2:

		for i in contours2:
			area = cv2.contourArea(i)
			if area > maximum2:
				maximum2 = area
				cnt=i

		x,y,w,h = cv2.boundingRect(cnt)
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		centroid_x = (x + x+w)/2
		centroid_y = (y + y+h)/2
		temp=(width/2)-centroid_x
		if temp>w or temp<(-w):
			print("tab")
			pyautogui.hotkey('alt','tab')



	cv2.imshow("img",img)		

	# cv2.line(img,(0,0),(int(centroid_x),int(centroid_y)),(0,0,255),5)

	# cv2.line(img,(0,int(centroid_y)),(800,int(centroid_y)),(255,0,0),5)

	


	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break


cv2.destroyAllWindows()

cap.release()
