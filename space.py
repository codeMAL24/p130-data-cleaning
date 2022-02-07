import csv
import pandas as pd

df = pd.read_csv("starFinal.csv")
print(df.shape)

#del df[""]
#there's nothing there to delete

df.to_csv("FinalFinal.csv")