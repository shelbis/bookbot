def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count():
    words = get_book_text("./books/frankenstein.txt").split()
    total_words = len(words)
    text = f"Found {total_words} total words"
    return text

def main():
    print(word_count())

main()