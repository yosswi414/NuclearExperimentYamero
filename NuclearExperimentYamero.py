import urllib.request
import json
import os
from dotenv import find_dotenv, load_dotenv
from twitter import Twitter, OAuth
from datetime import datetime as dt

load_dotenv(find_dotenv())

PS_API_KEY = os.environ.get('PS_API_KEY')
TW_API_KEY = os.environ.get('TW_API_KEY')
TW_API_SEC = os.environ.get('TW_API_SEC')
TW_TKN_KEY = os.environ.get('TW_TKN_KEY')
TW_TKN_SEC = os.environ.get('TW_TKN_SEC')

# print(TW_TKN_KEY)
# print(TW_TKN_SEC)
# print(TW_API_KEY)
# print(TW_API_SEC)

tw = Twitter(
    auth = OAuth(
        TW_TKN_KEY,
        TW_TKN_SEC,
        TW_API_KEY,
        TW_API_SEC,
    )
)

url = 'https://api.p2pquake.net/v2/jma/quake?\
limit=1&types[]=Destination\
%28%E9%9C%87%E6%BA%90%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E6%83%85%E5%A0%B1%29'
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    jsonRaw = response.read().decode()

jsonData = json.loads(jsonRaw)

createdDateStr = jsonData[0]['created_at']

# print('created at: {}'.format(createdDateStr))

longitude = jsonData[0]['earthquake']['hypocenter']['longitude']
latitude = jsonData[0]['earthquake']['hypocenter']['latitude']

print(longitude, latitude)

urlPlaceSearch = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?\
key=' + PS_API_KEY + '&\
input=university&\
inputtype=textquery&\
language=ja&\
locationbias=point:'+str(latitude)+','+str(longitude)+'&\
fields=name,types'

print(urlPlaceSearch)
print()

reqPlaceSearch = urllib.request.Request(urlPlaceSearch)
with urllib.request.urlopen(reqPlaceSearch) as response:
    resultRaw = response.read().decode()

jsonResult = json.loads(resultRaw)

suspectUniversityName = jsonResult['candidates'][0]['name']

assert '大学' in suspectUniversityName

print('suspected university string: {}'.format(suspectUniversityName))

universityName = suspectUniversityName[0:suspectUniversityName.find('大学')+2]

print('detected university name: {}'.format(universityName))

tweetTagString = universityName + 'は核実験をやめろ'

message = '#' + tweetTagString
print('\n\n')

createdDate = dt.strptime(createdDateStr, '%Y/%m/%d %H:%M:%S.%f')
currentDate = dt.now()
elapsedTime = currentDate - createdDate

print('Last detected earthquake date: {}'.format(createdDate))
print('Current date:                  {}'.format(currentDate))
print('\n')
print('Elapsed time: ',end='')
if elapsedTime.days > 0:
    print('{} day(s) '.format(elapsedTime.days),end='')
if elapsedTime.seconds//3600 > 0:
    print('{} hour(s) '.format(elapsedTime.seconds//3600),end='')
if elapsedTime.seconds%3600//60 > 0:
    print('{} minute(s) '.format(elapsedTime.seconds%3600//60),end='')
if elapsedTime.seconds % 60 > 0:
    print('{} second(s) '.format(elapsedTime.seconds%60),end='')
print('\n')

print('Are you sure to tweet:\"'+ message + '\" ?[y/N]')
answer = input()
if answer.strip() == 'y':
    tw.statuses.update(status=message)
    print('Tweet posted.')
else:
    print('Tweet aborted.')

print('press Enter to quit...')
input() # 
