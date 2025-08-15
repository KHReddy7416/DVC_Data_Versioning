import pandas as pd 
import os

data ={
    "name":{"hemanth","harini","sharmila"},
    "age":[22,23,24],
    "city":["chennai","bangalore","hyderabad"]
}

df=pd.DataFrame(data)
df.to_csv(os.path.join("DVC_Data_Versioning/data", "sample_data.csv"), index=False)