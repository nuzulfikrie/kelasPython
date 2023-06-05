from pydoc import stripid


print("hello world")
print('hello,world')


## multi-line string ##
print("""hello
world""")

## 2. String Manipulation Concatenate ##

hello = "hello" + " " + "world"  + " " + "good day !"
print(hello)

### 3 string method, get length of string ###
hello = "hello world here"
print(len(hello)) # 16

## if length is "" , it will return 0
print(len("")) # 0

## convert to lower case ##
print(" this is how to lower case")
string = "HELLO HELLO HERE"
print(string.lower())

### convert to upper case ###
print("this is how to upper case")
string = "hello hello here to upper case"
print(string.upper())

### strip white space ###
text = "   String with whitespace in front and end   "
print("original text: " + text)
textstrip = text.strip()
print ("modified text: " + textstrip)

print ("test is digit or not for string 123")
text = "123"
if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")