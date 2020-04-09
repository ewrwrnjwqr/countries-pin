import json
embassy = {}
i = 0 # change vary on len of dict
with open('mood.json') as data: 
    data = json.load(data)
#for i in data['embassies']: loop thru every country
    email = data['embassies'][i]['email']
    whom = data['embassies'][i]['title']
    print(whom)
    print(email)
    if email and whom:
        embassy.update({whom:email})
tf = '/Users/ejr/Desktop/everycount/dict.txt' 
f = open(tf,"a") 
with open(tf, "a") as f:
    f.write(str(embassy))
    f.write("\n")
    f.truncate()
    f.close()