def get_words():
  """Prompts the user for words and creates a list."""

  words = []
  while True:
    word = input("Enter a word (or 'done' to finish): ")
    if word.lower() == "done":
      break
    words.append(word)

  return words

def filter_odd_length_words(words):
  """Filters words with odd length using list comprehension."""

  odd_length_words = [word for word in words if len(word) % 2 != 0]
  return odd_length_words

def main():
  """Main function to create and filter word lists."""

  word_list = get_words()

  odd_word_list = filter_odd_length_words(word_list)

  print("Words with odd length:", odd_word_list)

if __name__ == "__main__":
  main()