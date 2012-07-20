import cv2.cv as cv
import time

cv.NamedWindow("camera", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("grayscale", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)




def repeat():
    frame = cv.QueryFrame(capture)
    grayframe = cv.CreateImage((frame.width, frame.height), cv.IPL_DEPTH_8U, 1)
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

