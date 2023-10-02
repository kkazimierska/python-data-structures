## Dictionaries, Maps, and Hash Tables

### Definition

Colloquially, the term **hash table** or **hash map**, **lookup tables**, or **associative arrays**. is often used interchangeably with the word **dictionary**. However, there’s a subtle difference between the two concepts as the former is more specific than the latter.

**Syntax for working with dictionaries**

```
phonebook = {
    "bob": 7387,
    "alice": 3719,
    "jack": 7052,


squares = {x: x * x for x in range(6)}

phonebook["alice"]

squares

```

A **dictionary** is an abstract data type made up of keys and values arranged in pairs. Moreover, it defines the following operations for those elements:

**Add** a key-value pair
**Delete** a key-value pair
**Update** a key-value pair
**Find** a value associated with the given key

```
glossary = {"BDFL": "Benevolent Dictator For Life"}
glossary["GIL"] = "Global Interpreter Lock"  # Add
glossary["BDFL"] = "Guido van Rossum"  # Update
del glossary["GIL"]  # Delete
glossary["BDFL"]  # Search
glossary
```

 Anytime you **map one thing to another or associate a value with a key**, you’re essentially using a kind of a **dictionary**. That’s why dictionaries are also known as maps or associative arrays.


A **has table** is an array with hasing function.

**Array** indexing.

```
import string
text = string.ascii_uppercase * 100_000_000

text[:50]  # Show the first 50 characters
'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX'
len(text)
```
The secret to such a blazing **speed** is that sequences in Python are backed by an array, which is a **random-access data structure** (the ability to access an arbitrary element of a sequence in equal time).
The array occupies a contiguous block of memory.
Every element in the array has a fixed size known up front.
When you know the memory address of an array, which is called the offset, then you can get to the desired element in the array instantly by calculating a fairly straightforward formula:

```
element_address = offset + (element_size x element_index)
```

Okay, so you know that finding an element in an array is quick, no matter where that element is physically located. Can you take the same idea and reuse it in a dictionary? Yes!
Hash tables get their name from a trick called **hashing**, which lets them translate an arbitrary key into an integer number that can work as an index in a regular array.

## References

[Hash Table Data Structure](https://realpython.com/python-hash-table/#get-to-know-the-hash-table-data-structure)

[Python Data Structures](https://realpython.com/python-data-structures/)