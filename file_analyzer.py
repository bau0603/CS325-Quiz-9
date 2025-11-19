from collections import Counter

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    return len(text)

def find_most_common_word(text):
    words = text.split()
    word_counts = Counter(words)
    if word_counts == {}:
        return "(Empty String)"
    return word_counts.most_common(1)[0][0] 