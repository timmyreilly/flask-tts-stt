from tokens import * 

SPEECH_END_POINT = "https://speech.platform.bing.com/recognize"

ttsHost = "https://speech.platform.bing.com"

payload = {'grant_type': 'client_credentials', 'client_id': 'nothing', 'client_secret': OXFORD_SPEECH_API, 'scope': ttsHost}

headers = {"Content-type": "application/x-www-form-urlencoded"}