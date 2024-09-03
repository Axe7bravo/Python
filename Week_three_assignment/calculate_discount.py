def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
      price (float): The original price of the item.
      discount_percent (float): The discount percentage.

  Returns:
      float: The final price after applying the discount, or the original price if the discount is less than 20%.
  """

  if discount_percent >= 20:
      discount_amount = price * discount_percent / 100
      final_price = price - discount_amount
  else:
      final_price = price

  return final_price

def main():
  """Main function to demonstrate the calculate_discount function."""

  while True:
    try:
      price = float(input("Enter the original price: "))
      if price < 0:
        raise ValueError("Price cannot be negative.")

      discount_percent = float(input("Enter the discount percentage: "))
      if discount_percent < 0:
        raise ValueError("Discount percentage cannot be negative.")

      final_price = calculate_discount(price, discount_percent)
      print("Final price:", final_price)
      break
    except ValueError as e:
      print(f"Invalid input: {e}")

if __name__ == "__main__":
  main()