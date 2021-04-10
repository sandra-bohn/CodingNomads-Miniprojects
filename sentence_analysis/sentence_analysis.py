'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.

**Note**: ignore all spaces.
'''

# Get sentence
sentence = input("Enter a sentence: ")
sentence = sentence.replace(" ", "")
# Make list of characters in sentence
characters = list(sentence)
# number of lower and upper case letters
lowers = 0
uppers = 0
for letter in characters:
    if letter.islower():
        lowers += 1
    elif letter.isupper():
        uppers += 1
sentdict = {'Upper case': uppers, 'Lower case': lowers}

# total number of characters
total = len(characters)
# the number of punctuations characters
puncs = total - lowers - uppers
sentdict['Punctuation'] = puncs
sentdict['Total chars'] = total

print(sentdict)
