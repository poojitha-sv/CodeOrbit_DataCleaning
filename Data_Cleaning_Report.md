
For this task, I created a small sample customer dataset (messy_customers.csv) with 12 rows and 7 columns: CustomerID, Name, Email, Phone, SignupDate, City, and PurchaseAmount.

I added some common data problems into it on purpose, so I could practice cleaning them:
- One row (Customer 2, Jane Doe) was an exact duplicate, copied twice
- Customer 9 (David Lee) was also entered twice, but one of the entries was missing the purchase amount
- Several missing values in Name, Phone, SignupDate, and PurchaseAmount
- Names, emails,s and cities were written inconsistently, like "jane doe" instead of "Jane Doe", or "JANE.DOE@EMAIL.COM" in all caps, plus some extra spaces like "Sarah Williams " with a trailing space
- Dates were written in 3 different formats in the same column (2023-01-15, 01/16/2023, 2023/01/17)
I used Python 3 with the pandas library to do the cleaning (clean_data.py).



 Customer 2's row was repeated exactly, so I used drop_duplicates() to remove the extra copy.

 Some entries had extra spaces before or after the text (like "Sarah Williams "), so I trimmed those using .strip().

 I made all names and cities use Title Case, and made all emails lowercase, so everything looks consistent.

 While checking the data, I noticed David Lee (Customer 9) was actually entered twice under the same ID, just with one row missing the purchase amount. I kept the row that had the complete data and removed the other one.

 Since the dates were in 3 different formats, I converted all of them to one standard format: YYYY-MM-DD.

 For missing names or dates, I couldn't guess the real value, so I filled them with "Unknown" or "Missing" instead of leaving them blank. For the missing purchase amounts, I filled them in using the median value of that column, since that's a safer choice than just using 0 or the average.

I made sure CustomerID was stored as a whole number, and PurchaseAmount was rounded to 2 decimal places, then saved the final result as cleaned_customers.csv.



Before cleaning, the dataset had 12 rows, 2 duplicate entries, 6 missing values, and 3 different date formats.

After cleaning, it has 10 rows, no duplicates, no missing values (they're either filled in or clearly marked), and one consistent date format.


| CustomerID | Name | Email | Phone | SignupDate | City | PurchaseAmount |

| 1 | John Smith | john.smith@email.com | 123-456-7890 | 2023-01-15 | New York | 250.50 |
| 2 | Jane Doe | jane.doe@email.com | 123-456-7891 | 2023-01-16 | Los Angeles | 300.00 |
| 3 | Mike Johnson | mike.j@email.com | Missing | 2023-01-17 | Chicago | 295.00 |
| 4 | Sarah Williams | sarah.w@email.com | 123-456-7893 | 2023-01-18 | Houston | 150.75 |
| 5 | Unknown | tom.brown@email.com | 123-456-7894 | 2023-01-19 | Phoenix | 400.00 |
| 6 | Emily Davis | emily.davis@email.com | 123-456-7895 | 2023-01-20 | Philadelphia | 275.25 |
| 7 | Chris Wilson | chris.w@email.com | 123-456-7896 | Missing | San Antonio | 295.00 |
| 8 | Anna Taylor | anna.taylor@email.com | 123-456-7897 | 2023-01-22 | San Diego | 325.00 |
| 9 | David Lee | david.lee@email.com | 123-456-7898 | 2023-01-23 | Dallas | 290.00 |
| 10 | Laura Martin | laura.m@email.com | 123-456-7899 | 2023-01-24 | Austin | 310.50 |

Note: 295.00 is the median purchase amount, which I used to fill in the two missing amounts.
