# jprinter
je Python module za printanje na printer koji može printati tekst i slike sa računala i webstranica.


# O jprinter-u
Dependencies:
* win32printing
* PIL
* urllib.request (samo za python3x)
* win32print
* win32ui

Podržava samo Windows 10.

# Instalacija
1. Skini zip
2. Unpack jprinter.py u root directory

# Korištenje
jprinter ima 3 funkcije:
1. link, za slike na webstranicama
2. img, za slike na računalu
3. text, za tekst

# Primjeri
Za importati se koristi
```python
import jprinter
```

**VAŽNO**: u argument se napiše **cijeli link** na webstranici
```python
jprinter.link("https://upload.wikimedia.org/wikipedia/commons/0/00/Two_adult_Guinea_Pigs_%28Cavia_porcellus%29.jpg")
```


```python
jprinter.img("banana.png")
```


**VAŽNO**: broj označava veličinu fonta
```python
jprinter.text("bok", 16)
```

