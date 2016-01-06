import http.client, urllib.parse, json, base64
from tokens import *

#Note: Sign up at http://www.projectoxford.ai to get a subscription key.  
#Search for Speech APIs from Azure Marketplace.
#Use the subscription key as Client secret below.

#uncomment this line and add your client_id: 
# clientSecret = '<32 digits of security>'

ttsHost = "https://speech.platform.bing.com"

params = urllib.parse.urlencode({'grant_type': 'client_credentials', 'client_id': 'nothing', 'client_secret': OXFORD_SPEECH_API, 'scope': ttsHost})

print ("The body data: %s" %(params))

headers = {"Content-type": "application/x-www-form-urlencoded"}
			
AccessTokenHost = "oxford-speech.cloudapp.net"
path = "/token/issueToken"

# Connect to server to get the Oxford Access Token
conn = http.client.HTTPSConnection(AccessTokenHost)
conn.request("POST", path, params, headers)
response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
conn.close()

accesstoken = data.decode("UTF-8")
print ("Oxford Access Token: " + accesstoken)

#decode the object from json
ddata=json.loads(accesstoken)
access_token = ddata['access_token']

headers = {"Content-type": "application/ssml+xml", 
			"X-Microsoft-OutputFormat": "riff-8khz-8bit-mono-mulaw", 
			"Authorization": "Bearer " + access_token, 
			"X-Search-AppId": "07D3234E49CE426DAA29772419F436CA", 
			"X-Search-ClientID": "1ECFAE91408841A480F00935DC390960", 
			"User-Agent": "TTSForPython"}


def get_raw_wav(text='say hello'):
	body = "<speak version='1.0' xml:lang='en-us'><voice xml:lang='en-us' xml:gender='Female' name='Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)'>" + text + "</voice></speak>"
	conn = http.client.HTTPSConnection("speech.platform.bing.com")
	conn.request("POST", "/synthesize", body, headers)
	response = conn.getresponse()
	print(response.status, response.reason)
	data = response.read()
	encoded = base64.b64encode(data)
	s = str(encoded)
	sliced = s[2:-1]
	conn.close()
	print(sliced)
	return sliced
	
	
if __name__ == "__main__":
	get_raw_wav('hello')