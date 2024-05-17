# Calculator Class

class Calculator:
    def square(self, num):
        return num * num

    def cube(self, num):
        return num * num * num

# Example usage
calc = Calculator()
print(calc.square(3))  # Output: 9
print(calc.cube(3))    # Output: 27
