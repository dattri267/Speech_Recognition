from flask import Flask, render_template, request, jsonify
import numpy as np
import subprocess
from tensorflow.keras.models import load_model
from utils.feature_extraction import extract_mfcc
import joblib
import os

# Flask Configuration
app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# Project Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
MODEL_PATH = os.path.join(BASE_DIR, "best_cnn_model.keras")
ENCODER_PATH = os.path.join(BASE_DIR, "encoder.pkl")

# Load Model
print("Loading CNN model...")
model = load_model(MODEL_PATH)
print("CNN model loaded successfully.")

# Load Label Encoder
print("Loading label encoder...")
encoder = joblib.load(ENCODER_PATH)
print(type(encoder))
print(encoder)
print("Label encoder loaded successfully.")


# Home Route
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():

    # Check whether an audio file was sent
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded."}), 400

    audio_file = request.files["audio"]

    if audio_file.filename == "":
        return jsonify({"error": "No file selected."}), 400

    # Save audio temporarily
   # Save uploaded WebM file
    webm_path = os.path.join(
        UPLOAD_FOLDER,
        "recording.webm"
    )

# Converted WAV file
    wav_path = os.path.join(
        UPLOAD_FOLDER,
        "recording.wav"
    )

    audio_file.save(webm_path)

# Convert WebM → WAV
    subprocess.run(
       [
          "ffmpeg",
          "-y",
          "-i",
          webm_path,
          wav_path
       ],
       check=True,
    )
    print("WAV Exists:", os.path.exists(wav_path))

    try:

    # Extract MFCC from WAV
        features = extract_mfcc(wav_path)

        print("Features shape:", features.shape)

    # CNN Prediction
        prediction = model.predict(features, verbose=0)
        print("Prediction shape:", prediction.shape)
        predicted_index = np.argmax(prediction)
        confidence = float(np.max(prediction) * 100)

        emotion = encoder.inverse_transform(prediction)[0][0]

        print("Prediction:", prediction)
        print("Predicted Index:", predicted_index)
        print("Emotion:", emotion)
        print("Confidence:", confidence)

        return jsonify({
            "emotion": emotion,
            "confidence": round(confidence, 2)
        })

    except Exception as e:
        import traceback
        traceback.print_exc()

        return jsonify({
          "error": str(e)
        }), 500

    finally:
        for file in [webm_path, wav_path]:

          if os.path.exists(file):

              try:
                  os.remove(file)

              except PermissionError:
                  pass
        

if __name__ == "__main__":
    app.run(debug=True)