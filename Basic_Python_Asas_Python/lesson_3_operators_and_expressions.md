# Python Basics: Operators and Expressions

In Python, operators are used to perform operations on variables and values. They allow you to manipulate data and perform calculations. Expressions, on the other hand, are combinations of operators, variables, and values that evaluate to a single value.

## Arithmetic Operators

Arithmetic operators are used to perform basic mathematical operations such as addition, subtraction, multiplication, division, and more.

### Common Arithmetic Operators

- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division
- `%`: Modulo (returns the remainder)
- `**`: Exponentiation (raises a number to the power of another number)
- `//`: Floor Division (returns the quotient, discarding any remainder)

```python
# Arithmetic operations example
x = 10
y = 3

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulo = x % y
exponentiation = x ** y
floor_division = x // y

print(addition)         # Output: 13
print(subtraction)      # Output: 7
print(multiplication)   # Output: 30
print(division)         # Output: 3.3333333333333335
print(modulo)           # Output: 1
print(exponentiation)   # Output: 1000
print(floor_division)   # Output: 3
```

## Comparison Operators

Comparison operators are used to compare values and determine the relationship between them. They return boolean values (`True` or `False`) based on the comparison result.

### Common Comparison Operators

- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

```python
# Comparison operations example
x = 5
y = 10

equal_to = x == y
not_equal_to = x != y
greater_than = x > y
less_than = x < y
greater_than_equal_to = x >= y
less_than_equal_to = x <= y

print(equal_to)             # Output: False
print(not_equal_to)         # Output: True
print(greater_than)         # Output: False
print(less_than)            # Output: True
print(greater_than_equal_to) # Output: False
print(less_than_equal_to)    # Output: True
```

## Logical Operators

Logical operators are used to combine multiple conditions and perform logical operations. They return boolean values based on the combination of conditions.

### Common Logical Operators

- `and`: Returns `True` if both conditions are `True`
- `or`: Returns `True` if at least one condition is `True`
- `not`: Returns the opposite boolean value of the condition

```python
# Logical operations example
x = 5
y = 10
z = 3

result1 = (x < y) and (y > z)
result2 = (x > y) or (y > z)
result3 = not (x > y)

print(result1)  # Output: True
print(result2)  # Output: True
print(result3)  # Output: True
```

Understanding operators and expressions is fundamental in programming, as they allow you to perform calculations, compare values, and make logical decisions. Utilizing different operators and constructing meaningful expressions enables you to create dynamic and functional code.

## Recap

- Operators in Python are used to perform operations on variables and values.
- Arithmetic operators are used for mathematical calculations.
- Comparison operators are used to compare values and evaluate conditions.
- Logical operators are used to combine conditions and perform logical operations.
- Understanding operators and expressions is crucial for performing calculations, making decisions, and implementing logical flow in programming.

By mastering operators and expressions, you gain the ability to manipulate data effectively, evaluate conditions, and create dynamic and functional code in Python.
