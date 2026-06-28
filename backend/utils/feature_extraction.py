import librosa
import numpy as np


def extract_mfcc(audio_path):
    """
    Extract MFCC features from an audio file.
    Returns features reshaped for the CNN model.
    """

    # Load audio
    y, sr = librosa.load(
        audio_path,
        duration=3,
        offset=0.5
    )

    # Extract MFCC features
    mfcc = librosa.feature.mfcc(
        y=y,
        sr=sr,
        n_mfcc=40
    )

    # Average over time axis
    mfcc = np.mean(mfcc.T, axis=0)

    # Reshape for CNN
    mfcc = mfcc.reshape(1, 40, 1)

    return mfcc