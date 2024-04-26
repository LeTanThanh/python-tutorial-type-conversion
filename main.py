if __name__ == "__main__":
  # Introduction to type conversion in Python
  # value = input("Enter a value: ")
  # print(value)

  price = int(input("Enter the price ($): "))
  tax = int(input("Enter the tax rate (%): "))

  tax_amount = price * tax / 100

  print(f"The tax amount price is ${tax_amount}")

  # Other type conversion functions

  """
  - float(str): convert a tring to a floating-point number.
  - bool(val): convert a value to a boolean value, either True or False.
  - str(val): return the string representation of a value.
  """

  # Getting the type of a value

  print(type(100))
  print(type(2.0))
  print(type("Hello"))
  print(type(True))
