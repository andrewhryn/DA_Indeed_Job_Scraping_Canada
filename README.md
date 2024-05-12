# Indeed Data Analyst Job Scraping Project using Python

## Introduction

This project aims to scrape job listings for data analyst positions from Indeed using Python. It utilizes web scraping techniques to extract job titles, company names, and locations from the Indeed job search results.

## Background

As I was searching for a dataset of data analyst job postings in Canada, I encountered challenges in finding a comprehensive and up-to-date source. Unable to locate an existing dataset, I embarked on building a solution using Python. Leveraging online guides and seeking assistance from ChatGPT for debugging, I developed a web scraping script to extract job listings from Indeed. This project serves not only as a tool for personal use but also contributes to filling the gap in available datasets for data analyst job postings in Canada.

## Tools I Used

- Python
- Requests library for making HTTP requests
- BeautifulSoup library for parsing HTML content
- Pandas library for data manipulation and analysis

## The Analysis

The main steps involved in the analysis are:

1. Extracting job titles, company names, and locations from Indeed job search results.
2. Parsing the HTML content of the job listings page using BeautifulSoup.
3. Transforming the extracted data into a structured format.
4. Storing the data in a Pandas DataFrame.
5. Saving the DataFrame to a CSV file for further analysis.

## What I Learned

Through this project, I gained experience in:

- Web scraping techniques using Python.
- Parsing HTML content with BeautifulSoup.
- Data manipulation and analysis with Pandas.

## Conclusion

Scraping job listings from Indeed provides valuable insights into the current job market for data analysts. This project demonstrates the power of web scraping and data analysis using Python for extracting useful information from online sources.

# How to Use This Code

1. Navigate to `final_code.py`. (under bs_venv foler)

2. **Before running the code below, please ensure you have installed all required libraries separately.**

```python
# Step 1: Install requests library
import requests

# Step 2: Install BeautifulSoup from bs4
from bs4 import BeautifulSoup

#Step 3: Install BeautifulSoup
import bs4

# Step 4: Install Pandas library
import pandas as pd


