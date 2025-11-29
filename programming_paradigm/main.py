# main.py

import sys
from robust_division_calculator import safe_divide


def main():
    # Check if exactly two arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        print("Example: python main.py 10 5")
        sys.exit(1)

    # Extract command-line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Perform safe division and print result
    result_message = safe_divide(numerator, denominator)
    print(result_message)


if __name__ == "__main__":
    main()