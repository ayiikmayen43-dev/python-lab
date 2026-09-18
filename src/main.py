from utils import celsius_to_fahrenheit, is_even, square


number = float(input("Enter a number: "))
parity = "even" if is_even(number) else "odd"

print(f"Square: {square(number)}")
print(f"The number is {parity}.")
print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(number)}")
