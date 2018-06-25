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
print(data['recordings'][110])
birdSoundURL = data['recordings'][117]['file']
birdSoundURL = birdSoundURL[2:]
print(birdSoundURL)
# print(recordingsPerPage)
# urllib.request.urlretrieve(birdSoundURL, 'tweetie.mp3')
