import sys
def get_num_words(words):
    word=words.split()
    return len(word)

def get_char_count(text):
    char_count={}
    text=text.lower()

    for char in text:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    
    return sorted_char_counts(char_count)

def sorted_char_counts(char_count):
    sorted_list=[{"character":char,"count":count} for char,count in char_count.items()]
    sorted_list.sort(key=lambda x : x['count'],reverse=True)
    return sorted_list