# Hand Gesture Recognition using OpenCV & MediaPipe  

This project uses OpenCV and MediaPipe to detect hand gestures in real-time via a webcam. It recognizes **Thumbs Up, Peace Sign, and Open Palm** gestures accurately.  

## 🚀 Features  
- **Real-time hand tracking** using MediaPipe Hands  
- **Detects multiple hand gestures**: Thumbs Up, Peace Sign, Open Palm  
- **Displays gesture name** directly on the screen  
- **Mirrored Camera Feed** for a natural user experience  

## 🛠 Installation  
Make sure you have Python installed. Then, install the required dependencies:  

```bash
pip install opencv-python mediapipe numpy
## 🎯 How to Run the Project  

### Clone the Repository:  
```bash
git clone https://github.com/your-username/hand-gesture-recognition.git
cd hand-gesture-recognition
### 📌 How It Works
Hand Detection: Uses MediaPipe Hands to track hand landmarks.
Gesture Recognition: Determines gestures based on fingertip positions.
Text Display: The detected gesture name appears on the screen.
### 🖐 Recognized Gestures
Gesture	Condition
Thumbs Up	Thumb up, other fingers curled
Peace Sign	Index & Middle fingers up, others down
Open Palm	All fingers extended

### 🔥 Future Improvements
Add more gestures (e.g., Fist, Okay Sign)
Integrate voice output for detected gestures
Create a GUI for better user experience
