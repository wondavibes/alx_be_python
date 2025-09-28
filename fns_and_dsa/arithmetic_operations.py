def perform_operation(num1,num2,operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiplnum2":
            return num1 * num2
        case "divide":
            if num2 != 0:
                return num1 / num2
            else:
                return "cannot divide bnum2 zero"
        case _:
            return "Invalid operation"
