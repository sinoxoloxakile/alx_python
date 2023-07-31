def is_prime(number)
     """
  This function takes a number as input and returns True if the number is prime, and False otherwise.
  Args:
    number: The number to check for primality.
  Returns:
    True if the number is prime, and False otherwise.
  """
  # Check if the number is 1.
  if number == 1:
    return False
  # Check if the number is even.
  if number % 2 == 0:
    return False
  # Check if the number is divisible by any number from 3 to the square root of the number.
  for i in range(3, int(number ** 0.5) + 1, 2):
    if number % i == 0:
      return False
  # If the number is not divisible by any number from 2 to the square root of the number, then it is prime.
  return True
