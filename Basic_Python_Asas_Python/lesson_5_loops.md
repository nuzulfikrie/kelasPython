# Python Loops: for and while

Loops are used in Python to repeatedly execute a block of code until a certain condition is met. There are two main types of loops in Python: `for` loops and `while` loops. Let's explore each of them in more detail and expand the notes to include additional examples and explanations.

## for Loops

A `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It allows you to perform a certain action for each item in the sequence.

### Syntax

```python
for item in sequence:
    # code to be executed for each item
```

### Example 1: Iterating over a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

In this example, the `for` loop iterates over the `fruits` list and prints each item on a new line. The loop will execute three times, once for each fruit in the list.

### Example 2: Finding the maximum value in a list

```python
numbers = [10, 5, 8, 12, 3]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print("The maximum value is:", max_value)
```

In this example, the `for` loop iterates over the `numbers` list and compares each number with the current `max_value`. If a number is greater than the current `max_value`, it becomes the new `max_value`. At the end of the loop, the maximum value is printed.

## while Loops

A `while` loop is used to repeatedly execute a block of code as long as a certain condition is true. It allows you to continue looping until the condition becomes false.

### Syntax

```python
while condition:
    # code to be executed as long as the condition is true
```

### Example 1: Counting from 1 to 5

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

In this example, the `while` loop continues to execute as long as the `count` variable is less than or equal to 5. It prints the value of `count` and increments it by 1 in each iteration. The loop will execute five times, printing the numbers from 1 to 5.

### Example 2: Finding prime numbers

```python
number = 10
is_prime = True
divisor = 2
while divisor < number:
    if number % divisor == 0:
        is_prime = False
        break
    divisor += 1

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
```

In this example, the `while` loop checks if the `number` is divisible by any number less than itself. If a divisor is found, the `is_prime` flag is set to `False`, and the loop is exited using the `break` statement. At the end of the loop, the program determines whether the number is prime or not based on the value of the `is_prime` flag.

## Loop Control Statements

Python provides control statements that can be used within loops to modify their behavior.

### break Statement

The `break` statement is used to exit the loop prematurely. It is often used when a certain condition is met, and you want to stop the loop execution.

### continue Statement

The `continue` statement is used to skip the rest of the code
block within a loop for the current iteration. It is often used when you want to skip certain items or values and proceed to the next iteration of the loop.

Example:

```python
for num in range(1, 11):
    if num == 5:
        break  # exit the loop when num is 5
    if num % 2 == 0:
        continue  # skip even numbers
    print(num)
```

In this example, the `break` statement is used to exit the loop when `num` is equal to 5. The `continue` statement is used to skip even numbers. The loop will print the odd numbers from 1 to 3.

## Additional Explanation

### Difference between for and while loops

- `for` loops are used when you have a definite sequence or iterable object, and you want to iterate over each item in the sequence.
- `while` loops are used when you want to repeatedly execute a block of code as long as a specific condition is true. The condition is checked before each iteration.

### Loop Control Statements

- `break` statement: It is used to exit the loop prematurely. When encountered, it immediately terminates the loop and continues with the next statement after the loop.
- `continue` statement: It is used to skip the rest of the code block for the current iteration and move on to the next iteration of the loop.

Using these control statements in loops provides flexibility and allows you to customize the loop's behavior based on specific conditions.

Loops are powerful constructs in Python that enable you to automate repetitive tasks, iterate over data, and implement complex logic. By understanding the different types of loops, loop control statements, and their applications, you can effectively solve various problems and write efficient code.

# Python Loops: Recap

In this section, let's recap the key points about loops in Python.

- Loops are used to repeatedly execute a block of code until a certain condition is met.
- Python provides two main types of loops: `for` loops and `while` loops.
- `for` loops are used to iterate over a sequence or any iterable object. The syntax is:

  ```python
  for item in sequence:
      # code to be executed for each item
  ```

- `while` loops are used to repeatedly execute a block of code as long as a certain condition is true. The syntax is:

  ```python
  while condition:
      # code to be executed as long as the condition is true
  ```

- `for` loops are suitable when you know the number of iterations in advance, while `while` loops are useful when you don't know the exact number of iterations or when you want to repeat a block of code until a specific condition is met.
- Loop control statements, such as `break` and `continue`, can modify the behavior of loops:
  - The `break` statement is used to exit the loop prematurely.
  - The `continue` statement is used to skip the rest of the code block for the current iteration and move to the next iteration.
- It's important to use these control statements judiciously to ensure proper flow and termination of the loop.

Loops are powerful constructs in Python that allow you to automate repetitive tasks, iterate over data, and implement complex logic. Understanding how to use `for` loops and `while` loops, along with loop control statements, provides you with the ability to write efficient and flexible code to solve various problems.
