import sys
from textblob import TextBlob
text = '''My book is about a wizard named Jergus. At first he is thought to be a bad guy. But we see a lot of things happen in the book and eventually we realize he is a good guy. He then has to fight the bad guy and save the day.'''

lang = sys.argv[1]

text = input('what would you like to translate')
print(text)
print(lang)
blob = TextBlob(text)
translation = blob.translate(to=lang)
print(translation)
from subprocess import call
call(['espeak', '-v', lang, str(translation)])


