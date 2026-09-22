# CodeOrbit Data Cleaning Task

This is my Task 1 submission for the CodeOrbit Tech Data Analyst internship.

## What this project does
I took a small sample customer dataset that I made myself, with some common data problems added in on purpose (duplicate rows, missing values, inconsistent formatting, different date formats). Then I cleaned it up using Python and pandas.

## Files here
- messy_customers.csv - the original messy data
- clean_data.py - the script I used to clean it
- cleaned_customers.csv - the cleaned result
- Data_Cleaning_Report.md - explains each step I did and why

## Tools used
- Python 3
- pandas

## How to run it
1. Install pandas if you don't have it: `pip install pandas`
2. Run the script: `python3 clean_data.py`
3. It will read messy_customers.csv, clean it, and save the result as cleaned_customers.csv

## Repo link
https://github.com/poojitha-sv/CodeOrbit_DataCleaning

## Quick summary of what was fixed
- Removed a duplicate row
- Found and removed a second hidden duplicate (same customer entered twice)
- Fixed inconsistent capitalization in names/emails/cities
- Removed extra spaces
- Standardized all dates to one format
- Filled in missing values (marked as Unknown/Missing for text, used median for the numeric column)
- Fixed data types

More details are in Data_Cleaning_Report.md.
