CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    temp = input("Enter the temperature to convert: ")
    question = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if question == "C":
        converted = convert_to_fahrenheit(float(temp))
        print(f"{temp}°C is {converted}°F")
    elif question == "F":
        converted = convert_to_celsius(float(temp))
        print(f"{temp}°F is {converted:.2f}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()
