from app.motion_detector import MotionDetector
import cv2
import numpy as np

def test_motion_detector_init():
    md = MotionDetector()
    assert md is not None

def test_detect_no_frame(monkeypatch):
    # простий тест, коли немає кадру
    md = MotionDetector()
    frame = None
    has_motion, contours = md.detect(frame)
    assert has_motion is False
