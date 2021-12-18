import cv2

face_cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
	_,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
		roi_gray = gray[y:y + h, x:x + w]
		roi_color = frame[y:y + h, x:x + w]
	cv2.imshow("Capture",frame)
	key = cv2.waitKey(1)
	if key == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()