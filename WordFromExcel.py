import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

###### User Numbers #######

# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client_gspread = gspread.authorize(creds)

# Open the Google Sheets document by its title
spreadsheet = client_gspread.open('VocabWordslist')

# Access a specific worksheet
worksheet = spreadsheet.get_worksheet(0)  # Index 0 refers to the first worksheet

# Example: Read data from column A
column_a_values = worksheet.col_values(1)  # 2 corresponds to column B (indexing starts from 1)
# Assuming today's date
today_date = str(datetime.date.today())

# Check if today's date is present in column A values
if any(today_date in i for i in column_a_values):
    # Find the index of the row where today's date is located
    row_index = column_a_values.index(today_date) + 1
    
    # Retrieve the values of the row
    row_values = worksheet.row_values(row_index)
    
    # Print the values of each cell in the row
  # Print the position and value of each cell in the row
    for position, value in enumerate(row_values, start=1):
        if position == 2:
            word = value
        if position == 3:
            pheonetic = value
        if position == 4:
            Type = value
        if position == 5: 
            Definition = value
        if position == 6:
            sentence = value
    sendout = (f"Word of the day!\n\n{word} {pheonetic}\n\n{Type}: {Definition}\n\n{sentence}")
else:
    print(f'{today_date} is not present in the list')

print (sendout)