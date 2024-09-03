def large_power(base, exponent):
  """Tests if base raised to the exponent is greater than 5000.

  Args:
      base (int): The base number.
      exponent (int): The exponent.

  Returns:
      bool: True if base^exponent is greater than 5000, False otherwise.
  """

  result = base ** exponent
  return result > 5000

def main():
  while True:
    try:
      base = int(input("Enter the base number: "))
      exponent = int(input("Enter the exponent: "))
      if base < 0 or exponent < 0:
        raise ValueError("Base and exponent must be non-negative.")
      is_large_power = large_power(base, exponent)
      if is_large_power:
          
        
        print(True)
      else:
         print(False)  
        
      break
    except ValueError:
      print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
  main()