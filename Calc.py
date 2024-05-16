def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Tidak dapat dibagi dengan 0"
  else:
    return x / y

def main():1
while True:
    print("Select operation:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    # Get numbers
    if choice in ('1', '2', '3', '4'):
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    
    # Perform operation based on user choice
    if choice == '1':
      result = add(num1, num2)
      print(num1, "+", num2, "=", result)
    elif choice == '2':
      result = subtract(num1, num2)
      print(num1, "-", num2, "=", result)
    elif choice == '3':
      result = multiply(num1, num2)
      print(num1, "*", num2, "=", result)
    elif choice == '4':
      result = divide(num1, num2)
      print(num1, "/", num2, "=", result)
    elif choice == '5':
      print("Exiting calculator...")
      break
    else:
      print("Invalid Input")

if __name__ == "__main__":
  main()
