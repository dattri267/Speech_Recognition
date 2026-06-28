# Speech Emotion Recognition using CNN

A full-stack Deep Learning web application that recognizes human emotions from speech using a Convolutional Neural Network (CNN). Users can record their voice directly in the browser, and the application predicts the underlying emotion in real time using MFCC feature extraction and a trained CNN model.

---

## Overview

This project combines Deep Learning, Digital Signal Processing, and Web Development into a single application. The frontend captures audio through the browser, while the Flask backend processes the recording, extracts MFCC features, performs emotion classification using a CNN, and returns the predicted emotion with a confidence score.

---

## Features

- Browser-based voice recording
- Audio playback before prediction
- Automatic WebM to WAV conversion using FFmpeg
- MFCC feature extraction with Librosa
- CNN-based speech emotion classification
- Confidence score visualization
- Responsive and modern user interface
- Flask REST API backend

---

## Supported Emotions

- Angry
- Disgust
- Fear
- Happy
- Neutral
- Pleasant Surprise
- Sad

---

## Application Workflow

```
User Speaks
      │
      ▼
Browser Records Audio
      │
      ▼
Frontend Sends Audio to Flask
      │
      ▼
Convert WebM → WAV (FFmpeg)
      │
      ▼
MFCC Feature Extraction
      │
      ▼
CNN Model Prediction
      │
      ▼
Emotion + Confidence
      │
      ▼
Display Result on Website
```

---

## Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Flask
- TensorFlow / Keras
- Librosa
- NumPy
- Scikit-learn
- FFmpeg

---

## Project Structure

```
Speech_Recognition/
│
├── backend/
│   ├── app.py
│   ├── best_cnn_model.keras
│   ├── encoder.pkl
│   ├── uploads/
│   └── utils/
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── templates/
│       └── index.html
│
├── notebook/
│   └── Emotion_Recognitionmodel.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Speech-Emotion-Recognition.git
```

### 2. Navigate to the project

```bash
cd Speech-Emotion-Recognition
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install FFmpeg

Download and install FFmpeg, then ensure it is added to your system PATH.

### 7. Run the application

```bash
python backend/app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Screenshots

### Home Page

_Add a screenshot here_

### Voice Recorder

_Add a screenshot here_

### Prediction Result

_Add a screenshot here_

---

## Future Improvements

- Improve model accuracy using larger datasets
- Support multilingual emotion recognition
- Display probability distribution for all emotions
- Add waveform and spectrogram visualization
- Deploy the application using Render or Railway
- Optimize the model for faster inference

---

## Learning Outcomes

This project helped me gain practical experience with:

- Deep Learning model deployment
- Speech signal processing
- MFCC feature extraction
- CNN inference using TensorFlow
- Flask backend development
- REST API integration
- Browser audio recording using JavaScript
- Frontend and backend communication

---

## Author

**Diya Attri**

Built as a Machine Learning and Full Stack AI deployment project using Flask and TensorFlow.

<img width="1237" height="723" alt="Screenshot 2026-06-28 232935" src="https://github.com/user-attachments/assets/fdc0925f-35b3-4757-a11b-289d4c2dca23" />
