# Translating Silence: Sign Language to Text Converter


## 📜 Abstract
This project bridges the communication gap between sign language users and non-signers by using computer vision and deep learning. It recognizes American Sign Language (ASL) gestures in real-time, converts them into text, and provides audio feedback. This system aims to enhance inclusivity and accessibility for the deaf and mute community.

---

## 🧐 Introduction
Sign language is vital for communication among the deaf and mute community, yet many non-signers find it difficult to understand. This project addresses this gap by translating hand gestures into text and speech in real-time using a CNN-based model.

---

## ✨ Features
- **Real-Time Gesture Recognition**: Captures and processes ASL gestures dynamically.
- **Text-to-Speech Output**: Converts recognized gestures into spoken words.
- **Spell Suggestions**: Provides word recommendations for correction and refinement.
- **User-Friendly GUI**: Displays recognized text and allows interaction.
- **Supports Backspace and Space Gestures**: Simplifies text editing during interaction.

---

## 🛠️ Technologies Used
- **Programming Language**: Python 3.9+
- **Libraries and Frameworks**:
  - OpenCV (Image Processing)
  - MediaPipe (Hand Tracking)
  - TensorFlow & Keras (Deep Learning)
  - NumPy (Data Manipulation)
  - pyttsx3 (Text-to-Speech)
  - Tkinter (GUI Development)
- **Hardware Requirements**:
  - Webcam (720p or above)
  - Intel Core i5 or higher processor
  - 8 GB RAM (minimum)

---

## 🚀 Installation

1. Clone the Repository
2. Set up a Virtual Environment(Python 3.9)
3. Install Dependencies
4. Use Pretrained Model/Train model using model.py
5. Run the Application:
   ```bash
   python final_prediction.py
   ```

---

## 🎮 Usage
1. Start the application and allow webcam access.
2. Perform an ASL gesture in front of the camera.
3. View the recognized text on the GUI.
4. Use additional controls to clear text, correct suggestions, or hear audio output.

---

## 📦 Modules

### 1. Data Collection (`collect_data.py`)
- Captures images of ASL gestures.
- Organizes data into labeled folders.

### 2. Dataset Preparation (`create_dataset.py`)
- Groups data into predefined gesture classes for training.

### 3. Model Training (`model.py`)
- Builds and trains a CNN for gesture classification.
- Outputs a trained model for real-time inference.

### 4. Real-Time Recognition (`final_prediction.py`)
- Uses the trained model to recognize gestures in real-time.
- Displays text and provides speech output.

---

### Accuracy
- **Overall Accuracy**: 96.26%
- **Robustness**: Tested across varied lighting conditions with acceptable performance.


🎥 Project Demonstration
For a complete walkthrough of the project, check out the demo video: final_demo.mp4
