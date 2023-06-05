### Lesson 1: String manipulation in Python

In this lesson, you'll learn how to manipulate strings in Python, including how to:

1. Print a string
2. Concatenate strings
3. Get the length of a string
4. Convert strings to lowercase and uppercase
5. Remove whitespace from the beginning and end of a string
6. Split a string into a list of substrings
7. Get a substring from the start of a string
8. Get a substring from the end of a string
9. Check if a string is in another string
10. Find the index of a string in another string
11. Replace a substring in a string
12. Count the occurrences of a substring in a string
13. Check if a string starts or ends with a substring
14. Check if a string is empty
15. Check if a string contains only digits
16. Check if a string contains only letters
17. Check if a string is alphanumeric
18. Check if a string is in title case
19. Check if a string is lowercase or uppercase
20. Check if a string is a valid identifier
21. Check if a string is a valid number
22. Check if a string is printable
23. Check if a string is a space

### 1. Print a string

To print a string in Python, use the `print()` function. For example:

```python
print("Hello, world!")
```

another examples

```python
print("soluton mundo")
```

This is how you print a string in Python. You can also print multiple strings at once by separating them with commas:

```python
print("Hello,", "world!")
```

Multiline strings can be printed using triple quotes:

```python
print("""This is a
multiline string""")
```

### 2. Concatenate strings

To concatenate, or combine, two strings, use the `+` operator. For example:

```python
print("Hello, " + "world!")
```

Another way to concatenate strings is to use the `+=` operator:

```python
text = "Hello, "
text += "world!"
print(text)
```

### 3. Get the length of a string

To get the length of a string in Python, use the `len()` function. For example:

```
text = "Hello, world!"
print(len(text))

```

This will output `13`, which is the length of the string "Hello, world!". You can also use this function to check if a string is empty:

```
text = ""
if len(text) == 0:
    print("The string is empty.")
else:
    print("The string is not empty.")

```

This will output "The string is empty." since the variable `text` is an empty string.

### 4. Convert strings to lowercase and uppercase

To convert a string to lowercase, use the `lower()` method. For example:

```python
text = "Hello, world!"
print(text.lower())
```

will print out "hello, world!".

This will output "hello, world!". To convert a string to uppercase, use the `upper()` method:

```python
text = "Hello, world!"
print(text.upper())
```

will output "HELLO, WORLD!".

### 5. Remove whitespace from the beginning and end of a string

To remove whitespace from the beginning and end of a string, use the `strip()` method. For example:

```python
text = "   String with whitespace in front and end   "
textstrip = strip(text)
print(textstrip)
```

### **6. Split a string into a list of substrings**

To split a string into a list of substrings in Python, use the `split()` method. For example:

```
text = "Hello, world!"
print(text.split(", "))

```

This will output:

```
['Hello', 'world!']

```

### **7. Get a substring from the start of a string**

To get a substring from the start of a string in Python, use slicing. For example:

```
text = "Hello, world!"
print(text[:5])

```

This will output:

```
Hello

```

### **8. Get a substring from the end of a string**

To get a substring from the end of a string in Python, use negative indexing and slicing. For example:

```
text = "Hello, world!"
print(text[-6:])

```

This will output:

```
world!

```

### **9. Check if a string is in another string**

To check if a string is in another string in Python, use the `in` keyword. For example:

```
text = "Hello, world!"
if "world" in text:
    print("The string 'world' is in the variable 'text'.")
else:
    print("The string 'world' is not in the variable 'text'.")

```

This will output:

```
The string 'world' is in the variable 'text'.

```

### **10. Find the index of a string in another string**

To find the index of a string in another string in Python, use the `index()` method. For example:

```
text = "Hello, world!"
print(text.index("world"))

```

This will output:

```
7

```

### **11. Replace a substring in a string**

To replace a substring in a string in Python, use the `replace()` method. For example:

```
text = "Hello, world!"
print(text.replace("world", "Python"))

```

This will output:

```
Hello, Python!

```

### **12. Count the occurrences of a substring in a string**

To count the occurrences of a substring in a string in Python, use the `count()` method. For example:

```
text = "Hello, world!"
print(text.count("o"))

```

This will output:

```
2

```

### **13.Check if a string starts or ends with a substring**

To check if a string starts or ends with a substring in Python, use the `startswith()` or `endswith()` method. For example:

```
text = "Hello, world!"
if text.startswith("Hello"):
    print("The string starts with 'Hello'.")
else:
    print("The string does not start with 'Hello'.")

if text.endswith("world!"):
    print("The string ends with 'world!'.")
else:
    print("The string does not end with 'world!'.")

```

This will output:

```
The string starts with 'Hello'.
The string ends with 'world!'.

```

### **14.Check if a string is empty**

To check if a string is empty in Python, use the `is_empty()` method. For example:

```python
text = ""
if text.is_empty():
    print("The string is empty.")
else:
    print("The string is not empty.")

```

### **15.Check if a string contains only digits**

To check if a string contains only digits in Python, use the `isdigit()` method. For example:

```python
text = "123"
if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

```

### **16. Check if a string contains only letters**

This is to check if a string contains only letters in Python, use the `isalpha()` method. For example:

```python
text = "Hello this text contains only letters"
if text.isalpha():
    print("The string contains only letters.")
else:
    print("The string does not contain only letters.")

```

to prove that this method only returns on a string that contains only letters, we can add a number to the string:

```python
text = "Hello this text contains only letters 123"
if text.isalpha():
    print("The string contains only letters.")
else:
    print("The string does not contain only letters.")

```

the output will be:

```python
The string does not contain only letters.

```

### **17. Check if a string is alphanumeric**

This is to check if a string is alphanumeric in Python, use the `isalnum()` method. For example:

```python
text = "Hello this text contains only letters and numbers 123"
if text.isalnum():
    print("The string contains only letters and numbers.")
else:
    print("The string does not contain only letters and numbers.")

```

the output will be:

```python
The string contains only letters and numbers.

```

### **18. Check if a string is in title case**

This is to check if a string is in title case in Python, use the `istitle()` method. For example:

```python

text = "Hello this text contains only letters and numbers 123"
if text.istitle():
    print("The string is in title case.")
else:
    print("The string is not in title case.")

```

### **19. Check if a string is lowercase or uppercase**

 This is to check if string is lowercase or uppercase in Python, use the `islower()` or `isupper()` method. For example:

```python
testupper = "HELLO"
testlower = "hello"

if testupper.isupper():
    print("The string is uppercase.")
else:
    print("The string is not uppercase.")

## next check if the string is lowercase
if testlower.islower():
    print("The string is lowercase.")
else:
    print("The string is not lowercase.")

```

### **20. Check if a string is a valid identifier**

To check if a string is a valid identifier in Python, use the ```isidentifier()``` method. For example:

```python

text = "my_variable"
if text.isidentifier():
    print("The string is a valid identifier.")
else:
    print("The string is not a valid identifier.")

```

### **21. Check if a string is a valid number**

To check if a string is a valid number in Python, you can use various methods depending on the specific requirements. Here are a few examples:

To check if a string represents an integer, you can use the isdigit() method:

```python

text = "123"
if text.isdigit():
    print("The string is a valid integer.")
else:
    print("The string is not a valid integer.")

```

### **22. Check if a string is printable**

To check if a string is printable in Python, you can use the isprintable() method. This method returns True if all characters in the string are printable or the string is empty, otherwise it returns False. Here's an example:

```python
text = "Hello, world!"
if text.isprintable():
    print("The string is printable.")
else:
    print("The string is not printable.")

```

This will output:

```python
The string is printable.

```

That is all, that covers the topic string manipulation in python.

### Nota Bahasa Melayu

### **Pengajaran 1: Pengendalian Rentetan dalam Python**

Dalam pengajaran ini, anda akan mempelajari cara pengendalian rentetan dalam Python, termasuk cara untuk:

1. Mencetak rentetan
2. Menggabungkan rentetan
3. Mendapatkan panjang rentetan
4. Menukar rentetan menjadi huruf kecil dan besar
5. Mengeluarkan ruang kosong dari mula dan akhir rentetan
6. Memecah rentetan menjadi senarai subrentetan
7. Mendapatkan subrentetan dari mula rentetan
8. Mendapatkan subrentetan dari akhir rentetan
9. Memeriksa sama ada rentetan dalam rentetan yang lain
10. Mencari indeks rentetan dalam rentetan yang lain
11. Menggantikan subrentetan dalam rentetan
12. Mengira bilangan kemunculan subrentetan dalam rentetan
13. Memeriksa sama ada rentetan bermula atau berakhir dengan subrentetan
14. Memeriksa sama ada rentetan kosong
15. Memeriksa sama ada rentetan mengandungi hanya digit
16. Memeriksa sama ada rentetan mengandungi hanya huruf
17. Memeriksa sama ada rentetan mengandungi huruf dan digit
18. Memeriksa sama ada rentetan dalam huruf pertama setiap perkataan besar
19. Memeriksa sama ada rentetan dalam huruf kecil atau besar
20. Memeriksa sama ada rentetan adalah pengenalan yang sah

### **1. Mencetak rentetan**

Untuk mencetak rentetan dalam Python, gunakan fungsi `print()`. Sebagai contoh:

```
print("Hello, world!")

```

Contoh lain:

```
print("soluton mundo")

```

Ini adalah cara untuk mencetak rentetan dalam Python. Anda juga boleh mencetak beberapa rentetan sekaligus dengan memisahkan mereka dengan koma:

```
print("Hello,", "world!")

```

Rentetan beberapa baris boleh dicetak dengan menggunakan tanda petik tiga:

```
print("""This is a
multiline string""")

```

### **2. Menggabungkan rentetan**

Untuk menggabungkan dua rentetan, gunakan operator `+`. Sebagai contoh:

```
print("Hello, " + "world!")

```

Cara lain untuk menggabungkan rentetan adalah menggunakan operator `+=`:

```
text = "Hello, "
text += "world!"
print(text)

```

### **3. Mendapatkan panjang rentetan**

Untuk mendapatkan panjang rentetan dalam Python, gunakan fungsi `len()`. Sebagai contoh:

```
text = "Hello, world!"
print(len(text))

```

Ini akan menghasilkan `13`, yang merupakan panjang rentetan "Hello, world!". Anda juga boleh menggunakan fungsi ini untuk memeriksa sama ada rentetan kosong:

```
text = ""
if len(text) == 0:
    print("Rentetan adalah kosong.")
else:
    print("Rentetan tidak kosong.")

```

Ini akan menghasilkan "Rentetan adalah kosong." kerana pemboleh ubah `text` adalah rentetan kosong.

### **4. Menukar rentetan menjadi huruf kecil dan besar**

Untuk menukar rentetan menjadi huruf kecil, gunakan kaedah `lower()`. Sebagai contoh:

```
text = "Hello, world!"
print(text.lower())

```

akan mencetak "hello, world!".

Untuk menukar rentetan menjadi huruf besar, gunakan kaedah `upper()`:

```
text = "Hello, world!"
print(text.upper())

```

akan mengeluarkan "HELLO, WORLD!".

### **5. Mengeluarkan ruang kosong dari mula dan akhir rentetan**

Untuk mengeluarkan ruang kosong dari mula dan akhir rentetan, gunakan kaedah `strip()`. Sebagai contoh:

```
text = "   Rentetan dengan ruang kosong di hadapan dan akhir   "
textstrip = strip(text)
print(textstrip)

```

### **6. Memecah rentetan menjadi senarai subrentetan**

Untuk memecah rentetan menjadi senarai subrentetan dalam Python, gunakan kaedah `split()`. Sebagai contoh:

```
text = "Hello, world!"
print(text.split(", "))

```

Ini akan mengeluarkan:

```
['Hello', 'world!']

```

### **7. Mendapatkan subrentetan dari mula rentetan**

Untuk mendapatkan subrentetan dari mula rentetan dalam Python, gunakan pemotongan. Sebagai contoh:

```
text = "Hello, world!"
print(text[:5])

```

Ini akan mengeluarkan:

```
Hello

```

### **8. Mendapatkan subrentetan dari akhir rentetan**

Untuk mendapatkan subrentetan dari akhir rentetan dalam Python, gunakan indeks negatif dan pemotongan. Sebagai contoh:

```
text = "Hello, world!"
print(text[-6:])

```

Ini akan mengeluarkan:

```
world!

```

### **9. Memeriksa sama ada rentetan dalam rentetan yang lain**

Untuk memeriksa sama ada rentetan dalam rentetan yang lain dalam Python, gunakan kata kunci `in`. Sebagai contoh:

```
text = "Hello, world!"
if "world" in text:
    print("Rentetan 'world' terdapat dalam pemboleh ubah 'text'.")
else:
    print("Rentetan 'world' tidak terdapat dalam pemboleh ubah 'text'.")

```

Ini akan mengeluarkan:

```
Rentetan 'world' terdapat dalam pemboleh ubah 'text'.

```

### **10. Mencari indeks rentetan dalam rentetan yang lain**

Untuk mencari indeks rentetan dalam rentetan yang lain dalam Python, gunakan kaedah `index()`. Sebagai contoh:

```
text = "Hello, world!"
print(text.index("world"))

```

Ini akan mengeluarkan:

```
7

```

### **11. Menggantikan subrentetan dalam rentetan**

Untuk menggantikan subrentetan dalam rentetan dalam Python, gunakan kaedah `replace()`. Sebagai contoh:

```
text = "Hello, world!"
print(text.replace("world", "Python"))

```

Ini akan mengeluarkan:

```
Hello, Python!

```

### **12. Mengira bilangan kemunculan subrentetan dalam rentetan**

Untuk mengira bilangan kemunculan subrentetan dalam rentetan dalam Python, gunakan kaedah `count()`. Sebagai contoh:

```
text = "Hello, world!"
print(text.count("o"))

```

Ini akan mengeluarkan:

```
2

```

### **13. Memeriksa sama ada rentetan bermula atau berakhir dengan subrentetan**

Untuk memeriksa sama ada rentetan bermula atau berakhir dengan subrentetan dalam Python, gunakan kaedah `startswith()` atau `endswith()`. Sebagai contoh:

```
text = "Hello, world!"
if text.startswith("Hello"):
    print("Rentetan bermula dengan 'Hello'.")
else:
    print("Rentetan tidak bermula dengan 'Hello'.")

if text.endswith("world!"):
    print("Rentetan berakhir dengan 'world!'.")
else:
    print("Rentetan tidak berakhir dengan 'world!'.")

```

Ini akan mengeluarkan:

```
Rentetan bermula dengan 'Hello'.
Rentetan berakhir dengan 'world!'.

```

### **14. Memeriksa sama ada rentetan kosong**

Untuk memeriksa sama ada rentetan kosong dalam Python, gunakan kaedah `is_empty()`. Sebagai contoh:

```
text = ""
if len(text) == 0:
    print("Rentetan kosong.")
else:
    print("Rentetan tidak kosong.")

```

### **15. Memeriksa sama ada rentetan mengandungi hanya digit**

Untuk memeriksa sama ada rentetan mengandungi hanya digit dalam Python, gunakan kaedah `isdigit()`. Sebagai contoh:

```
text = "123"
if text.isdigit():
    print("Rentetan mengandungi hanya digit.")
else:
    print("Rentetan tidak mengandungi hanya digit.")

```

### **16. Memeriksa sama ada rentetan mengandungi hanya huruf**

Untuk memeriksa sama ada rentetan mengandungi hanya huruf dalam Python, gunakan kaedah `isalpha()`. Sebagai contoh:

```
text = "Hello this text contains only letters"
if text.isalpha():
    print("Rentetan mengandungi hanya huruf.")
else:
    print("Rentetan tidak mengandungi hanya huruf.")

```

Untuk membuktikan bahawa kaedah ini hanya mengembalikan nilai benar pada rentetan yang mengandungi hanya huruf, kita boleh menambahkan nombor ke dalam rentetan:

```
text = "Hello this text contains only letters 123"
if text.isalpha():
    print("Rentetan mengandungi hanya huruf.")
else:
    print("Rentetan tidak mengandungi hanya huruf.")

```

keluarannya akan menjadi:

```
Rentetan tidak mengandungi hanya huruf.

```

### **17. Memeriksa sama ada rentetan mengandungi huruf dan digit**

Untuk memeriksa sama ada rentetan mengandungi huruf dan digit dalam Python, gunakan kaedah `isalnum()`. Sebagai contoh:

```
text = "Hello this text contains only letters and numbers 123"
if text.isalnum():
    print("Rentetan mengandungi huruf dan nombor sahaja.")
else:
    print("Rentetan tidak mengandungi huruf dan nombor sahaja.")

```

keluarannya akan menjadi:

```
Rentetan mengandungi huruf dan nombor sahaja.

```

### **18. Memeriksa sama ada rentetan dalam huruf pertama setiap perkataan besar**

Ini adalah untuk memeriksa sama ada rentetan dalam huruf pertama setiap perkataan besar dalam Python, gunakan kaedah `istitle()`. Sebagai contoh:

```
text = "Hello this text contains only letters and numbers 123"
if text.istitle():
    print("Rentetan dalam huruf pertama setiap perkataan besar.")
else:
    print("Rentetan tidak dalam huruf pertama setiap perkataan besar.")

```

### **19. Memeriksa sama ada rentetan dalam huruf kecil atau besar**

Ini adalah untuk memeriksa sama ada rentetan dalam huruf kecil atau besar dalam Python, menggunakan kaedah `islower()` atau `isupper()`. Sebagai contoh:

```
testupper = "HELLO"
testlower = "hello"

if testupper.isupper():
    print("Rentetan dalam huruf besar.")
else:
    print("Rentetan tidak dalam huruf besar.")

## kemudian periksa sama ada rentetan dalam huruf kecil
if testlower.islower():
    print("Rentetan dalam huruf kecil.")
else:
    print("Rentetan tidak dalam huruf kecil.")

```

### **20. Memeriksa sama ada rentetan adalah pengenalan yang sah**

Untuk memeriksa sama ada rentetan adalah pengenalan yang sah dalam Python, gunakan kaedah `isidentifier()`. Sebagai contoh:

```
text = "my_variable"
if text.isidentifier():
    print("Rentetan adalah pengenalan yang sah.")
else:
    print("Rentetan bukan pengenalan yang sah.")

```

### **21. Memeriksa sama ada rentetan adalah nombor yang sah**

Untuk memeriksa sama ada rentetan adalah nombor yang sah dalam Python, anda boleh menggunakan pelbagai kaedah bergantung kepada keperluan tertentu. Berikut adalah beberapa contoh:

Untuk memeriksa sama ada rentetan mewakili integer, anda boleh menggunakan kaedah `isdigit()`:

```
text = "123"
if text.isdigit():
    print("Rentetan adalah integer yang sah.")
else:
    print("Rentetan bukan integer yang sah.")

```

### **22. Memeriksa sama ada rentetan boleh dicetak**

Untuk memeriksa sama ada rentetan boleh dicetak dalam Python, anda boleh menggunakan kaedah `isprintable()`. Kaedah ini akan mengembalikan `True` jika semua aksara dalam rentetan boleh dicetak atau rentetan adalah kosong, jika tidak ia akan mengembalikan `False`. Berikut adalah contoh:

```
text = "Hello, world!"
if text.isprintable():
    print("Rentetan boleh dicetak.")
else:
    print("Rentetan tidak boleh dicetak.")

```

Ini akan mengeluarkan:

```
Rentetan boleh dicetak.

```

Itulah semua, topik pengendalian rentetan dalam python telah diliputi.
