# Hand Voice: Finger Gesture to Speech

A simple computer vision project that detects hand gestures from a webcam and converts them into spoken Indonesian phrases using text-to-speech.

## Features

- Real-time hand detection using MediaPipe Hands.
- Finger gesture recognition based on finger up/down states.
- Maps specific finger combinations to predefined Indonesian phrases.
- Text-to-speech output using gTTS (Google Text-to-Speech).
- Audio playback via `playsound`.
- Cool mirror-like camera view (frame is flipped horizontally).

## Tech Stack

- **Language:** Python
- **Computer Vision:** OpenCV
- **Hand Tracking:** MediaPipe
- **Text-to-Speech:** gTTS
- **Audio Playback:** playsound

## How It Works

1. The app captures frames from the webcam using OpenCV.
2. Each frame is:
   - Flipped horizontally (mirror effect).
   - Passed to MediaPipe Hands for hand landmark detection.
3. For each detected hand:
   - It checks the state (up/down) of fingers using specific landmark indices.
   - Creates a binary pattern like `[1, 0, 0, 0, 0]` indicating which fingers are up.
4. If a known pattern is detected and at least 3 seconds have passed since the last trigger:
   - It generates a speech audio file (in Indonesian) using gTTS.
   - Plays the audio using `playsound`.
5. The app exits when you press the `q` key.

### Gesture to Phrase Mapping

Current gesture mappings:

- `[1, 0, 0, 0, 0]` → **"halo"**
- `[0, 1, 0, 0, 0]` → **"perkenalkan"**
- `[0, 1, 1, 0, 0]` → **"aku"**
- `[1, 1, 1, 1, 1]` → **"Renatha Putri"**

You can customize these phrases in the code inside the `if finger_up == [...]` blocks.

## Getting Started

### Prerequisites

Make sure you have:

- Python 3.8+ installed
- A working webcam
- Internet connection (required by gTTS to generate speech)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/hand-voice.git
cd hand-voice
````

2. (Recommended) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install opencv-python mediapipe gTTS playsound==1.2.2
```

> Note: Some systems may require additional backend packages for audio playback.

### Running the App

Run the script:

```bash
python main.py
```

(or adjust the filename if you use a different name.)

* A window named `Hand Voice` will open.
* Show your hand in front of the webcam.
* Use one of the predefined gestures.
* The corresponding phrase will be spoken aloud.
* Press `q` to quit.

## File Overview

Main script (example: `main.py`) contains:

* Webcam capture setup (`cv2.VideoCapture(0)`).
* MediaPipe Hands initialization.
* Gesture detection logic.
* `speak(text)` function:

  * Generates `temp.mp3` using gTTS.
  * Plays the file using `playsound`.
  * Deletes the file after playback.

## Limitations

* Requires a stable internet connection for gTTS.
* Only supports predefined gestures and phrases (no dynamic mapping yet).
* Single-hand detection logic (focused on simple use cases).
* Uses a simple rule-based finger detection (no machine learning model training).

## Possible Improvements / Roadmap

* Add more gestures and phrases.
* Add on-screen text showing the detected phrase.
* Support multiple output languages (EN/ID switch).
* Build a small GUI to manage phrases.
* Replace gTTS with an offline TTS engine for fully offline usage.
