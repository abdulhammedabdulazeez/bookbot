import sys
from stats import get_book_text, count_words, count_char, sort_char

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    
    word_count = count_words(book)
    
    char_dict = count_char(book)

    sorted = sort_char(char_dict)
    # print(char_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in sorted:
        output = f"{char["char"]}: {char["num"]}"
        print(output)

    print("============= END ===============")




main()