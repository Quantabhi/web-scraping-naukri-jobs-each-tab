# Import necessary libraries
from playwright.sync_api import sync_playwright
from urllib.parse import urlparse
import csv
import time

# Parse the proxy URL
proxy_url = urlparse("http://add your proxie details")

# Extract the username and password
username = proxy_url.username
password = proxy_url.password

# Extract the host and port
host = proxy_url.hostname
port = proxy_url.port

# Function to handle job search
def handle_job_search():
    # List to store job data
    jobs_data = []

    # Set up Playwright and launch the Chromium browser
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            proxy={
                "server": f"http://{host}:{port}",
                "username": username,
                "password": password
            }
        )
        # Create a new browser context and open a new page
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the job search page on naukri.com
        page.goto('https://www.naukri.com/fresher-jobs-10')
        page.wait_for_load_state('networkidle')

        # Loop through a specified number of pages
        for _ in range(3):  # Loop for two pages (you can adjust the number as needed)
            # Select job elements on the current page
            job_elements = page.query_selector_all('div.row1')

            # Loop through each job element
            for job_element in job_elements:
                try:
                    # Simulate a Ctrl+Click to open the details in a new tab
                    job_element.click(button='middle') 

                    # Wait for the new tab to open
                    new_page = context.wait_for_event('page')
                    new_page.wait_for_load_state('networkidle')

                    # Extract job details from the new tab
                    main_div = new_page.locator('section.styles_job-header-container___0wLZ').all()
                    for divs in main_div:
                        job_title = divs.locator('h1.styles_jd-header-title__rZwM1').inner_text()
                        company_name = divs.locator('div.styles_jd-header-comp-name__MvqAI').all_text_contents()
                        location = divs.locator('span.styles_jhc__location__W_pVs').all_text_contents()
                        job_description = new_page.locator('div.styles_JDC__dang-inner-html__h0K4t').all_text_contents()
                        job_Openings = divs.locator('div.styles_jhc__jd-stats__KrId0').all_text_contents()
                        job_role = new_page.locator('div.styles_other-details__oEN4O').all_text_contents()
                        Education = new_page.locator('div.styles_education__KXFkO').all_text_contents()
                        Key_Skill = new_page.locator('div.styles_key-skill__GIPn_').all_text_contents()

                        # Append job data to the list
                        jobs_data.append([job_title, company_name, location, job_description, job_Openings, job_role,Education, Key_Skill])

                    # Close the new tab
                    new_page.close()
                except Exception as e:
                    print(f"Error processing job: {e}")

            # Check if there is a next page
            next_page_button = page.query_selector('a.styles_btn-secondary__2AsIP:has-text("Next")')
            if not next_page_button:
                break  # Exit the loop if there is no next page

            # Click on the next page button
            next_page_button.click()
            page.wait_for_load_state('networkidle')
            time.sleep(1)  # Add a delay to ensure the page loads completely

        # Close the main browser context
        context.close()
        browser.close()

    # Save data to CSV file
    with open('job_data_two.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(['Job Title', 'Company Name', 'Location', 'Job Description', 'Job Openings', 'Job role','Education', 'Key Skill'])
        # Write data rows
        csv_writer.writerows(jobs_data)

# Execute the job search function if the script is run as the main module
if __name__ == '__main__':
    handle_job_search()
