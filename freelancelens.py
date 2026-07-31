import pandas as pd
sample_data = pd.read_csv("freelancer_jobs.csv")
print(list(sample_data.columns))
print(sample_data["experience"].unique())
print(sample_data.head())
print(sample_data.info())
sample_data["experience"] = sample_data["experience"].str.lower().str.strip()
print(sample_data["title"].str.contains("�", na=False).any())
print(sample_data["experience"].unique())