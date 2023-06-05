# In this script, there are three examples of functions to calculate the areas of different shapes: rectangle, circle, and triangle. The user is prompted to enter the required dimensions, and the corresponding function is called to calculate and display the area.

# When you run the script, it will execute the function calls and prompt you for the necessary input to calculate the areas of the shapes.

# You can customize the code by adding more functions or expanding the modular structure to include additional functionality.


# Example: Function to calculate the area of a rectangle
def calculate_area_rectangle(length, width):
    area = length * width
    return area

# Example: Function to calculate the area of a circle
def calculate_area_circle(radius):
    area = 3.14 * radius * radius
    return area

# Example: Function to calculate the area of a triangle
def calculate_area_triangle(base, height):
    area = 0.5 * base * height
    return area

# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_area = calculate_area_rectangle(length, width)
print("Area of the rectangle:", rectangle_area)

radius = float(input("\nEnter the radius of the circle: "))
circle_area = calculate_area_circle(radius)
print("Area of the circle:", circle_area)

base = float(input("\nEnter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle_area = calculate_area_triangle(base, height)
print("Area of the triangle:", triangle_area)
