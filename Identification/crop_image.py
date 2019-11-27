import cv2
import numpy as np

def crop_current_image(camera=0):
    # Read image
    cap = cv2.VideoCapture(camera)
    ret, frame = cap.read()

    img = cv2.resize(frame, (1280, 1024))

    # Select ROI
    r = cv2.selectROI(img)


    cv2.destroyAllWindows()
    cap.release()

    return int(r[1]), int(r[1] + r[3]), int(r[0]), int(r[0] + r[2])