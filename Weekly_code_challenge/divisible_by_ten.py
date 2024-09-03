def divisible_by_ten(num):
    """Checks if a number is divisible by 10.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if num is divisible by 10, False otherwise.
    """

    remainder = num % 10
    if remainder == 0:
        return True
    else:
        return False
    
def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            is_divisible = divisible_by_ten(number)
            print(f"{number} is divisible by 10: {is_divisible}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()