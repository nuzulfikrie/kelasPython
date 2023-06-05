# Python Conditional Statements: if, else, elif

Introduction:
Conditional statements are essential for controlling the flow of execution in a program. They allow you to specify that certain code should be executed only if a particular condition is met. Python provides three types of conditional statements: `if`, `else`, and `elif`.

## if Statements

An `if` statement is used to check if a certain condition is met. If the condition is true, the code block indented after the `if` statement is executed. If the condition is false, the code block is skipped.

Example:

```python
age = 16
if age >= 18:
    print("You are an adult")
```

In this example, the code block following the `if` statement will only be executed if the variable `age` is greater than or equal to 18.

## else Statements

An `else` statement is used to execute code if the condition in the `if` statement is not met. It provides an alternative code block to be executed when the condition is false.

Example:

```python
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

In this example, if the variable `age` is less than 18, the code block indented after the `else` statement will be executed.

## elif Statements

An `elif` statement is used to check multiple conditions and execute the code block corresponding to the first condition that is true. It allows for multiple alternative paths of execution.

Example:

```python
age = 17
if age >= 18:
    print("You are an adult")
elif age >= 16:
    print("You are a teenager")
else:
    print("You are a child")
```

In this example, the code block following the first `if` statement will be executed if the variable `age` is greater than or equal to 18. If not, the next `elif` statement is checked. If the variable `age` is greater than or equal to 16, the code block indented after the second `elif` statement will be executed. Otherwise, if none of the conditions are met, the code block following the `else` statement will be executed.

Recap:

- `if` statements are used to check if a condition is met.
- `else` statements are used to execute code when the condition in the `if` statement is not met.
- `elif` statements allow for multiple alternative conditions and code blocks to be checked and executed sequentially.

Understanding and using conditional statements enables you to control program flow and execute specific code based on certain conditions.
