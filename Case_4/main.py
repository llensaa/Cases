from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator


def total_sen(a):
    counter = 0
    for i in range(len(a)):
        if (a[i] + a[i - 1] == '?!') or (a[i] + a[i - 1] == '!?') and i > 1:
            counter += 1
        elif a[i] in ['.', '!', '?']:
            counter += 1
    return counter


def total_words(a):
    return len(a.strip())


def asw(a):
    b = total_words(a)
    total_syllables = len([x for x in a if x.lower() in ['a', 'y',
                                                       'u', 'e',
                                                       'o', 'i',
                                                       'а', 'е',
                                                       'и', 'о',
                                                       'я', 'ы',
                                                       'э', 'у'
                                                            'ё', 'ю']])
    return total_syllables // b


def asl(a):
    b = total_words(a)
    c = total_sen(a)
    return b // c


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
