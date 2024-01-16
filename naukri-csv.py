import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/content/job_data.csv')

# Extract the 'Reviews' from the 'Company Name' column
df['Reviews'] = df['Company Name'].str.extract(r'(\d+\.\d+)')

# Remove extra characters and "Reviews" from the 'Company Name' column
df['Company Name'] = df['Company Name'].str.replace(r"[^a-zA-Z\s]", "").str.replace(r"Reviews", "").str.strip()

# Remove extra characters from other columns
columns_to_clean = ['Location', 'Job Description', 'Job role', 'Education']

for column in columns_to_clean:
    df[column] = df[column].str.replace(r"[^a-zA-Z\s]", "").str.strip()

# Remove square brackets and single quotes from the 'Key Skill' column
df['Key Skill'] = df['Key Skill'].str.replace(r"[\[\]']", "").str.strip()

# Extract number of applicants from 'Job Openings' and create 'Applicants' column
df['Applicants'] = df['Job Openings'].str.extract(r'Applicants:\s*(\d+)', expand=False)
df['Applicants'] = pd.to_numeric(df['Applicants'], errors='coerce')  # Convert to numeric, handle NaN

# Extract number of openings from 'Job Openings' and create 'Openings' column
df['Openings'] = df['Job Openings'].str.extract(r'Openings:\s*(\d+)', expand=False)
df['Openings'] = pd.to_numeric(df['Openings'], errors='coerce')  # Convert to numeric, handle NaN

# Remove unnecessary text from 'Job Openings' column
df = df.drop(columns=['Job Openings'])
# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_data.csv', index=False)