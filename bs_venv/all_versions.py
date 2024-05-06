
#Step 1: extracting job_title data from Indeed

import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q=data+analyst&start={page}&vjk=b7c58b9a5fc8f161'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_titles = soup.find_all('a', class_='jcs-JobTitle')  
    for title in job_titles:
        job_title_span = title.find('span', id=lambda x: x and x.startswith('jobTitle'))
        if job_title_span:
            print(job_title_span.text)
    return 

c = extract(0)
transform(c)

## Step 2: geting info for the location and company name: 

import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q=data+analyst&start={page}&vjk=b7c58b9a5fc8f161'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_listings = soup.find_all('div', class_='company_location')  # Find all divs containing company information
    for job in job_listings:
        company_name = job.find('span', class_='css-92r8pb')  # Find the span with company name
        location = job.find('div', class_='css-1p0sjhy')  # Find the div with location
        if company_name and location:
            print("Company:", company_name.text.strip())  # Extract and print company name
            print("Location:", location.text.strip())  # Extract and print location
            print()  # Add a blank line for readability
    return 

c = extract(0)
transform(c)


##Step 3: Merging results in the correct order, now we get result in correct order: 1) job tilte, 2) Company, 3) Location

import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q=data+analyst&start={page}&vjk=b7c58b9a5fc8f161'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_listings = soup.find_all('div', class_='company_location')  # Find all divs containing company information
    job_titles = soup.find_all('a', class_='jcs-JobTitle')  # Find all job titles

    for job_info, job_title in zip(job_listings, job_titles):
        # Extract and print job title
        job_title_span = job_title.find('span', id=lambda x: x and x.startswith('jobTitle'))
        if job_title_span:
            print("Job Title:", job_title_span.text.strip())

        # Extract and print company name
        company_name = job_info.find('span', class_='css-92r8pb')  # Find the span with company name
        if company_name:
            print("Company:", company_name.text.strip())

        # Extract and print location
        location = job_info.find('div', class_='css-1p0sjhy')  # Find the div with location
        if location:
            print("Location:", location.text.strip())

        print()  # Add a blank line for readability

c = extract(0)
transform(c)


#Step 4: Add salary range for existing code, write 'Salary: Not available' if job posting does not have one

import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q=data+analyst&start={page}&vjk=b7c58b9a5fc8f161'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_listings = soup.find_all('div', class_='company_location')  # Find all divs containing company information
    job_titles = soup.find_all('a', class_='jcs-JobTitle')  # Find all job titles

    for job_info, job_title in zip(job_listings, job_titles):
        # Extract and print job title
        job_title_span = job_title.find('span', id=lambda x: x and x.startswith('jobTitle'))
        if job_title_span:
            print("Job Title:", job_title_span.text.strip())

        # Extract and print company name
        company_name = job_info.find('span', class_='css-92r8pb')  # Find the span with company name
        if company_name:
            print("Company:", company_name.text.strip())

        # Extract and print location
        location = job_info.find('div', class_='css-1p0sjhy')  # Find the div with location
        if location:
            print("Location:", location.text.strip())

        # Extract and print salary (if available)
        try:
            salary = job_info.find('span', class_='css-1cvvo1b').text.strip()
            print("Salary:", salary)
        except AttributeError:
            print("Salary: Not available")

        print()  # Add a blank line for readability

c = extract(0)
transform(c)

#Step 5: store result as a list

import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q=data+analyst&start={page}&vjk=b7c58b9a5fc8f161'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_listings = soup.find_all('div', class_='company_location')  # Find all divs containing company information
    job_titles = soup.find_all('a', class_='jcs-JobTitle')  # Find all job titles

    job_data = []

    for job_info, job_title in zip(job_listings, job_titles):
        # Extract and print job title
        job_title_span = job_title.find('span', id=lambda x: x and x.startswith('jobTitle'))
        job_title_text = job_title_span.text.strip() if job_title_span else "Not available"

        # Extract and print company name
        company_name = job_info.find('span', class_='css-92r8pb')  # Find the span with company name
        company_text = company_name.text.strip() if company_name else "Not available"

        # Extract and print location
        location = job_info.find('div', class_='css-1p0sjhy')  # Find the div with location
        location_text = location.text.strip() if location else "Not available"

        # Extract and print salary (if available)
        try:
            salary = job_info.find('span', class_='css-1cvvo1b').text.strip()
        except AttributeError:
            salary = "Not available"

        # Create dictionary for job data
        job = {
            'job_title': job_title_text,
            'company': company_text,
            'location': location_text,
            'salary': salary
        }

        # Append job data to list
        job_data.append(job)

    return job_data

c = extract(0)
result = transform(c)
print(result)







## Step 6: Now importing Pandas, we will save result in pandas data frame for the first 10 pages

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q=data+analyst&start={page}&vjk=b7c58b9a5fc8f161'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_listings = soup.find_all('div', class_='company_location')  # Find all divs containing company information
    job_titles = soup.find_all('a', class_='jcs-JobTitle')  # Find all job titles

    job_data = []

    for job_info, job_title in zip(job_listings, job_titles):
        # Extract and print job title
        job_title_span = job_title.find('span', id=lambda x: x and x.startswith('jobTitle'))
        job_title_text = job_title_span.text.strip() if job_title_span else "Not available"

        # Extract and print company name
        company_name = job_info.find('span', class_='css-92r8pb')  # Find the span with company name
        company_text = company_name.text.strip() if company_name else "Not available"

        # Extract and print location
        location = job_info.find('div', class_='css-1p0sjhy')  # Find the div with location
        location_text = location.text.strip() if location else "Not available"

        # Extract and print salary (if available)
        try:
            salary = job_info.find('span', class_='css-1cvvo1b').text.strip()
        except AttributeError:
            salary = "Not available"

        # Create dictionary for job data
        job = {
            'job_title': job_title_text,
            'company': company_text,
            'location': location_text,
            'salary': salary
        }

        # Append job data to list
        job_data.append(job)

    return job_data

# Create an empty list to store all job data
all_job_data = []

# Iterate through the first 10 pages
for i in range(0, 40, 10):
    # Extract data from the current page
    soup = extract(i)
    # Transform the data and append it to the list
    page_job_data = transform(soup)
    all_job_data.extend(page_job_data)

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(all_job_data)

# Print the DataFrame
print(df)


## Step 7 remove salary because it is not working correctly

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q=data+analyst&start={page}&vjk=b7c58b9a5fc8f161'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_listings = soup.find_all('div', class_='company_location')  # Find all divs containing company information
    job_titles = soup.find_all('a', class_='jcs-JobTitle')  # Find all job titles

    job_data = []

    for job_info, job_title in zip(job_listings, job_titles):
        # Extract and print job title
        job_title_span = job_title.find('span', id=lambda x: x and x.startswith('jobTitle'))
        job_title_text = job_title_span.text.strip() if job_title_span else "Not available"

        # Extract and print company name
        company_name = job_info.find('span', class_='css-92r8pb')  # Find the span with company name
        company_text = company_name.text.strip() if company_name else "Not available"

        # Extract and print location
        location = job_info.find('div', class_='css-1p0sjhy')  # Find the div with location
        location_text = location.text.strip() if location else "Not available"

        # Create dictionary for job data
        job = {
            'job_title': job_title_text,
            'company': company_text,
            'location': location_text
        }

        # Append job data to list
        job_data.append(job)

    return job_data

# Create an empty list to store all job data
all_job_data = []

# Iterate through the first 10 pages
for i in range(0, 40, 10):
    # Extract data from the current page
    soup = extract(i)
    # Transform the data and append it to the list
    page_job_data = transform(soup)
    all_job_data.extend(page_job_data)

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(all_job_data)

# Print the DataFrame
print(df)

# Step 8 Now same thing but for the first 10 pages

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q=data+analyst&start={page}&vjk=b7c58b9a5fc8f161'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_listings = soup.find_all('div', class_='company_location')  # Find all divs containing company information
    job_titles = soup.find_all('a', class_='jcs-JobTitle')  # Find all job titles

    job_data = []

    for job_info, job_title in zip(job_listings, job_titles):
        # Extract and print job title
        job_title_span = job_title.find('span', id=lambda x: x and x.startswith('jobTitle'))
        job_title_text = job_title_span.text.strip() if job_title_span else "Not available"

        # Extract and print company name
        company_name = job_info.find('span', class_='css-92r8pb')  # Find the span with company name
        company_text = company_name.text.strip() if company_name else "Not available"

        # Extract and print location
        location = job_info.find('div', class_='css-1p0sjhy')  # Find the div with location
        location_text = location.text.strip() if location else "Not available"

        # Create dictionary for job data
        job = {
            'job_title': job_title_text,
            'company': company_text,
            'location': location_text
        }

        # Append job data to list
        job_data.append(job)

    return job_data

# Create an empty list to store all job data
all_job_data = []

# Iterate through the first 10 pages
for i in range(0, 10 * 10, 10):  # Scrape 10 pages, each page has 10 listings
    # Extract data from the current page
    soup = extract(i)
    # Transform the data and append it to the list
    page_job_data = transform(soup)
    all_job_data.extend(page_job_data)

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(all_job_data)

# Print the DataFrame
print(df)


#Step 9: now saving result set to csv file

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q=data+analyst&start={page}&vjk=b7c58b9a5fc8f161'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    job_listings = soup.find_all('div', class_='company_location')  # Find all divs containing company information
    job_titles = soup.find_all('a', class_='jcs-JobTitle')  # Find all job titles

    job_data = []

    for job_info, job_title in zip(job_listings, job_titles):
        # Extract and print job title
        job_title_span = job_title.find('span', id=lambda x: x and x.startswith('jobTitle'))
        job_title_text = job_title_span.text.strip() if job_title_span else "Not available"

        # Extract and print company name
        company_name = job_info.find('span', class_='css-92r8pb')  # Find the span with company name
        company_text = company_name.text.strip() if company_name else "Not available"

        # Extract and print location
        location = job_info.find('div', class_='css-1p0sjhy')  # Find the div with location
        location_text = location.text.strip() if location else "Not available"

        # Create dictionary for job data
        job = {
            'job_title': job_title_text,
            'company': company_text,
            'location': location_text
        }

        # Append job data to list
        job_data.append(job)

    return job_data

# Create an empty list to store all job data
all_job_data = []

# Iterate through the first 10 pages
for i in range(0, 10 * 10, 10):  # Scrape 10 pages, each page has 10 listings
    # Extract data from the current page
    soup = extract(i)
    # Transform the data and append it to the list
    page_job_data = transform(soup)
    all_job_data.extend(page_job_data)

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(all_job_data)

# Save the DataFrame to a CSV file
df.to_csv('job_listings.csv', index=False)

print("CSV file saved successfully!")