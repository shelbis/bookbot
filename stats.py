import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count():
    words = get_book_text(sys.argv[1]).split()
    total_words = len(words)
    text = f"Found {total_words} total words"
    return text

def count_characters():
    count = 1
    dictionary = {}
    text = get_book_text(sys.argv[1])
    for letter in text:
        letter = letter.lower()
        if letter not in dictionary:
            dictionary[letter] = count
        else:
            current_count = dictionary[letter]
            current_count += 1
            dictionary[letter] = current_count
    return dictionary

def sort_on(items):
    return items["num"]

def list_of_dictionaries():
    character_count = []
    dictionary = count_characters()
    for letter in dictionary:
        temporary_dictionary = {}
        temporary_dictionary["char"] = letter
        temporary_dictionary["num"] = dictionary[letter]
        character_count.append(temporary_dictionary)
    character_count.sort(reverse=True, key=sort_on)
    return character_count

def print_dictionary():
    for dictionary in list_of_dictionaries():
        letter = dictionary["char"]
        number = dictionary["num"]
        print(f"{letter}: {number}")
    return
        
def check():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def report():
    check()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_count())
    print("--------- Character Count -------")
    print_dictionary()
    print("============= END ===============")