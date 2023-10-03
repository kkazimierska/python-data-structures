## Data Structures
[Is it useful?](https://www.meme-arsenal.com/en/create/meme/2899280)

[Data Structures visualized](https://in.pinterest.com/pin/731060952016205869/)

[Usage](https://monkfox.com/course/algorithms-and-data-structures/)

Is a part of data structures and alogorythms and is udeful because it helps in
-   **Innovating scalable solutions** to every type of new and future problem
- **Optimizing your code**: most of  time goes into developing optimized algorithms for achieving the desired result, as opposed to coding.
- **Solving real-world problems**: Data structures and algorithms help in effectively organizing any messed-up environment.

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
## Arrays Data Structures

Overview.
### array.array: Basic Typed Arrays

**Arrays** created with the **array.array** class are mutable and behave similarly to lists except for one important difference: they’re **typed arrays** constrained to a single data type.

**Array** indexing.

```
import array
arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
arr[1]

# Arrays are mutable:
arr[1] = 23.0
arr

del arr[1]
arr

arr.append(42.0)
arr

# Arrays are "typed":
arr[1] = "hello"
```
### str: Immutable Arrays of Unicode Characters

Python 3.x uses str objects to store textual data as **immutable sequences of Unicode characters**.


```
import string
text = string.ascii_uppercase * 100_000_000
text[1]
# Strings are immutable:
text[1] = "a"

del text[1]

# Strings are recursive data structures:
type(text[0])
text[:50]  # Show the first 50 characters
'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX'
len(text)
```
The secret to such a blazing **speed** is that sequences in Python are backed by an array, which is a **random-access data structure** (the ability to access an arbitrary element of a sequence in equal time).
The array occupies a **contiguous block of memory**.
Every element in the array has a fixed size known up front.
When you know the memory address of an array, which is called the offset, then you can get to the desired element in the array instantly by calculating a fairly straightforward formula:

```
element_address = offset + (element_size x element_index)
```

Okay, so you know that finding an element in an array is quick, no matter where that element is physically located. Can you take the same idea and reuse it in a dictionary? Yes!
Hash tables get their name from a trick called **hashing**, which lets them translate an arbitrary key into an integer number that can work as an index in a regular array.


### list: Mutable Dynamic Arrays
Python’s lists are implemented as **dynamic arrays** behind the scenes.


This means a list allows elements to be **added or removed**, and the list will **automatically adjust** the backing store that holds these elements by allocating or releasing memory.

A **dynamic array** is similar to an array, but with the difference that its size can be dynamically modified at runtime.
```
arr = ["one", "two", "three"]
arr[0]


# Lists have a nice repr:
arr
['one', 'two', 'three']

# Lists are mutable:
arr[1] = "hello"
arr
['one', 'hello', 'three']

del arr[1]
arr
['one', 'three']

# Lists can hold arbitrary data types:
arr.append(23)
arr
```

If you’re willing to go beyond the Python standard library, then third-party packages like **NumPy** and **pandas** offer a wide range of fast array implementations for scientific computing and data science.


### Task on Arrays and Dicts
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?


## Stacks (LIFOs)

A **stack** is a collection of objects that supports fast **Last-In/First-Out (LIFO)** semantics for inserts and deletes. Unlike lists or arrays, stacks typically don’t allow for random access to the objects they contain. The insert and delete operations are also often called **push** and **pop**.

Implementation of a stack - **check stack.py** file.

Performance-wise, a proper stack implementation is expected to take **O(1) time for insert and delete operations.**

### Task on Stack

**Stack Min**: How would you design a stack which, in addition to push and pop, has a function **min**
which returns the minimum element? Push, pop and min should all operate in 0(1) time.



## References

[Hash Table Data Structure](https://realpython.com/python-hash-table/#get-to-know-the-hash-table-data-structure)

[Python Data Structures](https://realpython.com/python-data-structures/)

[Python-Algorythms-Data-Structures](https://github.com/kkazimierska/Python-for-Algorithms--Data-Structures--and-Interviews)

[Cracking Coding Interview PDF](https://github.com/kkazimierska/CrackingCodingInterview)

[Cracking Coding Interview - Solutions Python](https://github.com/kkazimierska/CtCI-6th-Edition-Python)

## TO add
Queue
Linked List

## QA Check

When can you best apply binary search? Give a real-world example.

Explain a linked list in your own words.

What is the difference between a stack and a queue?

Explain the difference between LIFO and FIFO.






