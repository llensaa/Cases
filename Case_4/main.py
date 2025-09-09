from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator

text = input()
language = detect(text)
if language != 'en':
    text = GoogleTranslator(source='auto', target='en').translate(text)

blob = TextBlob(text)

polarity, subjectivity = blob.sentiment

print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")