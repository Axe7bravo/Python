def get_person_info():
  """Prompts the user for personal information and returns it as a dictionary."""

  person = {}
  person["name"] = input("What is your name? ")
  person["age"] = int(input("How old are you? "))
  person["favorite_color"] = input("What is your favorite color? ")

  return person

def main():
  """Main function to collect and print person's information."""

  person_info = get_person_info()
  print("Person Information:")
  print(person_info)

if __name__ == "__main__":
  main()