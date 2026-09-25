# CodeOrbit Data Cleaning Task

This is my Task 1 submission for the CodeOrbit Tech Data Analyst internship.

## Project Title
Data Cleaning in Excel/Python - Sample Customer Dataset

## Technologies Used
- Python 3
- pandas

## Setup Instructions
1. Install pandas if you don't have it: `pip install pandas`
2. Run the script: `python3 clean_data.py`
3. It will read messy_customers.csv, clean it, and save the result as cleaned_customers.csv

## GitHub Repository Link
https://github.com/poojitha-sv/CodeOrbit_DataCleaning

## What This Project Does
I took a small sample customer dataset that I made myself, with some common data problems added in on purpose (duplicate rows, missing values, inconsistent formatting, different date formats). Then I cleaned it up using Python and pandas.

## Files Here
- messy_customers.csv - the original messy data
- clean_data.py - the script I used to clean it
- cleaned_customers.csv - the cleaned result
- Data_Cleaning_Report.md - explains each step I did and why

## Quick Summary of What Was Fixed
- Removed a duplicate row
- Found and removed a second hidden duplicate (same customer entered twice)
- Fixed inconsistent capitalization in names/emails/cities
- Removed extra spaces
- Standardized all dates to one format
- Filled in missing values (marked as Unknown/Missing for text, used median for the numeric column)
- Fixed data types

More details are in Data_Cleaning_Report.md.
