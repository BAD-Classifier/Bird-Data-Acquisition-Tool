import json
import requests
import urllib.request
import os
from tqdm import tqdm
# Requires the pip packages to be installed

# Specify API endpoint to the recordings in the country of South Africa
baseAPIEndPoint = 'http://www.xeno-canto.org/api/2/recordings?query=cnt:south_africa'
pageAPIEndPoint = 'http://www.xeno-canto.org/api/2/recordings?query=cnt:south_africa&page='
apiPage = 1
chunk_size = 1024
soundNumber = 1

# Use a GET request and store in the response object
response = requests.get(baseAPIEndPoint)
data = response.json()

numberOfRecordings = data['numRecordings']
numberOfSpecies = data['numSpecies']
currentPage = data['page']
totalPages = data['numPages']
recordingsPerPage = len(data['recordings'])

for page in range(1, totalPages):
    response = requests.get(pageAPIEndPoint + str(page))
    data = response.json()
    recordingsPerPage = len(data['recordings'])
    for recording in range(0, recordingsPerPage-1):

        birdGenus = data['recordings'][recording]['gen']
        birdSpecies = data['recordings'][recording]['sp']
        birdName = data['recordings'][recording]['en']
        soundID = data['recordings'][recording]['id']
        birdSoundURL = data['recordings'][recording]['file']
        birdSoundURL = birdSoundURL[2:]
        birdSoundURL = "http://" + birdSoundURL

        r = requests.get(birdSoundURL, stream=True)

        path = os.getcwd() + '/BirdSounds_1/page' + str(page) +'/'

        if not os.path.exists(path):
            os.makedirs(path)

        fileName = path + birdGenus + '-' + birdSpecies + '-' + birdName + '-' + soundID + '.mp3'
        total_size = int(r.headers['content-length'])

        print(str(soundNumber) + ") Downloading " +birdGenus + '-' + birdSpecies + '-' + birdName + '-' + soundID + '.mp3')
        with open(fileName, 'wb') as f:
            for chunk in tqdm(iterable = r.iter_content(chunk_size=chunk_size), total = total_size/chunk_size, unit = 'KB'):
                if chunk:
                    f.write(chunk)

        # print("File " + str(soundNumber) + " successfully downloaded")
        soundNumber = soundNumber + 1

    print("Page " + str(page) + " fully downloaded")
