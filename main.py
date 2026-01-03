import sys
from stats import get_num_words, get_char_count, sort_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content


def main():
    print("Usage: python3 main.py <path_to_book>")

    try:
        file_name = sys.argv[1]
    except Exception:
        sys.exit(1)

    file_path = f"./{file_name}"

    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_chars = sort_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["name"].isalpha():
            print(f"{char["name"]}: {char["num"]}")
    print("============= END ===============")


main()
