#Read A Video Stream From Camera(Frame by Frame)
import cv2

#First step
#To capture the device from which we read the frame
#If it is zero it is the default webcam and for other change id

cap = cv2.VideoCapture(0)

while True:

	#This .read returns two values from webcam the frame i.e image :- frame
	#and boolean value is the image captured or not :- ret
	ret,frame = cap.read()

	#to convert the image into gray scale image
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	#Just add an extra imshow method passing gray_frame and get the gray_frame

	#Multiple reason camera crashes or camera isnt loaded properly
	#So we simply continue
	if ret == False:
		continue

	cv2.imshow("Video Frame",frame)

	#Waits for user input
	#Suppose user press q, then you will stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break;	

	#Here we have taken & with 0xFF because the key_pressed returns a 32 bit value but
	#the ascii value of q lies with 0-255 i.e 8 bit . So we convert it into 8 bit.
	#ord('q') gives the ASCII value of q	

cap.release()
cv2.destroyAllWindows() 