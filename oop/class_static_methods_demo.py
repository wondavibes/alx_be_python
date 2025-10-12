class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a,b):
    
        """Adds two numbers and returns the result."""
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers after printing the calculation type."""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b
