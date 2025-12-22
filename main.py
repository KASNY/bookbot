import sys
from stats import get_num_words, count_characters, chars_dict_to_sorted_list
def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = count_characters(book_text)
    sported_chars = chars_dict_to_sorted_list(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path + "...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sported_chars:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
        
    print("============= END ===============")


    
main()