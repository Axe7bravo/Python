def sum_of_integers():
  """Computes the sum of integers in a user-provided list."""

  integer_list = []

  while True:
    user_input = input("Enter an integer (or 'done' to finish): ")
    if user_input.lower() == "done":
      break
    try:
      integer = int(user_input)
      integer_list.append(integer)
    except ValueError:
      print("Invalid input. Please enter an integer.")

  sum_of_integers = sum(integer_list)
  return sum_of_integers

if __name__ == "__main__":
  result = sum_of_integers()
  print("The sum of the integers is:", result)