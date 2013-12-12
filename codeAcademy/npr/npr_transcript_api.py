#!/usr/bin/env python
from urllib2 import urlopen
from json import load
from npr_api_key import get_api_key


key = get_api_key()
url="http://api.npr.org/transcript"
url+="?apiKey="+key
url+="&format=json&id=152248901"
response=urlopen(url)
j=load(response)

for paragraph in j['paragraph']:
    print paragraph['$text'] + "\n"
