import cv2.cv as cv
import time
import glob

class FaceDetection:
    _cascades = []
    def __init__(self):
        for xmlfile in glob.glob("haarcascade_frontalface_default.xml"):
            self._cascades.append((xmlfile, cv.Load(xmlfile)))
  
    def processImage(frame):
        #grayframe = cv.CreateImage((frame.width, frame.height), cv.IPL_DEPTH_8U, 1)
        #cv.CvtColor(frame, grayframe, cv.CV_BGR2GRAY)
        #cv.EqualizeHist(grayframe, grayframe)
        #return grayframe

    def detectFace(frame):
        # create storage
        storage = cv.CreateMemStorage(0)
        #cv.ClearMemStorage(storage)
        for item in self._cascades:
            k, cascade = item
            faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (50, 50))
        cv.ClearMemStorage(storage)
        return faces

    def overlay(frame, faces):
        for (x,y,w,h),n in faces:
            cv.Rectangle(frame, (x,y), (x+w,y+h), 255)
        return frame
        

def repeat(cls):
    frame = cv.QueryFrame(capture)
    procFrame = cls.processImage(frame)
    faces = cls.detectFace(procFrame)
    overlaid = cls.overlay(procFrame, faces)
    cv.ShowImage("MyFace", overlaid)
 
#def repeat():
#    frame = cv.QueryFrame(capture)
#    grayframe = cv.CreateImage((frame.width, frame.height), cv.IPL_DEPTH_8U, 1)
#    equalized = cv.CreateImage((grayframe.width, grayframe.height), cv.IPL_DEPTH_8U, 1)
#    cv.CvtColor(frame, grayframe,cv.CV_BGR2GRAY)
#    cv.ShowImage("camera", frame)
#    cv.ShowImage("grayscale",grayframe)
#    cv.EqualizeHist(grayframe, equalized)
#    cv.ShowImage("equalized", equalized)
#            storage = cv.CreateMemStorage(0)


if __name__ == "__main__":
    cv.NamedWindow("MyFace", cv.CV_WINDOW_AUTOSIZE)
    capture = cv.CaptureFromCAM(0)
    cls = FaceDetection()
    loop = True
    while loop:
        frame = cv.QueryFrame(capture)
        #procFrame = cls.processImage(frame)
        #faces = cls.detectFace(procFrame)
        #overlaid = cls.overlay(procFrame, faces)
        #cv.ShowImage("MyFace", overlaid)
        cv.ShowImage("MyFace", frame)
        if cv.WaitKey(50) == 27:
            break
    cv.DestroyWindow("MyFace")
