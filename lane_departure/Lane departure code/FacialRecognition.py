import cv2
from VideoProcessor import LaneDeparture
def FacialRecognition():
    eyeCascade = cv2.CascadeClassifier('C:\Users\mmuno\Documents\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier('C:\Users\mmuno\Documents\opencv\sources\data\haarcascades_cuda\haarcascade_eye.xml')
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.rectangle(frame, (150, 50), (500, 400), (0, 0, 255), 2)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor= 1.1,
            minNeighbors=5,
            minSize=(30,30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y), (x+w, y+h), (255, 0, 0), 2)
            
        eyes = eyeCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        
        
        for (x,y,w,h) in eyes:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    video_capture.release()
    cv2.destroyAllWindows()