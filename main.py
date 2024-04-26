if __name__ == "__main__":
  # Introduction to type conversion in Python
  # value = input("Enter a value: ")
  # print(value)

  price = int(input("Enter the price ($): "))
  tax = int(input("Enter the tax rate (%): "))

  tax_amount = price * tax / 100

  print(f"The tax amount price is ${tax_amount}")
