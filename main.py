from stats import count_words, count_characters, sort_char_counts

def main() :
    book_path = "books/frankenstein.txt"
    book_content = get_book_test(book_path)
    text = get_book_test("./books/frankenstein.txt")

#    print the book content
#    print(book_content)

    # header
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {book_path}...")
# Print the word count

    # word count section
    print("-" * 11 + " Word Count " + "-" * 11)

    word_count = count_words(text)
    print(f"Found {word_count} total words")


#   print the charachter count
    print("-" * 9 + " Character Count " + "-" * 8)
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
