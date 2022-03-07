import requests
from bs4 import BeautifulSoup
import pandas as pd

data=[]
combine=[[],[],[],[],[],[],[],[]]
page=0
while True:
    URL = "https://www.ams.usda.gov/rules-regulations/hemp/dea-laboratories?field_lab_location_administrative_area=All&page="+str(page)
    c = requests.get(URL)
    soup=BeautifulSoup(c.content,'html.parser')
    if(soup.find("div",class_="view-content")):
        table=soup.find("div",class_="view-content")
        page+=1
        for i in table.find_all("tr"):
            for j in i.find_all("td"):
                data.append(j.text)
                for k in j.find_all("a"):
                    l=k['href']
                    link="https://www.ams.usda.gov"+l
                    combine[3].append(link)
    else:
        break

for a in range(3):
    combine[a]=data[a::3]

for l in range(len(combine[3])):
    soup=BeautifulSoup((requests.get(combine[3][l])).content,'html.parser')
    table=soup.find("div",class_="region-content usa-width-three-fourths")
    for x in table.find("div",class_='field__item'):
            combine[4].append(x.find("span",class_='address-line1').text+x.find("span",class_='locality').text+","+x.find("span",class_='administrative-area').text+x.find("span",class_='postal-code').text+","+x.find("span",class_='country').text)

    if(table.find("div",class_="field field--name-field-phone-number field--type-string field--label-above")):
        combine[5].append(table.find("div",class_="field field--name-field-phone-number field--type-string field--label-above").find("div",class_="field__item").text)
    else:
        combine[5].append("NA")

    combine[6].append(table.find("div",class_="field field--name-field-contact field--type-string field--label-above").find("div",class_="field__item").text)
    
    combine[7].append(table.find("div",class_="field field--name-field-contact-email field--type-email field--label-above").find("div",class_="field__item").text)

df = pd.DataFrame({'Lab Name': combine[0],'City': combine[1],'State': combine[2],'Lab Location': combine[4],'Phone Number': combine[5],'Contact': combine[6],'Email': combine[7]})
print(df)
df.to_csv("Labs.csv")

