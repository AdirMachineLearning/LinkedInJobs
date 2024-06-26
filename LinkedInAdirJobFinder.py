#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

class LinkedInJobs():
    """
    A class to scrape job listings from LinkedIn based on specified job titles and locations.
    
    Attributes:
        job_list (list): A list to store job data dictionaries.
        job_title (str): The job title to search for.
        location (str): The geographic location for the job search.
        num_jobs (int): The total number of jobs to fetch.
        jobs_per_page (int): Number of jobs listings per page.
        num_pages (int): Total number of pages to scrape, calculated from num_jobs.
        dataframe_jobs (DataFrame): A pandas DataFrame to store job data.
        headers (dict): HTTP headers used for making requests.
    """

    def __init__(self, job_title, location, num_jobs):
        """
        Constructs all the necessary attributes for the LinkedInJobs object.
        
        Parameters:
            job_title (str): The job title to search for.
            location (str): The geographic location for the job search.
            num_jobs (int): The total number of jobs to fetch.
        """
        self.job_list = []
        self.job_title = job_title
        self.location = location
        self.num_jobs = num_jobs
        self.jobs_per_page = 25
        self.num_pages = math.ceil(num_jobs / self.jobs_per_page)
        self.dataframe_jobs = None
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

    def get_jobs(self):
        """
        Fetches job listings from LinkedIn and stores them in a DataFrame.
        
        Returns:
            DataFrame: A DataFrame containing job listings with titles, companies, and locations.
        """
        for page in range(self.num_pages):
            offset = page * self.jobs_per_page
            response = requests.get(
                f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={self.job_title}&location={self.location}&start={offset}',
                headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            job_listings = soup.find_all('li')
            for job in job_listings:
                title = job.find('h3', {'class': 'base-search-card__title'}).get_text(strip=True) if job.find('h3', {'class': 'base-search-card__title'}) else None
                company = job.find('h4', {'class': 'base-search-card__subtitle'}).get_text(strip=True) if job.find('h4', {'class': 'base-search-card__subtitle'}) else None
                location = job.find('span', {'class': 'job-search-card__location'}).get_text(strip=True) if job.find('span', {'class': 'job-search-card__location'}) else None
                link = job.find('a', {'class': 'base-card__full-link'})['href'] if job.find('a', {'class': 'base-card__full-link'}) else None
                self.job_list.append({'Title': title, 'Company': company, 'Location': location, 'Link': link})
        self.dataframe_jobs = pd.DataFrame(self.job_list)
        return self.dataframe_jobs

    def clean_names(self):
        """
        Cleans job titles in the DataFrame to standardize them based on predefined keywords.
        
        !!!!Remember to change the jobs names claening based on your needs!!!!
        
        Returns:
            DataFrame: The updated DataFrame with an additional column 'Cleaned Title' containing standardized job titles.
        """
        standard_titles = {
            'Data scientist': r'\bdata scientist\b',
            'Data science': r'\bdata science\b',
            'Data engineer': r'\bdata engineer\b',
            'Deep learning': r'\bdeep learning\b',
            'Machine learning engineer': r'\bmachine learning engineer\b',
            'Machine learning': r'\bmachine learning\b',
            'Data analyst': r'\bdata analyst\b',
            'Software Developer': r'\bsoftware developer\b',
            'Software Engineer': r'\bsoftware engineer\b',
            'ML Ops': r'\bml ops\b',
            'AI': r'\bai\b',
            'Data architect': r'\bdata architect\b',
            'AI engineer': r'\bai engineer\b',
            'NLP': r'\bnlp\b',
        }

        def clean_title(title):
            title = title.lower() 
            for standard, pattern in standard_titles.items():
                if re.search(pattern, title):
                    return standard  
            return title  

        self.dataframe_jobs['Cleaned Title'] = self.dataframe_jobs['Title'].apply(clean_title)
        return self.dataframe_jobs


# Define the job title, location, and number of jobs to scrape
job_title = 'data scientist'
location = 'Israel'
num_jobs = 10

job_scraper = LinkedInJobs(job_title, location, num_jobs)
df_class = job_scraper.get_jobs()
df_cleaned = job_scraper.clean_names()
pd.options.display.max_rows = None
display(df_cleaned)


# In[ ]:




