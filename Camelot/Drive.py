import camelot
import pandas as pd
tables = camelot.read_pdf("D:\Zigram\Camelot\All Active Registrants By County.pdf",pages="2-end",flavor="stream",table_areas=['105,621,430,90'])
print(tables[0].df)

m=[]
e=["",""]
for i in tables:
    l=i.df.values.tolist()
    if(len(l)%3!=0):
        for n in range(3-(len(l)%3)):
            l.append(e)
    for k in range(0,len(l),3):
        m.append(l[k]+l[k+1]+l[k+2])

df=pd.DataFrame(m,columns=["ID","Name","Col-3","Col-4","Phn No","Col-6"])
print(df)
df.to_csv("Drive.csv")





