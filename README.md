# Smart Surveillance System by Pion Tech FZE

A professional, company-grade solution for real-time video streaming and analysis. Developed by Pion Tech FZE, this platform delivers advanced security features for businesses and organizations.

## Features
- Real-time video streaming from multiple cameras
- Motion detection and event alerts
- Event recording with timestamped logs
- User-friendly web interface for camera management
- Modular design for easy expansion
- Basic data privacy and access control (planned)
- Adjustable motion detection sensitivity with min_area parameter
- Debug mode for visualizing motion contours
- Dynamic camera source switching
- Ability to save captured frames locally
- Improved error handling and reinitialization logic

## Quick Start
git clone https://github.com/SkyEyeSolutions/smart-surveillance-system.git 
cd smart-surveillance-system 
pip install -r requirements.txt
python app/web_server.py

Open http://localhost:8080/video_feed in your browser.

## Usage Example
from app.camera import VideoCamera
from app.motion_detector import MotionDetector
camera = VideoCamera(0) 
motion_detector = MotionDetector(min_area=500, debug=True)
while True: 
frame = camera.video.read() 
has_motion, contours = motion_detector.detect(frame) if has_motion:
print(“Motion detected!”) camera.save_frame()


## Configuration

MotionDetector parameters:

- `min_area`: Minimum object size to trigger motion detection (default 500)
- `threshold`: Motion detection intensity (default 244)
- `learning_rate`: Background learning rate for stability
- `debug`: Enables contour visualization for testing

## Development Roadmap
- Multi-camera management improvements
- Advanced motion/event recognition
- Role-based access control
- Cloud archiving support
- Added debug mode and noise filtering to MotionDetector (v1.1)
- Enhanced VideoCamera with dynamic source control and frame saving

