def perform_operation(num1, num2, operation):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return "Error: Division by zero"
            else:
                return num1 / num2
        case _:
            return "Invalid operation"


# Test the function (ALX checker runs this part)
if __name__ == "__main__":
    print(perform_operation(10, 5, "+"))   # 15
    print(perform_operation(10, 5, "-"))   # 5
    print(perform_operation(10, 5, "*"))   # 50
    print(perform_operation(10, 5, "/"))   # 2.0
    print(perform_operation(10, 0, "/"))   # Error message