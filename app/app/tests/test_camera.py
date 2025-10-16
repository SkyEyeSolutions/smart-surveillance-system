from app.camera import VideoCamera

def test_camera_init():
    cam = VideoCamera(0)
    assert cam is not None
