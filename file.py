import requests
import json
apikey = ''
filename = "repos-private.json"
url = 'https://api.github.com/reps/andrewbeattycourseware/aprivateone'
response = requests.get(url, auth=('token', apikey))
print(response.status_code)

with open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)