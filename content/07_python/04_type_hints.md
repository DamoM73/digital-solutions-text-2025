# Type Hints

:::{dropdown} Learning Goals
By the end of this section you will:
- understand what type hints are and why we use them
- know how to add type hints to variables, function parameters and return values
- know how to add type hints to lists, dictionaries and tuples
- know how to use VS Code to check our type hints
:::

## What are type hints?

Python is a **dynamically typed** language. We never have to tell Python what type of data a variable holds; it works it out while the program runs. That makes Python quick to write, but it can make our code harder to understand.

Let's think about this function:

:::{code} python
:linenos:
def calculate_total(price, quantity):
    return price * quantity
:::

What should `price` be? An `int`, a `float`, or maybe a string like `"$4.50"`? What does the function give back? We can't tell without reading the code, or worse, waiting for it to crash.

**Type hints** solve this. They are labels we add to our code that say what type of data a variable, parameter or return value should be.

:::{code} python
:linenos:
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
:::

Now anyone reading the function, including us in a few weeks' time, can see that it takes a `float` and an `int`, and gives back a `float`.

:::{hint} Why use type hints?
:class: dropdown
- **readability** &rarr; our code explains what data it expects, without extra comments
- **fewer errors** &rarr; VS Code can find type mistakes before we run our program
- **better autocomplete** &rarr; VS Code knows the type of each variable, so it suggests the right methods
- **good practice** &rarr; type hints are widely used in industry and make our code easier for others to maintain
:::

## Variables

To add a type hint to a variable, we put a colon (`:`) and the type after the variable name.

:::{code} python
:linenos:
name: str = "Alex"
age: int = 16
height: float = 1.75
is_enrolled: bool = True
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; `name` holds a string (`str`)
- **line 2** &rarr; `age` holds a whole number (`int`)
- **line 3** &rarr; `height` holds a decimal number (`float`)
- **line 4** &rarr; `is_enrolled` holds `True` or `False` (`bool`)
:::

We don't need to hint every variable. Python and VS Code can usually work out the type from the value. Variable hints are most useful when the value doesn't make the type obvious, such as an empty list (see [Collections](#type-hint-collections) below).

## Functions

Functions are where type hints are most useful. We hint each **parameter** with a colon, and the **return value** with an arrow (`->`) before the colon at the end of the `def` line.

:::{code} python
:linenos:
def greet(name: str) -> str:
    return f"Hello, {name}!"


def rectangle_area(width: float, height: float) -> float:
    return width * height
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; `greet` takes one parameter, `name`, which should be a `str`. The `-> str` says it returns a `str`
- **line 5** &rarr; `rectangle_area` takes two `float` parameters and returns a `float`
:::

### Functions that return nothing

If a function doesn't return a value, we hint the return type as `None`.

:::{code} python
:linenos:
def print_receipt(item: str, cost: float) -> None:
    print(f"{item}: ${cost:.2f}")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; `-> None` tells us `print_receipt` only prints. It doesn't return anything we can use
- **line 2** &rarr; prints the item and its cost to two decimal places
:::

### Type hints are not enforced

Type hints are only labels. Python ignores them when the program runs, so it won't stop us passing the wrong type.

:::{code} python
:linenos:
def double(number: int) -> int:
    return number * 2


result = double("5")
print(result)
:::

Output:

:::{code} text
55
:::

`double` was meant to receive an `int`, but we passed it the string `"5"`. Python ran it anyway, and `"5" * 2` joined the string to itself to make `"55"`. Nothing crashed, but the result is wrong. Bugs like this are hard to find, which is why we get VS Code to check our type hints for us.

(type-hint-collections)=
## Collections

For lists, dictionaries and tuples, we also say what type of data is stored **inside** the collection, using square brackets.

:::{code} python
:linenos:
subjects: list[str] = ["Digital Solutions", "English", "Maths"]
results: dict[str, int] = {"Digital Solutions": 92, "English": 78}
student: tuple[str, int] = ("Alex", 16)
classes: list[dict[str, str]] = [
    {"subject": "Digital Solutions", "room": "T12"},
    {"subject": "English", "room": "B3"},
]
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; `list[str]` is a list where every item is a `str`
- **line 2** &rarr; `dict[str, int]` is a dictionary with `str` keys and `int` values
- **line 3** &rarr; `tuple[str, int]` is a tuple with exactly two items: a `str` first, then an `int`
- **lines 4&ndash;7** &rarr; `list[dict[str, str]]` is a list of dictionaries, where each dictionary has `str` keys and `str` values. This is the same shape as the data we get from `csv.DictReader`
:::

:::{hint} Lists vs tuples
:class: dropdown
A list hint has one type, because every item should be the same type: `list[int]`.

A tuple hint lists the type of each position, because tuples have a fixed length: `tuple[str, int, float]` is a tuple of exactly three items.
:::

Collection hints work in functions too:

:::{code} python
:linenos:
def highest_result(results: dict[str, int]) -> str:
    best_subject = ""
    best_mark = 0
    for subject, mark in results.items():
        if mark > best_mark:
            best_subject = subject
            best_mark = mark
    return best_subject
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; the function takes a dictionary of subject names (`str`) and marks (`int`), and returns the name of a subject (`str`)
- **lines 2&ndash;3** &rarr; start with an empty subject and a mark of 0
- **line 4** &rarr; loops through each subject and mark in the dictionary
- **lines 5&ndash;7** &rarr; if this mark is higher than the best so far, it becomes the new best
- **line 8** &rarr; returns the subject with the highest mark
:::

## Checking type hints in VS Code

VS Code's Python extension includes **Pylance**, which can check our code against our type hints. Type checking is turned off by default, so we need to turn it on.

1. Open the VS Code settings with **Ctrl + ,** (Windows) or **Cmd + ,** (macOS).
2. Search for `type checking mode`.
3. Under **Python › Analysis: Type Checking Mode**, change the setting from `off` to `basic`.

Now VS Code underlines code that doesn't match our type hints with a red squiggle. If we go back to the `double("5")` example, `"5"` is underlined, and hovering over it shows:

:::{code} text
Argument of type "Literal['5']" cannot be assigned to parameter "number" of type "int" in function "double"
  "Literal['5']" is not assignable to "int"
:::

- `Argument of type "Literal['5']"` &rarr; the value we passed is the string `'5'`
- `cannot be assigned to parameter "number" of type "int"` &rarr; but the `number` parameter is hinted as an `int`
- `in function "double"` &rarr; the problem is in our call to `double`

The **Problems** panel (**View › Problems**) lists every type error in our open files, so we can fix them before we run our program.

:::{caution} Type checking modes
:class: dropdown
There are four modes: `off`, `basic`, `standard` and `strict`. `basic` catches the most common mistakes without overwhelming us. `strict` requires a hint on almost everything and will flag a lot of code that works perfectly well.
:::

## Summary

| Hint | Meaning | Example |
| --- | --- | --- |
| `str`, `int`, `float`, `bool` | basic types | `age: int = 16` |
| `name: type` | parameter type | `def greet(name: str)` |
| `-> type` | return type | `def greet(name: str) -> str:` |
| `-> None` | returns nothing | `def show(msg: str) -> None:` |
| `list[type]` | list of one type | `list[str]` |
| `dict[key_type, value_type]` | dictionary | `dict[str, int]` |
| `tuple[type, type, ...]` | tuple with a fixed type for each position | `tuple[str, int]` |

:::{seealso} Type Hint Activities
:class: dropdown
Turn on type checking in VS Code before starting these activities.

**Activity 1: Hint the variables**

Add type hints to each of these variables.

```python
team_name = "Bayside Bandits"
games_played = 12
win_rate = 0.75
in_finals = True
```

---

**Activity 2: Hint a function**

Add type hints to the parameter and return value of this function.

```python
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


print(celsius_to_fahrenheit(25))
```

Expected Output:

```text
77.0
```

---

**Activity 3: A function that returns nothing**

Add type hints to this function. Think carefully about what it returns.

```python
def print_scoreboard(home, home_score, away, away_score):
    print(f"{home} {home_score} - {away_score} {away}")


print_scoreboard("Lions", 3, "Tigers", 1)
```

Expected Output:

```text
Lions 3 - 1 Tigers
```

---

**Activity 4: Hint functions that use collections**

Add type hints to both functions, including the `counts` variable inside `count_words`.

```python
def average(scores):
    return sum(scores) / len(scores)


def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


print(average([70, 85, 90]))
print(count_words(["red", "blue", "red"]))
```

Expected Output:

```text
81.66666666666667
{'red': 2, 'blue': 1}
```

---

**Activity 5: Find the type errors**

This code already has type hints, but it has two type errors. Copy it into VS Code, use the red squiggles to find the errors, and fix them.

```python
def get_initials(first_name: str, last_name: str) -> str:
    return first_name[0] + last_name[0]


def total_marks(marks: list[int]) -> int:
    return sum(marks)


initials: str = get_initials("Sam", "Lee")
total: int = total_marks([18, 15, "20"])
average: int = total / 3
print(initials, total, average)
```

Expected Output (once fixed):

```text
SL 53 17.666666666666668
```
:::
