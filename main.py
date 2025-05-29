from stats import get_num_words, get_num_symbols, report
import sys
book = None
def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
        return book

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    except FileNotFoundError:
        print("Non - existent file!")

    book = get_book_text(sys.argv[1])
    
    num_words = get_num_words(book)

    char_list = get_num_symbols(book)
    
    report_list = report(book)
    
    print_report(book, report_list, char_list, num_words)
    
def print_report(book, report_list, char_list, num_words):
    print(f"""============ BOOKBOT ============
Analyzing book...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count ----------""")
    for i in report_list:
        print(i["char"] + ": " + str(i["num"]))
    print('''============= END ===============''')
main()
