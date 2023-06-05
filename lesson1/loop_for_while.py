# Example: Iterating over a List
# In this script, there are three examples of loops. The first example demonstrates how to iterate over a list using both a for loop and a while loop. The second example shows how to count using a while loop. The third example calculates the factorial of a given number using a for loop.

# When you run the script, it will execute the code inside the loops and display the corresponding output.

# Feel free to modify the code and add more examples to explore the capabilities of loops in Python.

fruits = ["apple", "banana", "cherry"]

print("Using for loop:")
for fruit in fruits:
    print(fruit)

print("\nUsing while loop:")
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

# Example: Counting with a while loop
count = 1

print("\nCounting with a while loop:")
while count <= 5:
    print(count)
    count += 1

# Example: Finding the factorial of a number with a for loop
number = int(input("\nEnter a number: "))
factorial = 1

for num in range(1, number + 1):
    factorial *= num

print("Factorial of", number, "is:", factorial)
