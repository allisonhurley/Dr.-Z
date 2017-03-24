import cv2
import numpy as np

def normalize(a):
    return (a-np.min(a))/(np.max(a)-np.min(a))

class LaneMarkersModel():
    def __init__(self):
        self.avgRGB = [ 0.8888889,   0.99607843,  0.98823529 ]
        self.avgHSV = [ 1.75261841e+02,   1.07563006e-01,   9.96078432e-01 ]
        self.lineProbabilityMap = 0
        self.initialPoints = []

    def UpdateModelFromMask(self, mask, img, hsv):
        self.avgRGB = cv2.mean(img, mask)[0:3]
        self.avgHSV = cv2.mean(hsv, mask)[0:3]
        distMap = cv2.distanceTransform(1-mask, cv2.cv.CV_DIST_L2, 5)[0]
        self.lineProbabilityMap = (1.0/(1.0+0.1*distMap))
        print self.avgRGB 
        print self.avgHSV 
        #cv2.imshow('test',self.lineProbabilityMap)
        #cv2.waitKey(1)
    
    def InitializeFromImage(self, img, windowName):
        cv2.imshow(windowName, img)
        cv2.setMouseCallback(windowName, self.AddPoint, [img, windowName])
        cv2.waitKey(0)
        
        #calculate average lane color
        hsv = np.float32(cv2.cvtColor(img, cv2.COLOR_RGB2HSV))
        
        if len(self.initialPoints)>0:
            flooded = np.uint8(img*255)
            largeMask = np.zeros((img.shape[0]+2, img.shape[1]+2), np.uint8)
            largeMask[:] = 0
            lo = 20
            hi = 20
            flags = cv2.FLOODFILL_FIXED_RANGE
            cv2.floodFill(flooded, largeMask, (self.initialPoints[0][1], self.initialPoints[0][0]), (0, 255, 0), (lo,), (hi,), flags)
            mask = largeMask[1:largeMask.shape[0]-1, 1:largeMask.shape[1]-1]
            cv2.imshow(windowName, mask*255)
            self.UpdateModelFromMask(mask, img, hsv)
        cv2.destroyWindow(windowName)

    def AddPoint(self, event, x, y, flags, data):
        if event & cv2.EVENT_LBUTTONUP:
            #print x, y, data[0][y, x]
            self.initialPoints.append([y, x])
            imgWithLines = data[0]
            '''
            if len(self.initialPoints)>1:
                cv2.line(imgWithLines, (self.initialPoints[0][1], self.initialPoints[0][0]), (self.initialPoints[1][1], self.initialPoints[1][0]), [0,1,0], 2)
            if len(self.initialPoints)>3:
                cv2.line(imgWithLines, (self.initialPoints[2][1], self.initialPoints[2][0]), (self.initialPoints[3][1], self.initialPoints[3][0]), [0,1,0], 2)
            '''
            flooded = np.uint8(imgWithLines*255)
            mask = np.zeros((imgWithLines.shape[0]+2, imgWithLines.shape[1]+2), np.uint8)
            mask[:] = 0
            lo = 20
            hi = 200
            flags = cv2.FLOODFILL_FIXED_RANGE
            cv2.floodFill(flooded, mask, (self.initialPoints[0][1], self.initialPoints[0][0]), (0, 255, 0), (lo,)*3, (hi,)*3, flags)
            cv2.imshow(data[1], mask*255)
            
            

if __name__ == '__main__':
    img = cv2.imread("C:\Users\mmuno\Documents\opencv\sources\samples\data\lena.jpg")
    test = LaneMarkersModel()
    test.InitializeFromImage(np.float32(img)/255.0, 'test')
