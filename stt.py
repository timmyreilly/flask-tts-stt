from tokens import *
import requests 
import json 
import base64

SPEECH_END_POINT = "https://speech.platform.bing.com/recognize"
TTSHOST = "https://speech.platform.bing.com"


TTS_URL = "https://speech.platform.bing.com/recognize/query" 
STT_HEADERS = {"Content-type": "audio/wav", "samplerate":"8000"}
STT_PARAMS = {"Version":"3.0","requestid":"1", "appID":"D4D52672-91D7-4C74-8AD8-42B1D98141A5","format": "json", "locale":"en-US", "device.os":"Windows OS", "scenarios":"ulm", "instanceid":"b2c95ede-97eb-4c88-81e4-80f32d6aee", "maxnbest":"3", "result.profanity":"0"}

r = requests.post(TTS_URL, headers=STT_HEADERS) 