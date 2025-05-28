from stats import count_words

def main() :
    book_content = get_book_test("./books/frankenstein.txt")
    text = get_book_test("./books/frankenstein.txt")
    word_count = count_words(text)
    print(f"{num_words} words found in the document")

#    print(book_content)

def get_book_test(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    main()
