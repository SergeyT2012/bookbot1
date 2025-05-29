from stats import get_num_symbols, get_num_words, report
from main import get_book_text, main

def main():
    book = get_book_text("books/frankenstein.txt")
    print("Book length:", len(book))
    print("First 100 characters:", book[:100])
    
    char_list = get_num_symbols(book)
    print("Character list length:", len(char_list))
    print("First few items:", list(char_list.items())[:5])
    
    list = report(book)
    print("Final list length:", len(list))
    print(list)