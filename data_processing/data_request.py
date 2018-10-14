import requests

r = requests.get("https://api.opendota.com/api/matches/4164255132")
print(r.text)

# pro players info
pro = requests.get("https://api.opendota.com/api/proPlayers")