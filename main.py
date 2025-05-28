from stats import count_words, count_characters, sort_char_counts

def main() :
    book_content = get_book_test("./books/frankenstein.txt")
    text = get_book_test("./books/frankenstein.txt")

#    print the book content
#    print(book_content)


# Print the word count

    word_count = count_words(text)
    print(f"{word_count} words found in the document")

#   print the charachter count
    char_count = count_characters(text)
    print(char_count)

    sorted_chars = sort_char_counts(char_count)

    for entry in sorted_chars:
        print (f"{entry['char']}: {entry['num']}")


def get_book_test(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    main()
