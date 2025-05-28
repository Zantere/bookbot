def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_char_counts(char_dict):
    items = [
        {"char": c, "num": count}
        for c, count in char_dict.items() if 
        c.isalpha()
    ]
    items.sort(key=lambda x: x["num"], reverse=True)

    return items