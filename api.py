import requests, json
teams =[]
url = 'https://raw.githubusercontent.com/openfootball/worldcup.json/master/2018/worldcup.teams.json'
url2 = 'https://worldcupjson.net/teams'

response = requests.get(url2)


json_response = response.json()

# for team in json_response['teams']:
    # teams.append(team['name'])
# print(json_response)

print('--------------------------------------')
for groups in json_response['groups']:
    teams2 = groups['teams']
    for team in teams2:
        # print(groups['letter'])   
        teams.append(team['name'])

