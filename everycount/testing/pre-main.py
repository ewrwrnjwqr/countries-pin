from bs4 import BeautifulSoup
import requests
import json

i = 0
embassy_d = {}

url = "https://embassy.goabroad.com/api/embassies?host_country_id=91&limit=986"
response = requests.get(url)
data = response.text
parsed = json.loads(data) #loads = load string

for i in range(0,986):
    email = parsed['embassies'][i]['email']
    whom = parsed['embassies'][i]['title']
    print(whom)
    print(email)
    if email and whom:
        embassy_d.update({whom:email})
    i += 1

tf = '/Users/ejr/Desktop/everycount/dict.txt' 
f = open(tf,"a") 
with open(tf, "a") as f:
    f.write(str(embassy_d))
    f.write("\n")
    f.truncate()
    f.close()

