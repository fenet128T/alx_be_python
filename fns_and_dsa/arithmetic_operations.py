def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"



if __name__ == "__main__":
    print(perform_operation(10, 5, "add"))      
    print(perform_operation(10, 5, "subtract")) 
    print(perform_operation(10, 5, "multiply")) 
    print(perform_operation(10, 5, "divide"))   
    print(perform_operation(10, 0, "divide"))   