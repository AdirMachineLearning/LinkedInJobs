# LinkedInJobs Scraper - Adir Leibovici

## Overview
LinkedInJobs is a Python class that automates the scraping of job listings from LinkedIn based on user-defined job titles and locations. The class effectively gathers data, such as job titles, companies, and locations, and further processes this information to categorize job titles into standardized forms.

## Features
**Job Fetching**: Automatically fetches job listings from LinkedIn for specified job titles and locations.
**Pagination Handling**: Manages multiple pages of job listings to gather comprehensive job data.
**Data Standardization**: Implements a cleaning function to standardize job titles based on common industry keywords.
**DataFrame Output**: Outputs the job data into a pandas DataFrame for easy analysis and manipulation.

## Dependencies
To run the LinkedInJobs scraper, you need Python installed on your machine along with the following packages:

**requests:** For making HTTP requests.
**beautifulsoup4:** For parsing HTML content.
**pandas:** For data manipulation and storage.
**math:** For basic mathematical operations.
**re:** For regular expression operations.

## Installation
Ensure Python is installed on your system and install the required Python packages using pip:

pip install requests beautifulsoup4 pandas
Usage
To use the LinkedInJobs scraper, instantiate the class with the desired job title, location, and the number of jobs to fetch. Here's a simple example to get started:

from LinkedInJobs import LinkedInJobs

# Initialize the scraper
job_scraper = LinkedInJobs('data scientist', 'Israel', 700)

# Fetch and clean job data
df_jobs = job_scraper.get_jobs()
df_cleaned = job_scraper.clean_names()

print(df_cleaned)
Note
The functionality of this scraper is dependent on the structure of LinkedIn's job pages. Any changes to LinkedIn's HTML structure may require adjustments to the scraper code.
Please ensure that you use this script responsibly and ethically, considering LinkedIn's terms of service regarding data scraping.



## Usage
To use the LinkedInJobs scraper, instantiate the class with the desired job title, location, and the number of jobs to fetch. Here's a simple example to get started:
``` python
from LinkedInJobs import LinkedInJobs

# Initialize the scraper
job_scraper = LinkedInJobs('data scientist', 'Israel', 700)

# Fetch and clean job data
df_jobs = job_scraper.get_jobs()
df_cleaned = job_scraper.clean_names()

print(df_cleaned)

```
## Example Output

The DataFrame will contain the following columns:

- **Title**: The job title.
- **Company**: The company offering the job.
- **Location**: The job location.
- **Link**: A direct link to the job posting on LinkedIn.
- **Cleaned Title**: The standardized job title based on common industry keywords.

