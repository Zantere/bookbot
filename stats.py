def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counts = {}
    for char in text.lower():
        counts(char) = counts.get(char, 0) + 1
    return counts