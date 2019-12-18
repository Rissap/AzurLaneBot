'''
import numpy as np
import cv2

#create gray image
image = cv2.imread("full.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("gray.jpg", gray)

#create edges
edged = cv2.Canny(gray, 10, 250)
cv2.imwrite("edged.jpg", edged)

#create closed contures
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("closed.jpg", closed)

#
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
total = 0
print(cnts)
'''
import cv2 
import numpy as np 

for num in range(10):
	# Read the main image 
	img_rgb = cv2.imread('full.jpg')
	  
	# Convert it to grayscale 
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
	  
	# Read the template 
	template = cv2.imread('button_confirm.png',0)
	  
	# Store width and height of template in w and h 
	w, h = template.shape[::-1] 
	  
	# Perform match operations. 
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
	  
	# Specify a threshold 
	threshold = 0.8
	  
	# Store the coordinates of matched area in a numpy array 
	loc = np.where( res >= threshold)  
	  
	# Draw a rectangle around the matched region. 
	for pt in zip(*loc[::-1]): 
	    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 
	  
	# Show the final image with the matched area. 
	cv2.imwrite('test_img/{}.jpg'.format(num),img_rgb) 

input()