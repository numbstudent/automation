import pandas as pd
df = pd.read_csv("phone.csv")
df["Tested"] = False
df["Result"] = False
df["Remark"] = "-"
count = 0
for i in df.index:
    if count > 9:
        break
    else:
        df["Tested"][i] = False
        df["Result"][i] = False
        # print(df.Number[i],df.Result[i])
        df.to_csv("phone.csv", index=False)
    count = count+1

df = pd.read_csv("phone.csv")
count = 0
for i in df.index:
    if count > 20:
        break
    else:
        print(df.Number[i],df.Tested[i],df.Result[i],df.Remark[i])
        df.to_csv(index=False)
    count = count+1