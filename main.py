from twilio.rest import Client
import random
from nltk.corpus import wordnet
from nltk.corpus import words


client = Client(account_sid, auth_token)

#number
twilio_numb ="+18194141979"

#recieveing number
recieveing_num = ["+16478314674", "+16476189047"]


#code to generate random words and their definitions
word_list = words.words()

#synonyms = []


def get_random_word_definition():
      while True:
        random_word = random.choice(word_list)
        synsets = wordnet.synsets(random_word)
        if synsets:
          term = random_word
          meaning = synsets[0].definition() 
          return f"{term}: {meaning}"

#print (get_random_word_definition())

        # for syn in wordnet.synsets(random_word):
        #     for l in syn.lemmas():
        #         synonyms.append(l.name())

for recipiants in recieveing_num:   
    message = client.messages.create(
        to = recipiants,
        from_ = twilio_numb, 
        body = get_random_word_definition()
    )

print("sms sucess", message.sid)

