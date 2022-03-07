import requests
from bs4 import BeautifulSoup
import pandas as pd
URL = "https://hdoa.hawaii.gov/hemp/licensees-by-county/"

c = requests.get(URL)

soup=BeautifulSoup(c.content,'html.parser')

d=[]
data=[[],[],[],[]]
table = soup.find('table',attrs={"border": '1',"style":"border-collapse: collapse; width: 91.1805%; height: 1318px;"})
table1 = soup.find('table',attrs={"border": '1',"style":"border-collapse: collapse; width: 91.1805%; height: 415px;"})
table.append(table1)

for j in table.find_all('td'):
        d.append(j.text)
d=d[4:]
for k in range(4):
    data[k]=d[k::4]

df = pd.DataFrame({'Date Licensed': data[0],'Name': data[1],'Island': data[2],"Contact":data[3]})

print(df)
# df.to_csv("data.csv")





