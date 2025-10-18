motion_detector = MotionDetector(min_area=500)
recorder = MotionRecorder(camera_source=0)

while True:
    ret, frame = recorder.camera.read()
    if not ret:
        break
    has_motion, _ = motion_detector.detect(frame)
    recorder.process_frame(frame, has_motion)

recorder.release()


