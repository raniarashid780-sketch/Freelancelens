import pandas as pd
sample_data = pd.read_csv("freelance_jobs.csv")
print(list(sample_data.columns))
print(sample_data["experience"].unique())
print(sample_data.head())
print(sample_data.info())
sample_data["experience"] = sample_data["experience"].str.lower().str.strip()
print(sample_data["title"].str.contains("�", na=False).any())
print(sample_data["experience"].unique())
sample_data["skills"] = sample_data["skills"].str.split(",")
exploded_data = sample_data.explode("skills")
exploded_data["skills"] = exploded_data["skills"].str.strip()
exploded_data = exploded_data[exploded_data["skills"] != ""]
print(exploded_data["skills"].value_counts())
print(sample_data["budget_type"].unique())   # verify first
sample_data["budget_type"] = sample_data["budget_type"].str.lower().str.strip()

sample_data["budget"] = pd.to_numeric(
    sample_data["budget"].astype(str).str.replace(r"[$,]", "", regex=True),
    errors="coerce"
)

fixed_df = sample_data[sample_data["budget_type"] == "fixed"]
hourly_df = sample_data[sample_data["budget_type"] == "hourly"]

fixed_summary = fixed_df.groupby("category")["budget"].agg(["mean", "count"])
hourly_summary = hourly_df.groupby("category")["budget"].agg(["mean", "count"])
print(fixed_summary)
print(hourly_summary)