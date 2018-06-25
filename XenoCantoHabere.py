import json
import requests
import urllib.request

# Requires the pip package

baseAPIEndPoint = 'http://www.xeno-canto.org/api/2/recordings?query=cnt:south_africa'
response = requests.get(baseAPIEndPoint)
data = response.json()



# Print the status code of the response.
print(response.headers)
print(data)
print(data['numRecordings'])

numberOfRecordings = data['numRecordings']
numberOfSpecies = data['numSpecies']
currentPage = data['page']
totalPages = data['numPages']
# recordingsPerPage = data[len(data['recordings'])]

print(totalPages)
print(data['recordings'][0])
birdName = data['recordings'][0]['en']
soundID = data['recordings'][0]['id']
birdSoundURL = data['recordings'][0]['file']
birdSoundURL = birdSoundURL[2:]
print(birdSoundURL)
birdSoundURL = "http://"+birdSoundURL
r = requests.get(birdSoundURL, stream = True)
fileName = soundID + '-' + birdName + '.mp3'


with open(fileName, 'wb') as f:
    for chunk in r.iter_content(chunk_size = 1024):
        if chunk:
            f.write(chunk)
# print(recordingsPerPage)
# urllib.request.urlretrieve(birdSoundURL, 'tweetie.mp3')
