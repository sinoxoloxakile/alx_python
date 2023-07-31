#!/usr/bin/python3
 def safe_print_division(a, b):
  """
  This function divides two integers and prints the result.
  Args:
    a: The first integer to divide.
    b: The second integer to divide by.
  Returns:
    The value of the division, or `None` if an error occurred.
  """
  try:
    result = a / b
  except ZeroDivisionError:
    result = None
  finally:
    print{"Inside result:", result}
  return result