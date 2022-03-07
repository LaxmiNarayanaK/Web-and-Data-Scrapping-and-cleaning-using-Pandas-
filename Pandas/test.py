import pandas as pd

df=pd.read_excel("D:\Zigram\Pandas\Alaska Industrial Hemp Registrant Public Records_USETHIS-converted.xlsx") 
df.columns = df.iloc[0]
df = df[1:]

df.rename(columns={'Expiration\nDate': 'Expiration Date', 'Phone\nNumber': 'Phone Number'}, inplace=True)


df["Street"]=df["Premises Address"].astype(str).apply(lambda x: x.split(",")[0] if "," in x else "")
df["City"]=df["Premises Address"].astype(str).apply(lambda x: x.split(",")[1] if "," in x else "")

# df["Zipcode"]=df["Premises Address"].astype(str).apply(lambda x: x.strip(",")[2] if "," in x else "")
# for index,row in df.iterrows():
#     if(len(str(df["Premises Address"][index]).split(","))==2):
#         print(index)
# df["City"]=df["Premises Address"].astype(str).str.split(",",n=2)


df["Combine"]=df.astype(str).apply(lambda x: x.Street+x.City, axis = 1)
df.to_csv("test.csv")
