import re
import ru_local as ru
from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator


def total_sen(a):
    '''
    Function, counting sentences
    :param a: text
    :return: counter
    '''
    counter = 1  # Counting last sentence, without space.
    for i in range(len(a)):
        if a[i - 1] + a[i] in ['. ', '! ', '? '] and i > 1:
            counter += 1
    return counter


def total_words(a):
    '''
    Function, counting words
    :param a: text
    :return: number of words
    '''
    a = re.sub(r'[^\w\s]', '', a.lower())
    return len([word for word in a.split() if word])


def total_syllabs(a):
    '''
    Function, counting syllables in text
    :param a: text
    :return: number of syllables
    '''
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
    '''
    Function, counting average number of syllables per word
    :param a: text
    :return: asw
    '''
    b = total_words(a)
    c = total_syllabs(a)
    return c / b


def asl(a):
    '''
    Function, counting average number of words per sentence
    :param a: text
    :return: asl
    '''
    b = total_words(a)
    c = total_sen(a)
    return b / c


text = input(f'{ru.ENTER_TEXT}')

language = detect(text)
if language != 'en':
    text_eng = GoogleTranslator(source='auto', target='en').translate(text)
    flesh_index = 206.835 - 1.52 * asl(text) - 65.14 * asw(text)
else:
    text_eng = text
    flesh_index = 206.835 - 1.015 * asl(text) - 84.6 * asw(text)
blob = TextBlob(text_eng)
polarity, subjectivity = blob.sentiment

if -1 <= polarity < -0.34:
    tone = ru.NEGATIVE
elif 0.34 =< polarity <= 1:
    tone = ru.POSITIVE
else:
    tone = ru.NEUTRAL

objectivity = int(100 * (1 - subjectivity))

print(f'{ru.SENTENCES} {total_sen(text)} \n')
print(f'{ru.WORDS} {total_words(text)}\n')
print(f'{ru.SYLLABLES} {total_syllabs(text)}\n')
print(f'{ru.ASL} {asl(text)}\n')
print(f'{ru.ASW} {asw(text)}\n')
print(f'{ru.FLASH} {flesh_index}\n')
if flesh_index >= 100:
    print(f'{ru.EASY_TO_READ}.\n')
elif 65 <= flesh_index < 100:
    print(f'{ru.EASY_TO_READ} ({ru.JUNIOR}).\n')
elif 30 <= flesh_index < 65:
    print(f'{ru.QUITE_TOUGH}.\n')
else:
    print(f'{ru.TOUGH}.\n')
print(f'{ru.POLARITY} {tone}\n')
print(f"{ru.OBJECTIVITY} {objectivity}%\n")
