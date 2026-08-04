import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


top_skills = exploded_data["skills"].value_counts().head(5)
fig, axes = plt.subplots(nrows=2, ncols= 2, figsize=(10, 8))
axes[0, 0].bar(top_skills.index, top_skills.values, color='tab:blue')
axes[0, 0].tick_params(axis='x', labelsize=6)
axes[0, 0].set_ylabel("Value")
axes[0, 0].set_title("Top 5 skills")

axes[0, 1].bar(fixed_summary.index, fixed_summary["mean"], color='tab:green')
axes[0, 1].set_ylabel("Average Budget")
axes[0, 1].set_title("Average budget per fixed category")

axes[1, 0].bar(hourly_summary.index, hourly_summary["mean"], color='tab:red')
axes[1, 0].set_ylabel("Average hourly rate")
axes[1, 0].set_title("Average hourly rate per category")

category_counts = sample_data["category"].value_counts()
axes[1, 1].bar(category_counts.index, category_counts.values, color='tab:orange')
axes[1, 1].set_xlabel("Category")
axes[1, 1].set_ylabel("Number of Listings")
axes[1, 1].set_title("Most Common Category")

fig.savefig("freelancelens_charts.png", dpi=150, bbox_inches='tight')
plt.subplots_adjust(hspace=0.5)
fig.tight_layout(pad=3.0)
fig.suptitle("FreelanceLens: Job Market Analysis", fontsize=14, fontweight='bold')
plt.show()