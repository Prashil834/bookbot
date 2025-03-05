import sys
from stats import get_char_count, get_num_words

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  

    try:
        words = get_book_text(book_path)  
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)

    num_words = get_num_words(words)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")  

    print("--------- Character Count -------")
    char_counts = get_char_count(words)

    for item in char_counts:
        print(f"{item['character']}: {item['count']}")  
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
