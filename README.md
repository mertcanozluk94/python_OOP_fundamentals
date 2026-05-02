# Python OOP Fundamentals

## Project Structure

```
python_OOP_fundamentals/
│
├── 01_lab.py — 16_lab.py     # Python fundamentals (16 labs)
│
└── OOP/
    ├── 01_lab.py             # Classes & objects
    ├── 02_lab.py             # Inheritance
    ├── 03_lab.py             # Polymorphism (with file I/O)
    ├── 04_lab.py             # Encapsulation
    ├── 05_lab.py             # Abstraction (ABC)
    ├── 06_lab.py             # Design pattern (Builder)
    ├── bill_info.txt         # Output file from lab 03
    └── bill_2.txt            # Output file from lab 03
```

---

## Requirements

- Python 3.10 or higher
- Some labs use external libraries:
  - `requests` — Lab 10 (API calls)
  - `pycryptodome` — Lab 14 (AES encryption)

Install optional dependencies with:

```bash
pip install requests pycryptodome
```

---

## Quick Start

```bash
# Move into the project folder
cd python_OOP_fundamentals

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Run any lab
python 01_lab.py
python OOP/01_lab.py
```

Most labs are interactive — they may ask for input via `input()`.

---

## Part 1: Python Fundamentals

Start here if you're new to Python. Each lab builds on the previous one.

### 01 — Variables and Basic I/O

The starting point: how to create variables, do simple math, and read input from the user.

**You'll learn:**
- Creating variables (numbers, strings, floats)
- The difference between `=` (assignment) and `:` (annotation)
- Using `input()` to read from the keyboard
- Type conversion with `int()`, `float()`, `str()`
- A common beginner trap: `"5" + "3"` is `"53"`, not `8`

---

### 02 — Conditionals

Make your code **decide** what to do.

**You'll learn:**
- `if` / `else` / `elif`
- Comparison operators (`>`, `<`, `==`, `!=`)
- The modulo operator `%` (used to check even/odd)
- Calculating area and perimeter of a square
- Debugging tips (F5, F11 in IDEs)

---

### 03 — Nested Conditionals

Combine multiple conditions: BMI calculator and a vehicle speed checker.

**You'll learn:**
- Logical operators: `and`, `or`, `not`
- Nested `if` statements
- Real-world flows: login → input → calculate → categorize
- The `.lower()` method for case-insensitive comparison

---

### 04 — While Loops

Repeat code while a condition is true.

**You'll learn:**
- `while` loops with counters
- Counting up and counting down
- Summing odd and even numbers
- Avoiding infinite loops (always update your counter!)

---

### 05 — For Loops and Nested Loops

A more structured way to repeat code.

**You'll learn:**
- `for` loops with `range(start, stop, step)`
- Counting odd vs. even numbers
- Nested loops (loops inside loops)
- Building a multiplication table
- Drawing patterns with `print(end='')`

---

### 06 — Lists

Store multiple values in a single variable.

**You'll learn:**
- Creating, accessing, and modifying lists
- Methods: `append()`, `remove()`, `pop()`
- Looping through a list with `for`
- Handling errors with `try`/`except` (e.g., `IndexError`)
- Filtering vowels from a word

---

### 07 — Built-in Functions for Lists

Powerful tools that work with collections.

**You'll learn:**
- `any()` and `all()` for boolean checks across collections
- `zip()` to combine multiple lists
- List comprehensions: `[x**2 for x in range(10)]`
- Generating random numbers with `randint`

---

### 08 — `map` and `lambda`

Apply a function to every item in a collection.

**You'll learn:**
- `map(function, iterable)` — apply transformation
- `lambda` — anonymous one-line functions
- Combining `map` with `lambda` for concise code
- Working with lists of lists (2D data)

---

### 09 — Sets and String Methods

Collections of unique items + handy string utilities.

**You'll learn:**
- Creating and modifying sets (`set`, `discard`, `remove`)
- The difference between `pop` (by index) and `remove` (by value)
- String validation methods: `isupper()`, `islower()`, `isdigit()`, `isalnum()`
- Building a password strength checker

---

### 10 — HTTP Requests (API Calls)

Talk to the outside world: fetch news from an online API.

**You'll learn:**
- The `requests` library
- Reading JSON responses
- Handling network errors: `HTTPError`, `ConnectionError`, `Timeout`
- Pretty-printing data with `pprint`

> ⚠️ **Note:** This lab contains a hard-coded API key in the source. **Never commit real API keys to git.** Use environment variables (`os.getenv("API_KEY")`) or a `.env` file instead.

---

### 11 — Functions

Package reusable code into named blocks.

**You'll learn:**
- Defining functions with `def`
- Type hints: `def foo(a: int, b: int) -> int:`
- Docstrings (the `"""..."""` block at the top)
- Default parameter values
- Keyword arguments

---

### 12 — Functions in Practice

Apply functions to real problems: number generators and password validators.

**You'll learn:**
- Returning multiple values from a function
- Unpacking returned tuples: `even, odd = find_even_odd(...)`
- Building a small login system
- Writing reusable utility functions

---

### 13 — Dictionary Filtering

Search and filter data stored in dictionaries.

**You'll learn:**
- The `dict.get()` method (safer than `dict[key]`)
- Filtering a list of dictionaries by multiple criteria
- Building search functions for product catalogs

---

### 14 — File I/O and Encryption

Read and write files. Bonus: AES encryption.

**You'll learn:**
- File modes: `r` (read), `w` (write), `a` (append)
- Opening files safely with `with open(...)`
- The `**kwargs` syntax for flexible function arguments
- AES encryption with `pycryptodome`
- Capturing system info: hostname, IP address

---

### 15 — Decorators

Wrap a function to add behavior **without modifying it**.

**You'll learn:**
- What a decorator is and why it's useful
- Writing a timing decorator (`calculate_time_execution`)
- The `@decorator` syntax
- The classic `*args, **kwargs` wrapper pattern

---

### 16 — Mini Banking App

Put it all together: a simple ATM-style program with multiple users.

**You'll learn:**
- Working with lists of dictionaries
- Implementing real-world logic flows:
  - Withdraw from main balance
  - Fall back to additional balance
  - Cancel if the user declines
- The structure of a small console application

---

## Part 2: Object-Oriented Programming (OOP/)

Once you're comfortable with the basics, dive into OOP — the way most production code is organized.

### What is OOP?

OOP organizes code around **objects** instead of just functions and variables. An object is something that has:
- **Attributes** (data — like `name`, `price`, `stock`)
- **Methods** (functions that work on that data — like `calculate_bill()`)

A **class** is the blueprint. An **object** (or **instance**) is built from that blueprint.

### The Four Pillars of OOP

| Pillar | What it means | Where you'll see it |
|---|---|---|
| **Encapsulation** | Hide internal details, expose a clean interface | Lab 04 |
| **Inheritance** | Build new classes on top of existing ones | Lab 02, 03 |
| **Polymorphism** | Same method name, different behavior per class | Lab 03 |
| **Abstraction** | Define "what" without specifying "how" | Lab 05 |

---

### OOP/01 — Classes and Objects

Your first class. Build cars, students, and circles.

**You'll learn:**
- Defining a class with `class Car:`
- The `__init__` constructor (runs when an object is created)
- The `self` keyword — refers to the current instance
- Class attributes vs. instance attributes
- Calling methods on an object: `c1.calculate_area()`
- Inspecting objects with `__dict__` and `dir()`

---

### OOP/02 — Inheritance

A class can **inherit** all the features of another class.

**You'll learn:**
- The parent → child relationship
- `class Child(Parent):` syntax
- The `super().__init__(...)` call — invokes the parent's constructor
- Adding new attributes in the child class
- Why inheritance reduces code duplication

---

### OOP/03 — Polymorphism (Bill Calculator)

Same method, different behavior. Water bill, gas bill, and electric bill all have a `calculate_bill()` method, but each computes it differently.

**You'll learn:**
- **Method overriding** — child redefines a parent method
- Calling parent's version with `super().calculate_bill()`
- Writing logs to a file with `with open(...)`
- The `datetime` module for timestamps

> Output goes to `bill_info.txt` — check that file after running.

---

### OOP/04 — Encapsulation

Hide internal details so they can't be accidentally broken from outside.

**You'll learn:**
- The naming convention for private attributes: `self.__id`
- Why we hide implementation details
- The `Enum` class for fixed sets of values (like `Status.Active`)
- Using `uuid4()` for unique identifiers
- Capturing system metadata (hostname, IP)

---

### OOP/05 — Abstraction (ABC)

Define a **contract** that subclasses must follow — without writing the actual logic in the parent.

**You'll learn:**
- The `abc` module: `ABC` and `@abstractmethod`
- Why you can't directly instantiate an abstract class
- Forcing subclasses to implement specific methods
- A musical instrument example: each instrument must define its own `call_sound()`
- The `dataclass` decorator (a shortcut for simple data classes)

---

### OOP/06 — Builder Pattern (Design Pattern)

A real-world design pattern: building a `CreditCard` step by step using different "builders" (American Express, Visa, etc.).

**You'll learn:**
- What a **design pattern** is
- The Builder pattern's purpose
- The `@property` decorator (turn a method into an attribute-like accessor)
- Combining abstraction with object construction
- Why patterns make code more maintainable

---

## OOP Quick Reference

### Defining a Class

```python
class Dog:
    species = "Canis familiaris"   # class attribute (shared by all)
    
    def __init__(self, name, age):
        self.name = name           # instance attribute
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

# Create an object
my_dog = Dog("Rex", 5)
my_dog.bark()                      # → "Rex says woof!"
```

### Inheritance

```python
class Puppy(Dog):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age)        # call parent constructor
        self.energy_level = energy_level
    
    def play(self):
        print(f"{self.name} is bouncing!")
```

### Encapsulation

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance           # private — leading __
    
    def get_balance(self):                 # controlled access
        return self.__balance
```

### Abstraction

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass                                # subclasses MUST implement

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):                         # required
        return 3.14 * self.r ** 2
```

---



## License

This project is provided for educational purposes.

