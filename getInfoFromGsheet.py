import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheets document by its title
spreadsheet = client.open('phoneNumResponses')

# Access a specific worksheet
worksheet = spreadsheet.get_worksheet(0)  # Index 0 refers to the first worksheet

# Example: Read data from column B
column_b_values = worksheet.col_values(2)  # 2 corresponds to column B (indexing starts from 1)

# Remove the first row (header row)
column_b_values = column_b_values[1:]

# Print the values from column B
print(column_b_values)

'''# Example: Read data from the worksheet
data = worksheet.get_all_values()
print(data)'''