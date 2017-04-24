import cv2
import serial

faceCascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades_cuda\haarcascade_eye.xml')
video_capture = cv2.VideoCapture(0)
ser = serial.Serial('COM3', 115200, timeout = 1) 

def existance(array): 
    if len(str(array)) > 2 : 
        return True

    elif len(str(array)) <= 2: 
        return False

def drawRectangle(frame, array, color):
    for (x,y,w,h) in array:
            cv2.rectangle(frame,(x,y), (x+w, y+h), color, 2)

def testForObjects():
    while True: 
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=5, minSize=(200,200), flags=cv2.CASCADE_SCALE_IMAGE)
        drawRectangle(frame, faces, (255, 0, 0))
    
        eyes = eyeCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50), maxSize=(90, 90), flags=cv2.CASCADE_SCALE_IMAGE)
        drawRectangle(frame, eyes, (0, 255, 0))
        
        if existance(faces) and existance(eyes):
            ser.write("DIST_0\n") 
            print "DIST_0\n" + "DROWSY_0\n" 
        
        if existance(faces) and not existance(eyes): 
            print "DROWSY_1"

        if not existance(faces):
            ser.write("DIST_1\n")
            print "DIST_1"
        
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    video_capture.release()
    cv2.destroyAllWindows()

    
testForObjects()
