import cv2
from LaneMarkersModel import LaneMarkersModel
from LaneMarkersModel import normalize
import numpy as np
from Sensor import LaneSensor
from LineDetector import LineDetector
import sys

def facial():
    eyeCascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_default.xml')
    faceCascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades_cuda\haarcascade_eye.xml')
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
#Initialize video input
facial()
#stream = cv2.VideoCapture(0) #6 7 8
stream = cv2.VideoCapture('C:/Users/michael/OneDrive/Visteon/ldwNight.avi') #6 7 8
if stream.isOpened() == False:
    print "Cannot open input video"
    sys.exit()

#Initialize video writing
videoWriter = cv2.VideoWriter('out7Test1.avi', cv2.cv.CV_FOURCC('M','J','P','G'), 30, (640, 480), 1)

#some image processing parameters
#cropArea = [0, 128, 637, 298]
#cropArea = [0,275,720,448] #3rd value controls green line length? 1st value controls x-offset from left side? 2nd value controls y-offset from the top?
cropArea = [100,150,800,448] 
sensorsNumber = 50
sensorsWidth = 70

#6L
line1LStart = np.array([50, 172])#first value is x-offset, second value is y-offset
line1LEnd = np.array([250, 32])
#6R
line1RStart = np.array([520, 146])
line1REnd = np.array([320, 11])

#7L
#line1LStart = np.array([71, 163])
#line1LEnd= np.array([303, 3])

#get first frame for color model
flag, imgFull = stream.read()
img = imgFull[cropArea[1]:cropArea[3], cropArea[0]:cropArea[2]]

#Initialize left lane
leftLineColorModel = LaneMarkersModel()
leftLineColorModel.InitializeFromImage(np.float32(img)/255.0, "Select left line")
leftLine = LineDetector(cropArea, sensorsNumber, sensorsWidth, line1LStart, line1LEnd, leftLineColorModel)

#Initialize right lane
rightLineColorModel = LaneMarkersModel()
rightLineColorModel.InitializeFromImage(np.float32(img)/255.0, "Select right line")
rightLine = LineDetector(cropArea, sensorsNumber, sensorsWidth, line1RStart, line1REnd, rightLineColorModel)

frameNumber = 0
while(cv2.waitKey(1) != 27):
    frameNumber+=1
    print frameNumber
    #read and crop
    flag, imgFull = stream.read()
    if flag == False: break #end of video

    #do some preprocessing to share results later
    img = np.float32(imgFull[cropArea[1]:cropArea[3], cropArea[0]:cropArea[2]])/255.0
    hsv = np.float32(cv2.cvtColor(img, cv2.COLOR_RGB2HSV))
    canny = cv2.Canny(cv2.cvtColor(np.uint8(img*255), cv2.COLOR_RGB2GRAY), 70, 170)
 
    #make output images
    outputImg = img.copy()
    outputFull = imgFull.copy()

    #process frame
    leftLine.ProcessFrame(img, hsv, canny, outputImg, outputFull)
    rightLine.ProcessFrame(img, hsv, canny, outputImg, outputFull)
    
    #show output
    cv2.imshow("Output", outputImg)
    cv2.imshow("Output full", outputFull)
    
    #write output
    videoWriter.write(outputFull)
    
cv2.destroyAllWindows()


