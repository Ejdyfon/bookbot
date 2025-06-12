def get_word_count(text):
   return len(text.split())

def count_characters(text):
   counted_chars = {}
   for i in text:
    char = i.lower()
    if char in counted_chars:
       counted_chars[char] += 1
    else:
       counted_chars[char] = 1

   return counted_chars

def sort_on(dict):
    return dict["num"]

def get_sorted_count(char_dict):
   char_list = []

   for char in char_dict:
      item = {"char": char, "num": char_dict[char]}
      char_list.append(item)

   char_list.sort(reverse=True,key=sort_on)

   return char_list