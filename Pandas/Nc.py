import camelot
import pandas as pd
tables = camelot.read_pdf("D:\\Zigram\Pandas\\nc_processors.pdf",pages="1-3",flavor="stream")
df=tables[0].df[2:]

#Making All tables to Have 3 Columns and formatting to 1St page table structure
for i in range(1,tables.__len__(),1):
    df1=tables[i].df
    if(len(df1.columns)==4):
        for index,row in df1.iterrows():
            if(df1[2][index]!=""):
                df1[1][index]+="\n"+df1[2][index]
        df1.drop(2, axis=1, inplace=True)
        df1.columns=range(df1.columns.size)
    elif(len(df1.columns) == 5):
    #iterate through all the rows
        for index,row in df1.iterrows():
            if df1[2][index] !="" and df1[3][index] != "":
                df1[1][index] += '\n'+df1[2][index] +'\n' + df1[3][index]
        df1.drop([2,3],axis=1,inplace=True)
        df1.columns = range(df1.columns.size)
    df=pd.concat([df, df1], axis=0)

df.reset_index(drop=True,inplace=True)
df.columns=['Col1','Col2','Col3']
df["Col4"]=""
df["Col5"]=""

for index,row in df.iterrows():
    #Name as NA If there is NO Name
    if(df["Col2"][index]!="" and df["Col3"][index]!=""  and df["Col1"][index]==""):
        if(df["Col2"][index]!="" or df["Col3"][index]!=""):
            df["Col1"][index]="NA"
    #Creating Col4
    if(df["Col1"][index]!="" and df["Col2"][index]=="" and df["Col3"][index]==""):
        if(df["Col1"][index-1]==""):
            df["Col4"][index-2]=df["Col1"][index]
        else:
            df["Col4"][index-1]=df["Col1"][index]
    #Creating Col5
    if(df["Col1"][index]=="" and df["Col3"][index]=="" and df["Col2"][index-1]=="" and df["Col3"][index-1]==""):
        if(df["Col1"][index-2]==""):
            df["Col5"][index-3]=df["Col2"][index]
        else:
            df["Col5"][index-2]=df["Col2"][index]
    #ADD 2nd Line Address
    if(df["Col2"][index]!=""  and df["Col1"][index]=="" and df["Col1"][index-1]!="" and df["Col2"][index-1]!="" ):
        df["Col2"][index-1]+=" "+df["Col2"][index]
    #ADD 2nd Number
    if(df["Col3"][index]!=""  and df["Col1"][index]=="" and df["Col1"][index-1]!="" and df["Col2"][index-1]!="" ):
        df["Col3"][index-1]+=","+df["Col3"][index]

df=df[df["Col4"]!=""]
df.reset_index(drop=True,inplace=True)

df["Col6"]=df["Col5"].astype(str).apply(lambda x: x.split("\n")[1])
df["Col7"]=df["Col5"].astype(str).apply(lambda x: x.split("\n")[2] if len(x.split("\n"))==3 else "")
df["Col5"]=df["Col5"].astype(str).apply(lambda x: x.split("\n")[0])
df.to_csv("D:\\Zigram\Pandas\\test.csv")
print(df)

