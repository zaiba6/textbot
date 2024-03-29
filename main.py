from twilio.rest import Client
from nltk.corpus import wordnet
from PyDictionary import PyDictionary
from random_word import RandomWords
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Your Twilio Account SID and Auth Token

client = Client(account_sid, auth_token)

# Number
twilio_numb = "+18194141979"

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

#["+16478314674"]
#["+16478314674", "+16476189047", "+16472212722", "+14167069714"]

r = RandomWords()
dictionary = PyDictionary()

word = "Ephemeral"
phenotic = "(e·phem·er·al)"

Sentence = "That shordy is straight ephemeral, here today, ghostin' tomorrow." 

# Get the meanings of the word from PyDictionary
definition = dictionary.meaning(word)

# Check if definition exists and format the meaning
if definition:
    # Get the part of speech using NLTK WordNet
    synsets = wordnet.synsets(word)
    if synsets:
        pos = synsets[0].pos()
        # Ensure the part of speech is in the expected format
        if pos == 'n':
            pos = 'Noun'
        elif pos == 'v':
            pos = 'Verb'
        elif pos == 'a':
            pos = 'Adjective'
        elif pos == 'r':
            pos = 'Adverb'
        meaning = f"{word} {phenotic}\n\n{pos}: {', '.join(definition.get(pos, ['Definition not found']))}"
        #print(meaning)
else:
    meaning = f"{word}: No word for today, sorry :')"


sendout = f"Word of the day!\n\n{meaning}\n\n{Sentence}"
print (sendout)


# Send SMS to each recipient
for recipient in receiving_num:
    message = client.messages.create(
        to=recipient,
        from_=twilio_numb,
        body= sendout
    )
    print("SMS sent to", recipient)
print("SMS successfully sent to all recipients")
