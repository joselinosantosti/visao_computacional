import cv2

camera = cv2.VideoCapture(0)
while(1):
    ret, frame = camera.read()
    cv2.imshow("Video", frame)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
camera.release()
cv2.destroyAllWindows()