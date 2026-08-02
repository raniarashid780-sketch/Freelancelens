# FreelanceLens

Small pandas project analyzing real freelance job listings from Upwork.

## What it does

I collected 24 real job listings manually (Upwork doesn't have a public
API and scraping violates their terms, so I copied them by hand). The
script cleans the data and answers a few questions:

- What skills show up most often across listings?
- What's the average budget per category? (Kept fixed-price and hourly
  jobs separate, since averaging a flat price with an hourly rate doesn't
  make sense.)
- Which category has the most job postings?

## A few honest notes on the data

- Only 24 rows, so some categories only have 2-4 listings in them. I'm
  showing the sample size (n) next to every average so it's clear when a
  number is based on very little data.
- When a job listed a budget range, I recorded the minimum value, so the
  real averages are probably a bit higher than what's shown here.
- Skills were split on commas, so a phrase like "Business Process,
  Automation" might have gotten split into two skills when it was
  meant as one. Didn't go back and fix these by hand, just noting it here.

## Built with

Python, pandas

## What I found

- Most requested skills: Data Analysis (11), Microsoft Excel (7),
  Automation (7), Python (4), Business Analysis (3)
- Highest-paying fixed-price category: Automation, ~$425 average (n=4)
- Highest-paying hourly category: Data Analyst, ~$18.79/hr average (n=12)
- Most common category: Data Analyst

## Author

Rania Rashid