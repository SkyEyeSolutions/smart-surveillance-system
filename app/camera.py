import cv2

class VideoCamera:
    def __init__(self, source=0):
        # source can be 0 for webcam or RTSP/HTTP URL for IP camera
        self.video = cv2.VideoCapture(source)

    def __del__(self):
        if hasattr(self, 'video') and self.video.isOpened():
            self.video.release()

    def get_frame(self):
        if not hasattr(self, 'video') or not self.video.isOpened():
            return None
        success, image = self.video.read()
        if not success:
            return None
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
