import cv2
from LaneMarkersModel import LaneMarkersModel
from LaneMarkersModel import normalize
import numpy as np
from Sensor import LaneSensor
from LineDetector import LineDetector
import sys

#Initialize video input
stream = cv2.VideoCapture(2) #6 7 8
#stream = cv2.VideoCapture('C:/Users/mmuno/Visteon/ldw.avi') #6 7 8
if stream.isOpened() == False:
    print "Cannot open input video"
    sys.exit()

#Initialize video writing
#videoWriter = cv2.VideoWriter('out7Test1.avi', cv2.cv.CV_FOURCC('M','J','P','G'), 30, (1280, 720), 1)

#some image processing parameters
#cropArea = [0, 128, 637, 298]
cropArea = [0,275,1080,448] #3rd value controls green line length? 1st value controls x-offset from left side? 2nd value controls y-offset from the top?
sensorsNumber = 50
sensorsWidth = 70

#6L
#line1LStart = np.array([35, 172])
line1LStart = np.array([35, 172])
line1LEnd = np.array([172, 32])
#6R
line1RStart = np.array([632, 146])
line1REnd = np.array([476, 11])

#7L
#line1LStart = np.array([71, 163])
#line1LEnd= np.array([303, 3])

#get first frame for color model
flag, imgFull = stream.read()
img = imgFull[cropArea[1]:cropArea[3], cropArea[0]:cropArea[2]]

#Initialize left lane
leftLineColorModel = LaneMarkersModel()
#leftLineColorModel.InitializeFromImage(np.float32(img)/255.0, "Select left line")
leftLine = LineDetector(cropArea, sensorsNumber, sensorsWidth, line1LStart, line1LEnd, leftLineColorModel)

#Initialize right lane
rightLineColorModel = LaneMarkersModel()
#rightLineColorModel.InitializeFromImage(np.float32(img)/255.0, "Select right line")
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
    #videoWriter.write(outputFull)
    
cv2.destroyAllWindows()
