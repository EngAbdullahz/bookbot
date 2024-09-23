def count_words(text):
    sep = text.split()
    cnt = len(sep)
    return cnt


def count_char(text):
    char_dict = {}
    strings = text.lower()
    for char in strings:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict


file_path = "books/frankenstein.txt"
with open(file_path) as f:
    text = f.read()
    char_dict = count_char(text)
    char_list = sorted(char_dict, key=char_dict.get, reverse=True)
    word_count = count_words(text)
    print("--- Begin report of " + file_path + " ---\n")
    print(f"{word_count} was found in the document\n")
    for char in char_list:
        if char.isalpha():
            print(f"The {char} character was found {char_dict[char]} times")
    print("--- End report ---")
