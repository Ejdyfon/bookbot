from stats import get_word_count, count_characters, get_sorted_count
import sys

def get_book_text(file_path):
    with open(file_path) as f:
       return f.read()
    
def main():
   if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   book_path = sys.argv[1]
   book_text = get_book_text(book_path)
   num_words = get_word_count(book_text)
   #print(f"{num_words} words found in the document")
   char_count = count_characters(book_text)
   #print(char_count)

   sorted_chars = get_sorted_count(char_count)

   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_path}...")
   print("----------- Word Count ----------")
   print(f"Found {num_words} total words")
   print("--------- Character Count -------")
   for sc in sorted_chars:
      if sc["char"].isalpha():
         print(f"{sc["char"]}: {sc["num"]}")
   print("============= END ===============")


main()
