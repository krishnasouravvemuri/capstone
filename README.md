# 🎓 Capstone Project — Emotion-Based Media Recommendation

This is a **Django-based web application** that uses **emotion detection** through facial analysis to recommend **music or movies** based on the user's current emotion.

The system integrates **OpenCV** and **DeepFace** for emotion detection, and offers a simple frontend interface for capturing emotions and showing personalized suggestions.

---

## 🚀 Features

* 🧠 Real-time emotion detection using webcam
* 🎵 Recommends media (music or movies) based on emotion
* 🎨 Responsive UI built with Django templates
* ⚙️ Modular design — detection, frontend, and recommender separated

---

## 🏗️ Project Structure

```
capstone/
├── CapstoneProject/
│   ├── CapstoneProject/         # Core Django config (settings, URLs, wsgi, etc.)
│   ├── detection/               # Emotion detection & recommendation logic
│   ├── frontend/                # UI templates and views
│   ├── manage.py                # Django management script
├── requirements.txt             # Python dependencies
└── .gitignore                   # Ignored files (venv, db, etc.)
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/krishnasouravvemuri/capstone.git
cd capstone
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Development Server

```bash
python manage.py runserver
```

Then open your browser and visit:
👉 `http://127.0.0.1:8000/`

---

## 🧠 Emotion Detection Flow

1. Open the camera interface.
2. The system detects your face and predicts your **emotion** using DeepFace.
3. You’ll be prompted to choose between **Music** or **Movies**.
4. The app recommends content matching your emotional state.

---

## 🧩 Tech Stack

| Layer                 | Tools / Libraries     |
| :-------------------- | :-------------------- |
| **Backend**           | Django, Python        |
| **Frontend**          | HTML, CSS, JavaScript |
| **Emotion Detection** | OpenCV, DeepFace      |
