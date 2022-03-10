import camelot
import pandas as pd
tables = camelot.read_pdf("MA Hemp Licenses 10.01.21.pdf",pages="1-end",flavor="stream")
li=[]
for i in tables:
    l=i.df.values.tolist()
    print(l)
    l=l[6:]
    for j in range(len(l)):
        li.append(l[j])
    
print((len(li)))

df=pd.DataFrame(li,columns=["License Type","License Number","Licensee","Mailing Address"])
print(df)
df.to_csv("pdf.csv")