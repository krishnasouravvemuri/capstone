# detection/emotion_detector.py
import os
import time
import cv2
import numpy as np
from deepface import DeepFace
from collections import Counter

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Load OpenCV face detector once
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def analyze_emotion_live():
    """
    Captures frames for 2.5 seconds and detects dominant emotion using DeepFace.
    Returns overall dominant emotion and last known bounding boxes.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Unable to access webcam")
        return {"dominant_emotion": "Camera Error", "faces": []}

    start_time = time.time()
    emotions, boxes = [], []

    while (time.time() - start_time) < 2.5:
        ret, frame = cap.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected_faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(80, 80))

        for (x, y, w, h) in detected_faces:
            face_roi = frame[y:y+h, x:x+w]
            try:
                result = DeepFace.analyze(
                    face_roi,
                    actions=['emotion'],
                    enforce_detection=False,
                    silent=True,
                    detector_backend='opencv'
                )
                if isinstance(result, list):
                    result = result[0]

                emotion = result['dominant_emotion']
                confidence = result['emotion'][emotion]

                if confidence > 40:
                    emotions.append(emotion)
                    boxes.append({
                        "x": int(x),
                        "y": int(y),
                        "w": int(w),
                        "h": int(h),
                        "emotion": emotion
                    })

            except Exception as e:
                print(f"[WARN] Face processing failed: {e}")
                continue

    cap.release()
    cv2.destroyAllWindows()

    if emotions:
        dominant = Counter(emotions).most_common(1)[0][0]
    else:
        dominant = "No Faces Detected"

    return {
        "dominant_emotion": dominant,
        "faces": boxes
    }

if __name__ == "__main__":
    result = analyze_emotion_live()
    print(result)
