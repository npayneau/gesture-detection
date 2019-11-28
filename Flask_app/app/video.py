import cv2

class Video:
    def __init__(self):
        self.cap=cv2.VideoCapture(0)

    def get_frame(self):
        _,self.frame=self.cap.read()
        ret, jpeg = cv2.imencode('.jpg', self.frame)
        return jpeg.tobytes()

if __name__ == '__main__':
    vid = Video()
