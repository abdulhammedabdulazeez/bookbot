def get_book_text(file_path):

    with open(file_path) as f:
        text = f.read()
    return text

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_dict = {}

    for char in text:
        char_lower = char.lower()
        count = char_dict.get(char_lower, 0)
        char_dict[char_lower] = count + 1 

    return char_dict


def sort_on(items):
    return items["num"]

def sort_char(char_dict):
    char_list = []

    for char in char_dict:
        if char.isalpha():
            char_obj = {
                "char": char,
                "num": char_dict[char]
            }

            char_list.append(char_obj)

    char_list.sort( key=sort_on, reverse=True )

    return char_list
    
