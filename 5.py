string = 'мама мыла раму'
sorted_words = sorted(string.split(), key=lambda x: (len(x), x.lower()))
print(sorted_words)

string = 'Яндекс использует Python во многих проектах'
sorted_words = sorted(string.split(), key=lambda x: (len(x), x.lower()))
print(sorted_words) 