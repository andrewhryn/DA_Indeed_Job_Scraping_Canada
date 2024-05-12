# 🍲 Indeed Data Analyst Job Scraping Project using Python
![alt text](image-1.png)
# :rocket: Introduction

This project aims to scrape job listings for data analyst positions from Indeed using Python. It utilizes web scraping techniques to extract job titles, company names, and locations from the Indeed job search results.

# :clipboard: Background

As I was searching for a dataset of data analyst job postings in Canada, I encountered challenges in finding a comprehensive and up-to-date source. Unable to locate an existing dataset, I embarked on building a solution using Python. Leveraging online guides and seeking assistance from ChatGPT for debugging, I developed a web scraping script to extract job listings from Indeed. This project serves not only as a tool for personal use but also contributes to filling the gap in available datasets for data analyst job postings in Canada.

# :wrench: Tools I Used

- Python
- Requests library for making HTTP requests
- BeautifulSoup library for parsing HTML content
- Pandas library for data manipulation and analysis

# :computer: How to Use This Code

### 1. **Navigate to [final_code.py](https://github.com/MadGrib/DA_Indeed_Job_postings_Canada/blob/main/bs_venv/final_code.py)**

### 2. **Before running the code below, please ensure you have installed all required libraries separately.**

```python
# Step 1: Install requests library
import requests

# Step 2: Install BeautifulSoup from bs4
from bs4 import BeautifulSoup

#Step 3: Install BeautifulSoup
import bs4

# Step 4: Install Pandas library
import pandas as pd
```

### 3. **Paste Your Own User Agent:**

Edit the following line in the code to replace `'your_own_link_here'` with your actual user agent link:

```python
url = f'your_own_link_here'
```
####  NOTE: To find your user agent link, simply search "my user agent" in Google. 

### 4. **Customize the Number of Pages and Job Listings:**

You can adjust the number of pages you want to scrape and the number of job listings per page. For example:
```python
for i in range(0, 70 * 15, 15):  # Scrape 70 pages, each page has 15 listings
```

# :running: Run the Script:

Once you've made the necessary adjustments, run the script to scrape job listings from Indeed. The extracted data will be stored in a CSV file named `job_listings.csv` in the same directory.


# :bar_chart: The Analysis

The main steps involved in the analysis are:

1. Extracting job titles, company names, and locations from Indeed job search results.
2. Parsing the HTML content of the job listings page using BeautifulSoup.
3. Transforming the extracted data into a structured format.
4. Storing the data in a Pandas DataFrame.
5. Saving the DataFrame to a CSV file for further analysis.

# :books: What I Learned

Through this project, I gained experience in:

- Web scraping techniques using Python.
- Parsing HTML content with BeautifulSoup.
- Data manipulation and analysis with Pandas.

# :mega: Conclusion

Scraping job listings from Indeed provides valuable insights into the current job market for data analysts. This project demonstrates the power of web scraping and data analysis using Python for extracting useful information from online sources.
