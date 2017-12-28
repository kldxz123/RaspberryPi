
import speech_recognition as sr
import wave
from os import path
import os

os.system("arecord -f S16_LE -r 16000 try.wav")
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "try.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")


r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source) 

BING_KEY = "cade57ac56b74219899994e5d46234b1"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings


try:
    result = r.recognize_bing(audio, key=BING_KEY)
    print(result.encode("utf-8"))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

