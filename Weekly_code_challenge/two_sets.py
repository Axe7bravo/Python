def get_integer_set(set_name):
  """Prompts the user for integers to create a set."""

  integer_set = set()
  while True:
    user_input = input(f"Enter an integer for set {set_name} (or 'done' to finish): ")
    if user_input.lower() == "done":
      break
    try:
      integer = int(user_input)
      integer_set.add(integer)
    except ValueError:
      print("Invalid input. Please enter an integer.")

  return integer_set

def find_common_elements(set1, set2):
  """Finds elements common to both sets."""

  common_elements = set1.intersection(set2)
  return common_elements

def main():
  """Main function to create sets and find common elements."""

  set1 = get_integer_set("1")
  set2 = get_integer_set("2")

  common_set = find_common_elements(set1, set2)

  if common_set:
    print("Common elements:", common_set)
  else:
    print("There are no common elements.")
if __name__ == "__main__":
  main()