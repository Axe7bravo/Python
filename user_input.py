# user_input.py

def get_user_info():
  """
  Prompts the user for their name, age, and location,
  and returns them as a dictionary.

  Returns:
      dict: A dictionary containing the user's name, age (as an integer), and location.
  """
  name = input("What is your name? ")
  while True:
    try:
      age = int(input("How old are you? "))
      if age < 0:
        print("Age cannot be negative. Please enter a valid age:")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter an integer for your age:")
  location = input("Where do you live? ")
  return {"name": name, "age": age, "location": location}

def print_personalized_message(user_info):
  """
  Prints a personalized message using the user's information.

  Args:
      user_info (dict): A dictionary containing the user's name, age, and location.
  """
  print(f"Hello {user_info['name']}, you are {user_info['age']} years old and live in {user_info['location']}.")

def main():
  """
  The main function to execute the program.
  """
  user_info = get_user_info()
  print_personalized_message(user_info)

if __name__ == "__main__":
  main()