import pandas as pd
from playsound import playsound
df = pd.read_csv("phone.csv")
df["Tested"] = False
df["Result"] = False
df["Remark"] = "-"

for i in df.index:
    remark = "meng"
    result = True
    df.loc[i,"Tested"] = True
    df.loc[i,"Result"] = result
    df.loc[i,"Remark"] = remark
    # print(df.Number[i],df.Result[i])
    df.to_csv("phone.csv", index=False)


# playsound('alert.mp3')
df = pd.read_csv("phone.csv")
print(df.head())