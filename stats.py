def get_num_words(book_content):
    word_count = 0
    words = book_content.split()

    for word in words:
        word_count += 1

    return word_count


def get_char_count(book_content):
    char_dict = {}

    for char in book_content:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
            continue

        char_dict[char.lower()] = 1

    return char_dict


def sort_helper(char):
    return char["num"]


def sort_chars(char_dict):
    char_list = []

    for char in char_dict:
        char_list.append({"name": char, "num": char_dict[char]})

    char_list.sort(reverse=True, key=sort_helper)

    return char_list
