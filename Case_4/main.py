import re
from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator


def total_sen(a):
    counter = 1  # учитывая последнее предложение, без пробела
    for i in range(len(a)):
        if ((a[i - 1] + a[i] == '. ') or \
            (a[i - 1] + a[i] == '! ') or \
            (a[i - 1] + a[i] == '? ')) \
                and i > 1:
            counter += 1
    return counter


def total_words(a):
    a = re.sub(r'[^\w\s]', '', text.lower())
    return len([word for word in a.split() if word])


def total_syllabs(a):
    total_syllables = len([x for x in a if x.lower() in ['a', 'y',
                                                         'u', 'e',
                                                         'o', 'i',
                                                         'а', 'е',
                                                         'и', 'о',
                                                         'я', 'ы',
                                                         'э', 'у',
                                                         'ё', 'ю']])
    return total_syllables


def asw(a):
    b = total_words(a)
    c = total_syllabs(a)
    return c / b


def asl(a):
    b = total_words(a)
    c = total_sen(a)
    return b / c


text = input(f'Введите текст: ')

language = detect(text)
if language != 'en':
    text_eng = GoogleTranslator(source='auto', target='en').translate(text)
    flesh_index = 206.835 - 1.52 * asl(text) - 65.14 * asw(text)
else:
    text_eng = text
    flesh_index = 206.835 - 1.015 * asl(text) - 84.6 * asw(text)
blob = TextBlob(text_eng)
polarity, subjectivity = blob.sentiment

if -1 <= polarity < -0.6:
    tone = 'негативная'
elif 0.6 < polarity <= 1:
    tone = 'позитивная'
else:
    tone = 'нейтральная'

objectivity = int(100 * (1 - subjectivity))

print(f'Предложений: {total_sen(text)}')
print(f'Слов: {total_words(text)}')
print(f'Слогов: {total_syllabs(text)}')
print(f'Средняя длина предллжения в словах: {asl(text)}')
print(f'Средняя длина слова в слогах: {asw(text)}')
print(f'Индекс удобочитаемости Флеша: {flesh_index}')

print(f'Тональность текста: {tone}')
print(f"Объективность: {objectivity}%")
