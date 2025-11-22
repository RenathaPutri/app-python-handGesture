import cv2
import mediapipe as mp
import time
import os
from gtts import gTTS
from playsound import playsound
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)

last_trigger = 0

def speak(text):
    tts = gTTS(text=text, lang="id")
    filename = "temp.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

while True:
    success, img = cap.read()
    if not success:
        continue

  
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            landmarks = handLms.landmark
            finger_up = []
            tips = [4, 8, 12, 16, 20]

            for tip in tips:
                if landmarks[tip].y < landmarks[tip - 2].y:
                    finger_up.append(1)
                else:
                    finger_up.append(0)

            total_fingers = sum(finger_up)
            current_time = time.time()

            if current_time - last_trigger > 3:
                if finger_up == [1, 0, 0, 0, 0]:
                    speak("halo")
                elif finger_up == [0, 1, 0, 0, 0]:
                    speak("perkenalkan")
                elif finger_up == [0, 1, 1, 0, 0]:
                    speak("aku")
                elif finger_up == [1, 1, 1, 1, 1]:
                    speak("Renatha Putri")

                last_trigger = current_time

    cv2.imshow("Hand Voice", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
