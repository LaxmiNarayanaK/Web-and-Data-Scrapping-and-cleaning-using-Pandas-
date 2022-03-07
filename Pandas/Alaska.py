import pandas as pd

df=pd.read_excel("Alaska Industrial Hemp Registrant Public Records_USETHIS-converted.xlsx")
header = df.iloc[0] 
df = df[1:]
df.columns = header 

new = df["Premises Address"].str.split(",", n = 2, expand = True)
df.drop('Premises Address', axis=1, inplace=True)

new.columns=["Street","City","Province"]
zipcode=new["Province"].str.replace(",","").str.split(" ",n=2, expand = True)
new.drop('Province', axis=1, inplace=True)
zipcode.drop(0,axis=1, inplace=True)
zipcode.columns=["Province","Zip Code"]

address=pd.concat([new, zipcode], axis=1)

for i in reversed(range(len(address.columns))):
    df.insert(loc=1, column=address.columns[i], value=address[address.columns[i]])
df.to_csv("Alaska.csv")

