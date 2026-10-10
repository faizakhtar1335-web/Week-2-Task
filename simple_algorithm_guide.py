"""
Week 2 Task: Explaining a Simple Programming Process
Algorithm: Check whether a number is positive, negative, or zero.

Run:
    python simple_algorithm_guide.py
"""

def classify_number(number):
    """Return whether a number is positive, negative, or zero."""
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


def main():
    print("NUMBER CHECKER")
    print("This program checks whether a number is positive, negative, or zero.")

    try:
        user_input = input("Enter a number: ").strip()
        number = float(user_input)
        result = classify_number(number)
        print(f"The number {number:g} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a number, such as 8, -3, 0, or 2.5.")


if __name__ == "__main__":
    main()
