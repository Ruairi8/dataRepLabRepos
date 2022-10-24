# 23/10/22
from github import Github
from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)

# Outputted the names of my github respositories:
#for repo in g.get_user().get_repos():
#    print(repo.name)

repo = g.get_repo("Ruairi8/dataRepLabRepos")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)