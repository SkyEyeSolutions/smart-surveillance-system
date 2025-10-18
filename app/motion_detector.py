import cv2

class MotionDetector:
    def __init__(self, min_area=500, threshold=244, debug=False, learning_rate=-1):
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2()
        self.min_area = min_area
        self.threshold = threshold
        self.debug = debug
        self.learning_rate = learning_rate

    def detect(self, frame):
        fg_mask = self.bg_subtractor.apply(frame, learningRate=self.learning_rate)
        _, thresh = cv2.threshold(fg_mask, self.threshold, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motion_contours = []
        for cnt in contours:
            if cv2.contourArea(cnt) >= self.min_area:
                motion_contours.append(cnt)
                if self.debug:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        has_motion = bool(motion_contours)
        return has_motion, motion_contours

