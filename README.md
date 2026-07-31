# FreelanceLens

Analyzes freelance job listings (manually collected from Upwork) to surface
in-demand skills and typical budgets by category.

## What it does
- Loads job listing data (title, skills, budget, category)
- Finds most commonly requested skills
- Computes average budget per category (fixed vs hourly handled separately)
- Flags missing data (e.g. unlisted hourly rates)

## Data
`freelance_jobs.csv` — 20-25 manually collected Upwork listings, July 2026.
Note: budget ranges were recorded at their minimum value.

## Tech
Python, pandas, NumPy

## Author
Rania Rashid