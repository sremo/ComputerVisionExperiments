import cv2.cv as cv
import time

cv.NamedWindow("camera", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("grayscale", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)

grayframe = cv.CreateImage((640, 480), cv.IPL_DEPTH_8U, 1)


def repeat():
    frame = cv.QueryFrame(capture)
    #edge1 = cvCreateImage(cvSize (frame.size[0], frame.size[1]), 32, 1)
    cv.CvtColor(frame, grayframe,cv.CV_BGR2GRAY)
    cv.ShowImage("camera", frame)
    cv.ShowImage("grayscale",grayframe)
   

loop = True

while loop:
    repeat()
    if cv.WaitKey(10) == 27:
        break

cv.DestroyWindow("camera")
cv.DestroyWindow("grayscale")

