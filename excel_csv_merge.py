import pandas as pd
import os 
import shutil
import glob

files = glob.glob("Data/Source/*.xlsx")
files += glob.glob("Data/Source/*.csv")

data = []

os.makedirs("Data/Archive", exist_ok=True)

if not files:
    raise FileNotFoundError("No CSV or Excel files found.")

for file in files:
    if file.endswith(".xlsx"):
        df = pd.read_excel(file)

    elif file.endswith(".csv"):
        df = pd.read_csv(file)

    data.append(df)  
    shutil.move(file, "Data/Archive")

#merging

merge_df = pd.concat(data, ignore_index= True)

print("Merge completed successfully.")

merge_df.drop_duplicates(inplace=True)  
#save output
os.makedirs("Output", exist_ok=True)

merge_df.to_excel("Output/Merge_data.xlsx", index = False)



                     