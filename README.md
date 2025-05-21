EmoTune: Emotion-Based Music and Lighting Controller

Concept:
- A smart emotion detector that plays music and adjusts smart light colors based on your current mood — detected via webcam and voice input.

Why It's Unique:
- Most mood-based apps require manual input.
- EmoTune uses facial expression and voice tone to predict your mood (happy, sad, stressed, neutral).
- Automatically plays a matching Spotify playlist and sets the room lighting (via a smart light API like Philips Hue or WLED).

Tech Stack:
- Python
- OpenCV + DeepFace (for facial emotion recognition)
- SpeechRecognition + pyttsx3 (for tone/mood via voice)
- Spotify API (for music playback)
- Smart Light API (like WLED, Philips Hue, or simulated GUI light)
- Flask (if you want a dashboard)

Key Features:
- Real-time emotion detection from webcam or mic
- Auto-playlist selection from your Spotify account
- Light color changes: e.g., blue for calm, yellow for happy, red for energetic
- Optional mood tracking dashboard (see how your emotions vary by day/time)

