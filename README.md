# Web Scraping Naukri Jobs (Each Tab)
This Python script utilizes Playwright to perform web scraping of fresher jobs listed on Naukri.com. The script opens each job in a new tab to extract detailed information such as job title, company name, location, job description, job openings, job role, education requirements, and key skills.

# Prerequisites
efore running the script, ensure that you have the following installed:

Python (>=3.6)
Playwright (install using pip install playwright)
# Setup
# Clone the repository
```bash
git clone https://github.com/Quantabhi/web-scraping-naukri-jobs-each-tab.git
```
Change directory to the project folder
```bash
cd web-scraping-naukri-jobs-each-tab
```
Open the script (scrape_naukri_jobs.py) in a text editor to add your proxy details:
proxy_url = urlparse("http://add your proxie details")
Replace "http://add your proxie details" with the actual proxy URL.

# Usage
Run the script using the following command:

python scrape_naukri_jobs.py
The script will open a browser, navigate to the Naukri.com fresher jobs page, and scrape information from each job's details tab. The data will be saved to a CSV file named job_data_two.csv.

Customize
Adjust the loop range in the script (for _ in range(3):) to control the number of pages to scrape.
Modify the CSV file name in the script (with open('job_data_two.csv', 'w', ...) to save the data with a different name.
Note
Ensure that your proxy details are correctly configured to avoid connection issues.
The script may need adjustments if there are changes to the Naukri.com website structure.

# Cleaning Naukri Jobs Data (naukri-csv.py)
This Python script uses the Pandas library to clean and enhance the Naukri jobs data extracted from the job_data.csv file. It performs various cleaning operations on columns such as 'Company Name', 'Location', 'Job Description', 'Job role', 'Education', 'Key Skill', and 'Job Openings'.

# Cleaning Operations
Extract Reviews from 'Company Name':

Extract numerical values representing reviews from the 'Company Name' column and create a new 'Reviews' column.
Clean 'Company Name':

Remove extra characters, non-alphabetic characters, and "Reviews" from the 'Company Name' column.
Clean Other Columns:

Apply similar cleaning operations to 'Location', 'Job Description', 'Job role', and 'Education' columns.
Clean 'Key Skill':

Remove square brackets and single quotes from the 'Key Skill' column.
Extract 'Applicants' and 'Openings' from 'Job Openings':

Extract the number of applicants and openings from the 'Job Openings' column and create new 'Applicants' and 'Openings' columns.
Remove 'Job Openings' Column:

Remove the original 'Job Openings' column as it is no longer needed.
Save Cleaned Data:

Save the cleaned DataFrame to a new CSV file named cleaned_data.csv.

## Disclaimer
This script is provided for educational purposes only. Ensure compliance with Naukri.com's terms of service and legal regulations while using web scraping tools.
