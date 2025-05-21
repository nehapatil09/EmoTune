import cv2
from deepface import DeepFace
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def detect_emotion():
    cam = cv2.VideoCapture(0)
    print("Detecting Emotion. Look at the camera...")

    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        return "neutral"

    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    emotion = result[0]['dominant_emotion']
    print(f"Detected Emotion: {emotion}")
    cam.release()
    cv2.destroyAllWindows()
    return emotion

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="b01ca3c10234419baf6e4dbdfcccf324",
    client_secret="4033297a0dbf43ef8bf81c495c9584d1",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-playback-state,user-modify-playback-state"
))

emotion_to_playlist_uri = {
    "happy": "spotify:playlist:37i9dQZF1DXdPec7aLTmlC",
    "sad": "spotify:playlist:37i9dQZF1DWVrtsSlLKzro",
    "angry": "spotify:playlist:37i9dQZF1DWZLcGGC0HJbc",
    "neutral": "spotify:playlist:37i9dQZF1DWZeKCadgRdKQ",
    "surprise": "spotify:playlist:37i9dQZF1DX5trt9i14X7j",
    "fear": "spotify:playlist:37i9dQZF1DWX83CujKHHOn"
}

import webbrowser

def play_spotify_music(emotion):
    playlist_uri = emotion_to_playlist_uri.get(emotion)
    if playlist_uri:
        playlist_id = playlist_uri.split(":")[-1]
        playlist_url = f"https://open.spotify.com/playlist/{playlist_id}"
        webbrowser.open(playlist_url)
        print(f"Opened playlist for emotion '{emotion}' in your browser.")
    else:
        print(f"No playlist found for emotion: {emotion}")

def simulate_light_color(emotion):
    color_map = {
        "happy": "🟨 Yellow - Uplifting",
        "sad": "🔵 Blue - Calm",
        "angry": "🔴 Red - Intense",
        "neutral": "⚪ White - Neutral",
        "surprise": "🟣 Purple - Exciting",
        "fear": "🟢 Green - Reassuring"
    }
    print(f"Light color set to: {color_map.get(emotion, '⚪ White')}")
    
if __name__ == "__main__":
    emotion = detect_emotion()
    simulate_light_color(emotion)
    play_spotify_music(emotion)
