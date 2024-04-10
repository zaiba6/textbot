from twilio.rest import Client
from nltk.corpus import wordnet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from WordFromExcel import sendout

# Your Twilio Account SID and Auth Token
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Number
twilio_numb = " "

###### User Numbers #######

# Define the scope and credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client_gspread = gspread.authorize(creds)

# Open the Google Sheets document by its title
spreadsheet = client_gspread.open('phoneNumResponses')

# Access a specific worksheet
worksheet = spreadsheet.get_worksheet(0)  # Index 0 refers to the first worksheet

# Example: Read data from column B
column_b_values = worksheet.col_values(2)  # 2 corresponds to column B (indexing starts from 1)

# Remove the first row (header row)
column_b_values = column_b_values[1:]

# Receiving numbers
receiving_num = column_b_values

# Send SMS to each recipient
for recipient in receiving_num:
    message = client.messages.create(
        to=recipient,
        from_=twilio_numb,
        body= sendout
    )
    print("SMS sent to", recipient)
print("SMS successfully sent to all recipients")
