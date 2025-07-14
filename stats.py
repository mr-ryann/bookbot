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

def sort_key(d):
    return d['num']

def sorted_dict(d):
    l=[]
    for data in d:
        if data.isalpha():
            dict={"char":data,"num":d[data]}
            l.append(dict)
    l.sort(reverse=True,key=sort_key)
    return l
        
        
    

