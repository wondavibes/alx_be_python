def perform_operation(x,y,operation):
    match operation:
        case "add":
            return x + y
        case "subtract":
            return x - y
        case "multiply":
            return x * y
        case "divide":
            if y != 0:
                return x / y
            else:
                return "cannot divide by zero"
        case _:
            return "Invalid operation"
