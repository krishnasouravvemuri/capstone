# detection/emotion_detector.py
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import cv2
import numpy as np
from deepface import DeepFace
from collections import Counter

# Load more robust detector: Haar Cascade fallback
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def preprocess_image(frame):
    """Enhance brightness and normalize contrast before emotion analysis."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Use CLAHE to improve lighting contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced_gray = clahe.apply(gray)
    enhanced_frame = cv2.cvtColor(enhanced_gray, cv2.COLOR_GRAY2BGR)
    return enhanced_frame

def analyze_emotion(image_bytes):
    """
    Detect faces using Haar Cascade and predict emotion using DeepFace pretrained model.
    Returns dominant emotion + bounding boxes.
    """
    np_arr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if frame is None:
        print("[ERROR] Invalid image input")
        return {"dominant_emotion": "Invalid Image", "faces": []}

    # Preprocess to normalize lighting
    frame = preprocess_image(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80)
    )

    emotions, boxes = [], []

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]

        try:
            # ✅ Use a better backend for accuracy — 'retinaface' or 'mtcnn' (if installed)
            result = DeepFace.analyze(
                face_roi,
                actions=['emotion'],
                enforce_detection=False,
                silent=True,
                detector_backend='retinaface'  # much better face alignment
            )

            # DeepFace sometimes returns a list
            if isinstance(result, list):
                result = result[0]

            emotion = result['dominant_emotion']
            confidence = result['emotion'][emotion]

            # Slightly lower confidence threshold to avoid missing subtle emotions
            if confidence > 30:
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

    dominant = Counter(emotions).most_common(1)[0][0] if emotions else "No Faces Detected"

    return {
        "dominant_emotion": dominant,
        "faces": boxes
    }
