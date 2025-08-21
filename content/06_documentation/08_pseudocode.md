# Pseudocode 📝

:::{dropdown} Learning Goals
By the end of this section you will:
:::

![good code](./assets/08/good_code.png)<p>&nbsp;</p>

Pseudocode is a simplified way of writing out the steps of an algorithm without worrying about the rules of a specific programming language.

It helps programmers:
- plan before coding
- spot errors more easily
- explain logic to others
- write readable documentation
- transition smoothly from idea to code

Key advantages:
- Easier to read than real code
- Faster to write and update
- Good for testing logic before coding
- Helps with collaboration between tech and non-tech team members
- Ideal bridge between flowcharts and final code

## QCAA Pseudocode Rules

In Digital Solutions, pseudocode is the standard way to represent algorithms. Since schools use different programming languages, the syllabus uses pseudocode to ensure consistency. The QCAA has set specific rules for how it must be written.

:::{caution} Do not use Python Code
Yes Python is easy to read, and many developers joke that it is like writing in Pseudocode, but it is not the pseudocode that is expected from QCAA. Avoid getting so detailed in your pseudocode that you start using Python specific language.
:::

### Keywords

**KEYWORDS** should be written bold and capitalized.

Keywords do not have to be valid programming language words as long as they clearly convey the intent of the line of pseudocode.

### Calculations

Pseudocode should clearly indicate what is happening at each step, including formulas of calculations.

For example:
`CALCULATE net` is not as clear as `CALCULATE net = gross − tax`

### Naming Conventions

Use snake case naming convention for variable names with multiple words, subroutines, methods and functions.

Snake case is a convention where all words are in lowercase and spaces between words is replaces with an `_`

For example:
`VAR file_name`

### Font

Use a mono-space typeface when writing algorithms on computer:

Windows mono-space fonts:
- Courier New
- Consolas
- Cascadia Code
- Cascadia Mono

Mac mono-spaced fonts:
- Andalé Mono
- Consolas
- Courier
- Courier New

### Variables

To input or output values, common words can be used as keywords.

For example:
- `INPUT mark`
- `WRITE "the total is" count`
- `PRINT x, y`
- `DISPLAY name, result`
- `READ name from list.txt`
- `OUTPUT average`

Pseudocode uses the assignment operator, `=` to assign values.

For example:
- `CALCULATE net = gross - tax`

:::{seealso} Simple Pseudocode Activities
:class: dropdown
**Activity 1**
Create an algorithm that asks the user to enter the length and width of a rectangle, calculates the area, and displays the result.

---

**Activity 2**
Create an algorithm that asks the user to enter the number of hours worked and the hourly rate, calculates the total pay, and displays the result.

---
**Activity 3**
Create an algorithm that reads three student marks from a file called `marks.txt`, calculates the average, and writes the result to a file named `average.txt`.
:::

### Modularisation

All pseudocode modules start and ends with the `BEGIN` and `END` keywords.

Main algorithm:

``` pseudocode
BEGIN
    statements
END
```

Defining procedures, subroutines, methods or functions

``` pseudocode
BEGIN function_name
    statements
END
```

Calling procedures, subroutines, methods or functions

``` pseudocode
statements
function_name
statements
```

:::{seealso} Modularisation Pseudocode Activities
:class: dropdown
**Activity 1**
Create a program that calculates the perimeter of a rectangle. The main program should:
- Ask the user to input the length and width
- Call a module named `calculate_perimeter` which returns the perimeter using the formula: perimeter = 2 × (length + width)
- Display the result to the user

---
**Activity 2**
You are designing a program that reads a student's name and score from a file called `input.txt`. The main program should:
- Call a function named `generate_report`
- `generate_report` should call another function named `format_score`, which returns a sentence combining the name and score
- `generate_report` should write that sentence to a file called report.txt
:::

### Iterations

There are three main types of loops — each has a clear start and end, with the statements within the loop indented.

**Post-test loops**

``` pseudocode
REPEAT
    statements
UNTIL
```

:::{caution} No post- test loops in Python
Python does not have a Post-test loop, so we will not be using this for units 1-3. But you need to know this concept for Unit 4, especially for the external exam.
:::

**Pre-test loop**

``` pseudocode
WHILE
    statements
ENDWHILE
```

**Counted loop**

``` pseudocode
FOR count = start_val TO end_val
    statements
NEXT count
ENDFOR
```

:::{seealso} Iteration Pseudocode Activities
:class: dropdown
**Activity 1**
Write an algorithm that displays the numbers 1 to 10, one per line.

---
**Activity 2**

Write an algorithm that asks the user to enter a password.
Repeat until the correct password `"admin123"` is entered.

---
**Activity 3**

Write an algorithm that displays a menu with options and asks the user for a choice. Keep repeating until the user enters `"exit"`.

---
**Activity 4**

Write an algorithm that reads 5 numbers from the user and calculates the total.
:::

### Selection

A control structure used for decisions or branching and choosing alternate paths. The beginning and end of these structures are indicated with keywords.

**IF statement**

``` pseudocode
IF condition THEN
    statements
ENDIF
```

**IF...ELSE statement**

``` pseudocode
IF condition THEN
    statements
ELSE
    statements
ENDIF
```

**IF...ELIF...ELSE statement**

``` pseudocode
IF condition THEN
    statements
ELSE IF condition THEN
    statements
ELSE
    statements
ENDIF
```

**MATCH statement**

In most other languages these are called switches

``` pseudocode
SWITCH test_variable
    CASE option
        statements
    CASE option
        statements
    CASE statements
ENDSWITCH
```

:::{seealso} Iteration Pseudocode Activities
:class: dropdown
**Activity 1**

Ask the user for a number. If the number is greater than 100, display `"Big number"`.

---

**Activity 2**

Ask the user to enter their age. If the age is 18 or over, display `"Adult"`, otherwise display `"Minor"`.

---

**Activity 3**

Ask the user to enter a test score (0–100).

- If the score is 80 or more, display `"High"`
- If the score is 50 or more, display `"Medium"`
- Otherwise, display `"Low"`

---
**Activity 4**

Ask the user to type a day abbreviation (eg. `"mon"`, `"tue"`, `"wed"`). Display the full day name (e.g. `"Monday"`).
:::

### SQL

The QCAA does not have any opinion about the pseudocode for SQL. Therefore, just write your SQL code like you would use it in your program.

:::{seealso} Full Pseudocode Activities
:class: dropdown
**Activity 1**
You are creating a program to process student results. The program should:
1. Read a list of 5 student names and their scores from `scores.txt`
2. For each student:
   - Calculate if their score is a pass or fail (pass mark is 50)
   - Store a formatted message like "Jamal scored 78: PASS"
3. Write all results to a file called results.txt
4. Repeat this process until the file is finished
5. Use modularisation to separate the calculation logic from the report generation

---

**Activity 2**
You’re building a system for a group of friends who ordered multiple pizzas and want to split the cost based on how many slices each person ate.

Each line in **pizza_log.txt** contains:
`person_name, slices_eaten`

The total cost and total number of slices are entered by the user.

The program should:
1. Ask the user for the total pizza cost and the total number of slices across all pizzas.
2. For each line in pizza_log.txt, read the person’s name and slices eaten.
3. Use a function called `calculate_share` to calculate what that person owes.
4. Write each person’s name and amount owed to `pizza_bill.txt`.
5. Accumulate the total collected and display it at the end.
:::

## What Pseudocode to Include

Your assignment have limited space, so you will not be able include all your algorithms as pseudocode. That presents the question, what code should you include?

Ultimately, the pseudocode presented in your assignment should demonstrate your coding skill. Choose the algorithms that you are most proud of, or that you found the trickiest.

Also keep in find that you should be demonstrating all six of the algorithm basic building blocks:
- sequence
- assignment
- conditions
- selection
- iteration
- modularisation

:::{seealso} General Pseudocode Activities
:class: dropdown
1. What are two key advantages of writing pseudocode before coding?
2. Why does the QCAA use pseudocode instead of specific programming languages?
3. What naming convention should be used for variables and functions in pseudocode?
4. What pseudocode should you include in your assignments?
5. What are the six basic building blocks that should be demonstrated in your pseudocode?
:::