import json
i = 0
with open('mood.json') as data: 
    data = json.load(data)
    email = data['embassies'][i]['email']
    print(email)