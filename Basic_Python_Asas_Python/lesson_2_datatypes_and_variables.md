# Python basics data types and variables

## Data Types and Variables in python

Examples of data types in Python explained in the tables below:

| Data Type | Description | Example |
| --- | --- | --- |
| Text Type: | str | x = "Hello World" |
| Numeric Types: | int, float, complex | x = 20 <br> x = 20.5 <br> x = 1j |
| Sequence Types: | list, tuple, range | x = \["apple", "banana", "cherry"\] <br> x = ("apple", "banana", "cherry") <br> x = range(6) |
| Mapping Type: | dict | x = {"name" : "John", "age" : 36} |
| Set Types: | set, frozenset | x = {"apple", "banana", "cherry"} <br> x = frozenset({"apple", "banana", "cherry"}) |
| Boolean Type: | bool | x = True |
| Binary Types: | bytes, bytearray, memoryview | x = b"Hello" <br> x = bytearray(5) <br> x = memoryview(bytes(5)) |

Now that we've learned about strings, let's move on to another data type: **integers**.

## Integers

Integers are used to represent numerical values without any decimal points. Examples include 0, 1, -5, and so on.

### Example of Using Integers

```
pythonCopy code# Integer variable examples
x = 10
y = -5
z = 0

# Arithmetic operations with integers
result = x + y
print("Result:", result)

# Conditional testing with integers
is_positive = x > 0
print("Is x positive?", is_positive)

```

<!-- make this a quote -->

### How to Test the Python Code

1. Save the above code in a Python file with the extension `.py`, for example, `integer_example.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the Python file is saved.
4. Run the command `python integer_example.py`.
5. Observe the output generated.

### Real-Life Example

### 1 Integer Variables

Suppose you are developing an inventory application for a store. You use integer variables to represent the quantity of items in the store. You can perform mathematical operations to calculate the number of items sold, add new stock, or determine the remaining stock quantity.

In this example, integer variables allow you to manage inventory data in an organized and systematic manner.
let's explore how integer variables can be used to manage and update inventory quantities.

```python
# Inventory application example
# Initialize the quantity of items in the store
stock_quantity = 100

# Simulate selling 20 items
items_sold = 20

# Calculate the remaining stock
remaining_stock = stock_quantity - items_sold

# Add new stock
new_stock = 50
stock_quantity += new_stock

# Print the updated stock information
print("Remaining stock:", remaining_stock)
print("Current stock quantity:", stock_quantity)
```

In the above example, we start with an initial stock quantity of 100 items in the store. We simulate selling 20 items by subtracting the ```items_sold``` value from the ```stock_quantity```. The result is stored in the ```remaining_stock``` variable.

Next, we receive a new stock of 50 items and update the ```stock_quantity``` by adding ```new_stock``` to it. Finally, we print the updated information, which includes the remaining stock and the current stock quantity.

Using integer variables, we can perform calculations and keep track of inventory changes in our application. This helps us effectively manage stock levels, make informed decisions, and provide accurate information to users or store owners.

### 2 Floats

Let's continue the inventory application example by introducing floats to represent the cost of items in the store.

```Python
# Inventory application example with floats
# Initialize the quantity and cost of items in the store
stock_quantity = 100
item_cost = 9.99

# Calculate the total value of current stock
total_value = stock_quantity * item_cost

# Simulate selling 20 items
items_sold = 20

# Calculate the remaining stock and its value
remaining_stock = stock_quantity - items_sold
remaining_value = remaining_stock * item_cost

# Add new stock
new_stock = 50
stock_quantity += new_stock

# Print the updated stock information
print("Remaining stock:", remaining_stock)
print("Remaining stock value:", remaining_value)
print("Current stock quantity:", stock_quantity)

# Calculate the total value of the updated stock
total_value += new_stock * item_cost
print("Total stock value:", total_value)

```

In this updated example, we introduce the float variable `item_cost` to represent the cost of each item in the store. We calculate the `total_value` of the current stock by multiplying the `stock_quantity` by the `item_cost`.

After simulating the sale of 20 items, we calculate the `remaining_stock` and its corresponding `remaining_value`. Then, we add new stock of 50 items to the `stock_quantity`.

Finally, we print the updated stock information, including the remaining stock quantity, its value, and the current stock quantity. Additionally, we calculate the `total_value` of the updated stock by adding the value of the new stock. This showcases how float variables can be used to represent the cost and value of items in real-world scenarios.

Using floats, we can perform calculations involving decimal values, enabling accurate financial calculations and providing insights into the value of inventory in our application.

Above example, we introduce the float variable `item_cost` to represent the cost of each item in the store. We calculate the `total_value` of the current stock by multiplying the `stock_quantity` by the `item_cost`.

The output generated by the above code is shown below:

```
Remaining stock: 80
Remaining stock value: 799.2
Current stock quantity: 150
Total stock value: 1498.5
```

# Python Basics: Sequence Types

In Python, sequence types are used to represent collections of items in a specific order. The three main sequence types in Python are lists, tuples, and ranges. Let's explore each of them in more detail.

## Lists

Lists are one of the most commonly used data structures in Python. They are mutable, meaning that you can modify them after they are created. Lists can contain elements of different data types and allow duplicate values.

### Creating Lists

```python
# Creating an empty list
my_list = []

# Creating a list with initial values
fruits = ["apple", "banana", "cherry"]
```

### Accessing List Elements

```python
# Accessing elements by index
first_fruit = fruits[0]
print(first_fruit)  # Output: apple

# Accessing elements using negative indexing
last_fruit = fruits[-1]
print(last_fruit)  # Output: cherry
```

### Modifying List Elements

```python
# Modifying an element
fruits[1] = "orange"
print(fruits)  # Output: ["apple", "orange", "cherry"]

# Appending elements to the end of the list
fruits.append("grape")
print(fruits)  # Output: ["apple", "orange", "cherry", "grape"]
```

## Tuples

Tuples are similar to lists but are immutable, meaning that once created, their elements cannot be changed. Tuples can contain elements of different data types and allow duplicate values.

### Creating Tuples

```python
# Creating an empty tuple
my_tuple = ()

# Creating a tuple with initial values
coordinates = (3, 4)
```

### Accessing Tuple Elements

```python
# Accessing elements by index
x = coordinates[0]
print(x)  # Output: 3

# Accessing elements using negative indexing
y = coordinates[-1]
print(y)  # Output: 4
```

### Immutable Nature of Tuples

```python
# Trying to modify a tuple will result in an error
coordinates[0] = 5  # TypeError: 'tuple' object does not support item assignment
```

## Range

Ranges are used to represent a sequence of numbers. They are commonly used in loops to iterate a specific number of times.

### Creating Ranges

```python
# Creating a range with a stop value
my_range = range(5)  # Represents numbers from 0 to 4

# Creating a range with start and stop values
my_range = range(1, 6)  # Represents numbers from 1 to 5
```

### Accessing Range Elements

```python
# Accessing elements by index is not possible directly with ranges

# Using a loop to access range elements
for num in my_range:
    print(num)
# Output: 0, 1, 2, 3, 4
```

### Note

Ranges are immutable, similar to tuples. Once created, you cannot modify their elements.

Sequence types, such as lists, tuples, and ranges, provide flexible ways to store and manipulate collections of data in Python. Understanding these sequence types and their properties will enable you to effectively work with various types of data in your programs.

# Python Basics: Set Types

In Python, set types are used to store collections of unique elements. Sets are unordered and mutable, meaning you can modify them after they are created. Sets are commonly used to perform mathematical operations, such as union, intersection, and difference.

## Sets

Sets are defined by enclosing comma-separated elements in curly braces `{}` or by using the `set()` constructor.

### Creating Sets

```python
# Creating an empty set
my_set = set()

# Creating a set with initial values
fruits = {"apple", "banana", "cherry"}
```

### Modifying Sets

```python
# Adding elements to a set
fruits.add("orange")
print(fruits)  # Output: {"apple", "banana", "cherry", "orange"}

# Removing elements from a set
fruits.remove("banana")
print(fruits)  # Output: {"apple", "cherry", "orange"}
```

### Set Operations

```python
# Performing set union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Performing set intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Performing set difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
```

## Frozen Sets

Frozen sets are similar to sets, but they are immutable, meaning their elements cannot be changed once created. Frozen sets are defined using the `frozenset()` constructor.

### Creating Frozen Sets

```python
# Creating a frozen set
my_frozen_set = frozenset([1, 2, 3])
```

### Immutable Nature of Frozen Sets

```python
# Trying to modify a frozen set will result in an error
my_frozen_set.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'
```

Set types, such as sets and frozen sets, provide powerful operations for working with unique elements and performing mathematical set operations. Understanding sets can be helpful in scenarios that involve handling distinct items or performing operations based on set theory.

# Python Basics: Boolean Type

In Python, the boolean type represents two values: `True` and `False`. Booleans are used to perform logical operations and make decisions based on conditions. They are fundamental in controlling the flow of programs.

## Boolean Values

Boolean values can either be `True` or `False`. They are used to represent the truth or falsity of a condition. Booleans are often the result of a comparison or a logical operation.

### Assigning Boolean Values

```python
# Assigning boolean values directly
is_true = True
is_false = False
```

## Logical Operations

Python provides several logical operators that can be used with boolean values. These operators allow you to combine or manipulate boolean values to make decisions or evaluate conditions.

### Logical Operators

- `and`: Returns `True` if both operands are `True`.
- `or`: Returns `True` if at least one operand is `True`.
- `not`: Returns the opposite boolean value of the operand.

### Examples of Logical Operations

```python
# Using the 'and' operator
result = True and False
print(result)  # Output: False

# Using the 'or' operator
result = True or False
print(result)  # Output: True

# Using the 'not' operator
result = not True
print(result)  # Output: False
```

## Conditional Statements

Conditional statements, such as `if`, `else`, and `elif`, are used to control the flow of a program based on specific conditions. These statements allow different blocks of code to be executed based on whether certain conditions are true or false.

### Example of a Conditional Statement

```python
x = 5
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```

In the above example, the program evaluates the value of `x` and executes the corresponding block of code based on the condition. The output depends on the value assigned to `x`.

Boolean values and logical operations play a crucial role in making decisions and controlling the execution flow of a program. Understanding boolean types and logical operations will allow you to build programs that respond dynamically to different conditions and make informed decisions based on boolean evaluations.

# Python Basics: Binary Types

In Python, binary types are used to represent binary data and work with raw byte data. There are three main binary types in Python: `bytes`, `bytearray`, and `memoryview`. These types allow you to work with binary data and perform operations on it.

## Bytes

The `bytes` type represents a sequence of bytes. Bytes are immutable, meaning they cannot be modified once created. They are commonly used to store and transmit binary data.

### Creating Bytes

```python
# Creating an empty bytes object
empty_bytes = bytes()

# Creating bytes from a sequence of integers
my_bytes = bytes([65, 66, 67])  # Represents the ASCII values of 'A', 'B', and 'C'
```

### Accessing Bytes

```python
# Accessing individual bytes by index
print(my_bytes[0])  # Output: 65
```

## Bytearray

The `bytearray` type is similar to bytes but is mutable, allowing you to modify its elements. Bytearrays are commonly used when you need to modify binary data.

### Creating Bytearrays

```python
# Creating an empty bytearray
empty_bytearray = bytearray()

# Creating a bytearray from a sequence of integers
my_bytearray = bytearray([65, 66, 67])
```

### Modifying Bytearrays

```python
# Modifying individual bytes
my_bytearray[1] = 68
print(my_bytearray)  # Output: bytearray(b'ADC')
```

## Memoryview

The `memoryview` type provides a way to access the internal data of other binary objects, such as bytes or bytearrays, without making a copy. It allows for efficient manipulation of large amounts of binary data.

### Creating Memoryview

```python
# Creating a memoryview from a bytes object
my_bytes = bytes([65, 66, 67])
my_memoryview = memoryview(my_bytes)
```

### Accessing Memoryview

```python
# Accessing individual bytes through memoryview
print(my_memoryview[0])  # Output: 65
```

Binary types in Python, such as bytes, bytearrays, and memoryviews, provide powerful ways to work with binary data. Understanding these types allows you to handle binary information, such as reading or writing binary files, network communication, and other low-level operations involving binary data.
