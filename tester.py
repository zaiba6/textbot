import random
from nltk.corpus import wordnet
from nltk.corpus import words
from nltk import pos_tag

# Code to generate random words and their definitions
word_list = words.words()

def get_random_word_definition():
    while True:
        random_word = random.choice(word_list)
        synsets = wordnet.synsets(random_word)
        if synsets:
            synonyms = []  # Clearing synonyms list for each word
            term = random_word
            meaning = synsets[0].definition()
            for syn in wordnet.synsets(random_word):
                for l in syn.lemmas():
                    synonyms.append(l.name())
            # Get part-of-speech tags for the random word
            pos_tags = pos_tag([term])
            pos_tag_word = pos_tags[0][1]
            # Determine if the word is singular or plural
            if pos_tag_word.startswith('N'):  # Nouns
                singular_or_plural = 'Singular' if wordnet.synset(synsets[0].name()).lemmas()[0].count() == 1 else 'Plural'
            else:
                singular_or_plural = ''
            # Determine if the word is a verb or adjective
            if pos_tag_word.startswith('V'):
                pos_description = 'Verb'
            elif pos_tag_word.startswith('J'):
                pos_description = 'Adjective'
            else:
                pos_description = ''
            return f"{term}: {meaning}, Synonyms: {', '.join(set(synonyms))}, {singular_or_plural}, {pos_description}"

# Example usage
print(get_random_word_definition())
