def count_words(string):
    words = string.split()
    return len(words)

def character_count(string):
    d={}
    for x in string:
        y=x.lower()
        if y not in d:
            d[y] = 1
        else:
            d[y] += 1
    return d
