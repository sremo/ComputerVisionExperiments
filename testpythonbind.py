import cv2.cv as cv
import time

cv.NamedWindow("camera", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)


def repeat():
    frame = cv.QueryFrame(capture)
    cv.ShowImage("camera", frame)


loopCondition = True

while loopCondition:
    repeat()
    if cv.WaitKey(10) == 27:
        break

cv.DestroyWindow("camera")


