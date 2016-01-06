from tokens import *
import requests 
import json 
import base64

SPEECH_END_POINT = "https://speech.platform.bing.com/recognize"
TTSHOST = "https://speech.platform.bing.com"


ACCESS_TOKEN_PAYLOAD = {'grant_type': 'client_credentials', 'client_id': 'nothing', 'client_secret': OXFORD_SPEECH_API, 'scope': TTSHOST}
ACCESS_TOKEN_HEADERS = {"Content-type": "application/x-www-form-urlencoded"}
ACCESS_TOKEN_HOST = "http://oxford-speech.cloudapp.net"
ACCESS_TOKEN_PATH = "/token/issueToken" 
ACCESS_TOKEN_URL = ACCESS_TOKEN_HOST+ACCESS_TOKEN_PATH 

def get_access_token():
    r = requests.post(ACCESS_TOKEN_URL, headers=ACCESS_TOKEN_HEADERS, data=ACCESS_TOKEN_PAYLOAD)
    print "Access token status code: " + str(r.status_code)
    data = r.content 
    return str(json.loads(data)['access_token'])

TTS_HEADERS = {"Content-type": "application/ssml+xml", 
			"X-Microsoft-OutputFormat": "riff-8khz-8bit-mono-mulaw", 
			"Authorization": "Bearer " + get_access_token(), 
			"X-Search-AppId": "07D3234E49CE426DAA29772419F436CA", 
			"X-Search-ClientID": "1ECFAE91408841A480F00935DC390960", 
			"User-Agent": "TTSForPython"}

TTS_URL = TTSHOST + "/synthesize"

def get_raw_wav(text="hello world"):
    body = "<speak version='1.0' xml:lang='en-us'><voice xml:lang='en-us' xml:gender='Female' name='Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)'>" + text + "</voice></speak>"
    r = requests.post(TTS_URL, headers=TTS_HEADERS, data=body)
    print "TTS Status Code: " + str(r.status_code) 
    data = r.content 
    return str(base64.b64encode(data))
