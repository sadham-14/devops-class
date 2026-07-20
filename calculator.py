````python
def show_menu():
    print("Sample Calculator")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number .")

def main():
    while True:
        show_menu()
        choice = input("Choose an operation: ").strip()

        if choice == "5":
            print("Goodbye.")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice.")
            continue

        a = get_number("Enter first number in number format: ")
        b = get_number("Enter second number in number format: ")

        if choice == "1":
            result = a + b
            op = "+"
        elif choice == "2":
            result = a - b
            op = "-"
        elif choice == "3":
            result = a * b
            op = "*"
        else:
            if b == 0:
                print("Cannot divide by zero.")
                continue
            result = a / b
            op = "/"

        print(f"{a} {op} {b} = {result}\n")

if __name__ == "__main__":
    main()
````