import cv2
import datetime

class VideoCamera:
    def __init__(self, source=0):
        self.video = cv2.VideoCapture(source)
        self.source = source
        print(f"[INFO] Camera initialized with source: {self.source}")

    def __del__(self):
        if hasattr(self, 'video') and self.video.isOpened():
            self.video.release()
            print("[INFO] Camera released.")

    def get_frame(self):
        if not hasattr(self, 'video') or not self.video.isOpened():
            print("[WARNING] Camera not initialized or opened. Attempting to reinitialize.")
            self.video = cv2.VideoCapture(self.source)
            if not self.video.isOpened():
                print("[ERROR] Unable to open video source.")
                return None
        success, image = self.video.read()
        if not success:
            print("[ERROR] Failed to read frame from source.")
            return None
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def set_source(self, new_source):
        if hasattr(self, 'video') and self.video.isOpened():
            self.video.release()
        self.video = cv2.VideoCapture(new_source)
        self.source = new_source
        print(f"[INFO] Camera source changed to: {self.source}")

    def save_frame(self, filename=None):
        if not hasattr(self, 'video') or not self.video.isOpened():
            print("[ERROR] Camera not available for saving frame.")
            return False
        success, image = self.video.read()
        if not success:
            print("[ERROR] Could not read frame for saving.")
            return False
        if filename is None:
            filename = f"frame_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, image)
        print(f"[INFO] Frame saved as {filename}")
          return True
      
