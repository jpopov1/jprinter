# jprinter
is a Python module for printing images and text to the printer.


# Dependencies
* urllib.request
* win32printing
* win32print
* win32ui
* PIL

jprinter only works for Python 3x on Windows 10.

# Installation
1. Download the code
2. Unpack jprinter.py into the root directory

# Usage
jprinter has 3 functions:
1. link, for images on websites
2. img, for images on the PC
3. text, for text

# Examples
To import the module use
```python
import jprinter
```

**NOTE**: the argument requires the **whole link** of the website
```python
jprinter.link("https://upload.wikimedia.org/wikipedia/commons/0/00/Two_adult_Guinea_Pigs_%28Cavia_porcellus%29.jpg")
```

**NOTE**: the file **must** be in the same directory from where you are executing your .py script
```python
jprinter.img("banana.png")
```


**NOTE**: the number represents font size
```python
jprinter.text("Hello World!", 16)
```

