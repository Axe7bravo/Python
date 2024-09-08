import json
import difflib

def load_dictionary(filename):
  """Loads a JSON file into a Python dictionary.

  Args:
      filename (str): The name of the JSON file.

  Returns:
      dict: A dictionary containing the contents of the JSON file.
  """

  with open(filename, 'r') as f:
      return json.load(f)

def get_definition(dictionary, word):
  """Gets the definition of a word from a dictionary.

  Args:
      dictionary (dict): A dictionary containing word definitions.
      word (str): The word to look up.

  Returns:
      str: The definition of the word, or None if not found.
  """

  word = word.lower()  # Convert word to lowercase
  definition = dictionary.get(word)
  if not definition:
      # Check for spelling errors
      closest_match = difflib.get_close_matches(word, dictionary.keys(), n=1)
      if closest_match:
          print(f"Did you mean '{closest_match[0]}'?")
          definition = dictionary.get(closest_match[0])
  return definition

def main():
  dictionary = load_dictionary('data.json')
  while True:
      word = input("Enter a word to look up (or 'end program' to exit): ")
      if word.lower() == 'end program':
          break
      definition = get_definition(dictionary, word)
      if definition:
          print(definition)
      else:
          print("Word not found.")

if __name__ == '__main__':
  main()