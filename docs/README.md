# My Python Lab Project

## Part C - Python Code

### `src/utils.py`

```python
def square(n):
	return n * n


def is_even(n):
	return n % 2 == 0


def celsius_to_fahrenheit(c):
	return (c * 9 / 5) + 32


def greet(name):
	return f"Hello, {name}!"
```

### `src/main.py`

```python
from utils import celsius_to_fahrenheit, greet, is_even, square


name = input("Enter your name: ")
number = float(input("Enter a number: "))
parity = "even" if is_even(number) else "odd"

print(greet(name))
print(f"Square: {square(number)}")
print(f"The number is {parity}.")
print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(number)}")
```

Python searches the script's directory when resolving a local import. Because
`main.py` and `utils.py` are both in `src`, `from utils import ...` loads the
functions defined in `utils.py` so `main.py` can call them.

### Test Results

The program was run with three inputs:

```text
Input: 2
Square: 4.0
The number is even.
Fahrenheit equivalent: 35.6

Input: 3
Square: 9.0
The number is odd.
Fahrenheit equivalent: 37.4

Input: 25
Square: 625.0
The number is odd.
Fahrenheit equivalent: 77.0
```
