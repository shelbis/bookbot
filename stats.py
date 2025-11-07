def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count():
    words = get_book_text("./books/frankenstein.txt").split()
    total_words = len(words)
    text = f"Found {total_words} total words"
    return text

def count_characters():
    count = 1
    dictionary = {}
    text = get_book_text("./books/frankenstein.txt")
    for letter in text:
        letter = letter.lower()
        if letter not in dictionary:
            dictionary[letter] = count
        else:
            current_count = dictionary[letter]
            current_count += 1
            dictionary[letter] = current_count
    return dictionary