# LinkedInJobs Scraper - Adir Leibovici

## Overview
`LinkedInJobs` is a Python class designed to scrape job listing information from LinkedIn based on specified job titles and locations. It collects job listings and stores details such as job titles, companies, and locations into a DataFrame, which can be useful for analysis or job market research.

## Features
- Fetch job listings from LinkedIn for a given job title and location.
- Pagination support to handle multiple pages of job listings.
- Collect job information into a pandas DataFrame for easy manipulation and display.

## Dependencies
- `requests`: To make HTTP requests to LinkedIn's job listing pages.
- `beautifulsoup4`: To parse HTML content and extract data.
- `pandas`: To store and manipulate the fetched job data in a DataFrame.
- `math`: For calculating the number of pages based on the number of jobs.

## Installation

Before you can use the `LinkedInJobs` class, ensure you have Python installed on your system, then install the required packages:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage
Here is a simple example of how to use the LinkedInJobs class to fetch job listings for "data scientist" positions in "Israel":

``` python
from LinkedInJobs import LinkedInJobs

# Create an instance of LinkedInJobs
job_scraper = LinkedInJobs(job_title="data scientist", location="Israel", numjob=700)

# Fetch job listings and display them
df_jobs = job_scraper.get_jobs()
display(df_jobs)
```
## Notes
This scraper relies on the structure of LinkedIn's job listing pages. Changes to LinkedIn's page layout may require updates to the scraper code.
Use this script responsibly to avoid violating LinkedIn's terms of service.
