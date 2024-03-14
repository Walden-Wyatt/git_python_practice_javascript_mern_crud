# main_script.py
from ..main_program import addition, multiplication

def main():
    num1 = 5
    num2 = 3

    result_addition = addition.add_numbers(num1, num2)
    result_multiplication = multiplication.multiply_numbers(num1, num2)

    print(f"Result of addition: {result_addition}")
    print(f"Result of multiplication: {result_multiplication}")

if __name__ == "__main__":
    main()
