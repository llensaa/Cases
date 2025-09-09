from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator

text = input()
language = detect(text)
if language != 'en':
    text = GoogleTranslator(source='auto', target='en').translate(text)

blob = TextBlob(text)
polarity, subjectivity = blob.sentiment

if -1 <= polarity < -0.6:
    tone = 'негативная'
elif 0.6 < polarity <= 1:
    tone = 'позитивная'
else:
    tone = 'нейтральная'

objectivity = int(100 * (1 - subjectivity))

print(f'Тональность текста: {tone}')
print(f"Объективность: {objectivity}%")