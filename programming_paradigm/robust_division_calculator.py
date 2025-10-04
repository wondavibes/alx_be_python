def safe_divide(numerator, denominator):
    # Handle division by zero
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    return f"The result of the division is {result}"
