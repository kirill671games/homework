import pandas as pd
import string

def length_stats(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))
    words = text.split()
    length_dict = {word: len(word) for word in words}
    length_series = pd.Series(length_dict).sort_index()
    return length_series
print(length_stats('Мама мыла раму'))