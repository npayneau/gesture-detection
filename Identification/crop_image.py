import cv2
import numpy as np

def crop_current_image():
    # Read image
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Select ROI
    r = cv2.selectROI(frame)

    cv2.destroyAllWindows()
    cap.release()

    return int(r[1]), int(r[1] + r[3]), int(r[0]), int(r[0] + r[2])