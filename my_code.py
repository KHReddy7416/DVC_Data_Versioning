import pandas as pd
import os

# Data
data = {
    "name": ["hemanth", "harini", "sharmila"],
    "age": [22, 23, 24],
    "city": ["chennai", "bangalore", "hyderabad"]
}

# Create DataFrame
df = pd.DataFrame(data)

new_row = {"name": "new_user", "age": 25, "city": "delhi"}
df.loc[len(df.index)]=new_row
# Directory path
save_dir = "data"

# Create directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Save CSV
df.to_csv(os.path.join(save_dir, "sample_data.csv"), index=False)

print("CSV saved successfully!")
