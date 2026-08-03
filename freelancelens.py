import pandas as pd
import numpy as np
sample_data = pd.read_csv("freelance_jobs.csv")

sample_data["experience"] = sample_data["experience"].str.lower().str.strip()

sample_data["skills"] = sample_data["skills"].str.split(",")
exploded_data = sample_data.explode("skills")
exploded_data["skills"] = exploded_data["skills"].str.strip()
exploded_data = exploded_data[exploded_data["skills"] != ""]

sample_data["budget_type"] = sample_data["budget_type"].str.lower().str.strip()

sample_data["budget"] = pd.to_numeric(
    sample_data["budget"].astype(str).str.replace(r"[$,]", "", regex=True),
    errors="coerce"
)

fixed_df = sample_data[sample_data["budget_type"] == "fixed"]
hourly_df = sample_data[sample_data["budget_type"] == "hourly"]

fixed_summary = fixed_df.groupby("category")["budget"].agg(["mean", "count"])
hourly_summary = hourly_df.groupby("category")["budget"].agg(["mean", "count"])
print("Top five skills")
print(exploded_data["skills"].value_counts().head(5))
print("Fixed-price budget by category")
print(fixed_summary)
print("Hourly budget by category")
print(hourly_summary)

print("Most common category")
print(sample_data["category"].value_counts().idxmax())
print("Highest-paying fixed category:", fixed_summary["mean"].idxmax())
print("Highest-paying hourly category:", hourly_summary["mean"].idxmax())
fixed_std = fixed_df.groupby("category")["budget"].apply(lambda x : np.nanstd(x, ddof=1))
hourly_std = hourly_df.groupby("category")["budget"].apply(lambda x : np.nanstd(x, ddof=1))
print("Fixed budget std dev by category")
print(fixed_std)
print("Hourly budget std dev by category")
print(hourly_std)
fixed_median = fixed_df.groupby("category")["budget"].apply(lambda x: np.nanpercentile(x, 50))
hourly_median = hourly_df.groupby("category")["budget"].apply(lambda x: np.nanpercentile(x, 50))
print("Fixed median budget by category")
print(fixed_median)
print("Hourly median budget by category")
print(hourly_median)