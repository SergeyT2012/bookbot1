def sort_on(dict):
    return dict["num"]

def get_num_words(book):
    num_words = len(book.split())
    return num_words
def get_num_symbols(book):
    character_list = {}
    for i in str(book):
        if i.lower() in character_list.keys():
           character_list[i.lower()] += 1
        elif i.lower() not in character_list.keys():
           character_list[i.lower()] = 1

    return character_list
def report(book):
    char_list = get_num_symbols(book)
    report_char_num_list = []
    for i in char_list:
        if i.isalpha():
            report_char_num_list.append({"char" : i, "num" : char_list[i]})
    report_char_num_list.sort(reverse=True,key=sort_on)
    return report_char_num_list
