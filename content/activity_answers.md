# Activity Solutions

:::{attention}Suggested solutions
Just like all things digital, there are many paths to a solution. The solutions provided below are **a** solution, but are **not the only** solution.

They are provided not so you can check you answers, but so you can check the thinking that lead to your answers.
:::

## Coding

### Coding Introduction

:::{seealso} IPO Solutions
:class: dropdown
**1. Budget Calculator**

| Input | Process | Output |
| --- | --- | --- |
| Total weekly income | Add up all expenses | Total expenses |
| List of expenses (e.g. food, transport, entertainment) | Subtract expenses from income | Remaining money |

---

**2. Step Counter App**

| Input | Process | Output |
| --- | --- | --- |
| Step data from motion sensor | Count total steps walked<br><br>Calculate distance and calories using step count and user data | Total steps<br><br>Distance walked and calories burned |

---

**3. Quiz App**

| Input | Process | Output |
| --- | --- | --- |
| User-selected answer | Compare answer to correct answer<br><br>Track score for each question | Show “Correct” or “Incorrect”<br><br>Final score after all questions |
:::

:::{seealso} Decomposition Solutions
:class: dropdown
**Activity 1**

- Ask the user to enter homework details (subject, task, due date)
- Store the homework tasks in a list or file
- Display the list of tasks to the user
- Allow the user to mark tasks as completed
- Sort or filter tasks by due date or subject

---

**Activity 2**

- Get team names and store them
- Set the starting score for each team to zero
- Create a way to add or subtract points during the game
- Display the current score on screen
- Show a final message with the winner when the game ends

---

**Activity 3**

- Load a set of questions and multiple-choice answers
- Display one question at a time to the user
- Record the user’s selected answer
- Check if the answer is correct and keep score
- Show the final score after all questions are answered
:::

:::{seealso} Pattern Recognition Solutions
:class: dropdown

**Activity 1**

Quiz Feedback Program:

- Each question has a structure: question text, multiple options, one correct answer
- The same process is repeated: show question → get answer → check answer → give feedback
- Feedback messages follow a pattern (e.g. "Correct!" or "Incorrect, the right answer is...")

---

**Activity 2**

Weather App:

- Each day’s forecast uses the same data format: day name, icon, temperature, description
- Icons represent weather types (e.g. sun, cloud, rain) and are reused across days
- Patterns in temperature changes (e.g. hot in afternoon, cool at night) can be recognised

---

**Activity 3**

Timetable Generator:

- Class times follow regular patterns (e.g. Period 1 starts at 9:00 every day)
- Subjects repeat on the same days each week
- Breaks and lunch are placed in the same time slots across all timetables
:::

:::{seealso} Abstraction Solutions
:class: dropdown
**Activity 1: Water Intake App**

- **Necessary information and features**: Date, amount of water consumed, daily goal, total intake so far, and a simple way to log each drink
- **Unnecessary details to leave out**: Brand of water, exact time of each sip, detailed drink history beyond a few days
- **Abstraction used**: Focus on tracking totals and goals; ignore details that don’t help the user meet their target

---

**Activity 2: Puzzle Game**

- **Parts that stay the same**: Player controls, puzzle-solving mechanics, scoring system, level completion logic
- **How to group/simplify**: Use a single function or module to handle shared game mechanics; only change artwork, sound, and puzzle layout per level
- **Abstraction used**: Group repeated behaviour into reusable procedures or objects (e.g. movePlayer(), checkPuzzleComplete())

---

**Activity 3: Staff Profiles Website**

- **Essential information**: Name, photo, job title, email address
- **How to keep it consistent**: Use one profile template or function that fills in staff data for each person
- **Abstraction used**: Create a reusable layout or function for all staff profiles instead of writing separate code for each one
:::

:::{seealso} System Thinking Solutions
:class: dropdown
**Activity 1: School Attendance App**

Parts of the system:

- Student data input (e.g. scanned ID or manual entry)
- Database storing attendance records
- Notification system for sending updates to teachers and parents
- Reporting interface for staff

Interactions:

- When a student is marked present or absent, the database updates
- The system sends notifications based on changes
- Reports are generated from stored attendance data
- If the input method fails, notifications and reports may be incorrect

---

**Activity 2: Online Food Delivery System**

Parts of the system:

- User app (for browsing and ordering)
- Restaurant system (receives and confirms orders)
- Payment gateway
- Delivery tracking system

Interactions:

- The user order triggers updates across the system
- Payment confirmation activates the restaurant system
- Restaurant status affects delivery time
- If one part fails (e.g. restaurant delay), it affects the whole order process

---

**Activity 3: Smart Home Lighting System**

Parts of the system:

- Light bulbs or smart switches
- Sensors (e.g. motion or daylight sensors)
- User interface (e.g. mobile app or voice assistant)
- Automation rules

Interactions:

- Sensor input affects lighting behaviour
- User settings control when and how lights change
- Automation rules link actions together (e.g. turn off lights when no motion)
- A change in settings or sensor failure can disrupt the whole system’s function
:::

### Basic Features

:::{seealso} Algorithms Solutions
:class: dropdown
Here are the **answers** to the algorithm learning questions:
1. Algorithms are the set of commands or instructions that tell a computer what to do and how to solve a problem.
2. It processes instructions one after the other in the order they appear.
3. Assignment stores the result of an expression into a variable, which holds the value for later use in the program.
4. A *condition* checks whether something is true or false; *selection* uses that condition to decide if a part of the code should run.
5. *Iteration* repeats a set of instructions multiple times, while *sequence* runs instructions once, in order.
6. Example: A guessing game where the computer checks if your guess is correct (*selection*), and keeps asking until it is (*iteration*).
7. It makes programs easier to manage, test, reuse, and debug by breaking them into smaller, logical sections.
8. *Sequence* (to go through questions), *selection* (to check answers), *assignment* (to store score), *iteration* (to go through multiple questions), and possibly *modularisation* (to separate the quiz logic into functions).
9. The code could become hard to read, debug, test, and maintain. Errors in one part of the code may affect other parts.
:::

:::{seealso} Variable Solutions
:class: dropdown
1. To store values in computer memory for use in a program.
2. The kind of data stored at that memory location.
3. Dynamic types are checked at runtime and can change; static types are checked before running and cannot change.
4. Because type checking happens at runtime and variables can change type.
5. With single or double quotes.
6. `int`
7. `float`
8. `True` and `False`
9. Values that evaluate to `True` or `False` in a Boolean context.
10. `None`, `0`, `''`
11. `Falsy`
12. Where in the program a variable can be used.
13. Global is defined outside functions and used anywhere; local is defined inside functions and used only there.
14. It limits variable access to reduce bugs and improve code organisation.
15. Local, Enclosing, Global, Built-in
16. Local → Enclosing → Global → Built-in
17. It overrides the built-in function while the code runs.
18. No
19. No
20. Global variables and built-in names
:::

:::{seealso} Control Structures Solutions
:class: dropdown
1. Sequential, selection, iteration
2. Line by line from top to bottom
3. A check to see if something is true or false
4. `True` or `False`
5. `if` and `while`
6. value operator value
7. `!=`
8. `>=`
9. Choosing a path in code based on a condition
10. Branching
11. It checks conditions in order and runs the first block that is true
12. Yes
13. Nothing runs unless there’s an `else` block
14. Runs if all previous conditions are false
15. Compares a variable against fixed values
16. Python 3.10
17. Repeating a block of code
18. Loop
19. Definite has a known number of repetitions; indefinite does not
20. `for` loop
21. `while` loop
22. Post-test loop (`do...while`)
23. `while` loop
24. Uses each item one at a time
25. A container you can move through one item at a time
26. Lists, tuples, strings (also: dictionaries, sets)
:::

:::{seealso} Data Structures Solutions
:class: dropdown
1. To store data in an organized form.
2. As collections of related data, like a shopping list or contact list.
3. Lists, tuples, sets, dictionaries.
4. An ordered collection of items.
5. Using square brackets `[]` with items separated by commas.
6. Items can be changed, added, or removed.
7. Index 0.
8. Tuples cannot be changed (immutable), lists can.
9. They offer faster performance and are ideal for fixed data.
10. Using parentheses `()` with items separated by commas.
11. A collection of unique items with no specific order.
12. Sets are unordered and only hold unique items.
13. Yes.
14. When you only care about whether an item exists, not order or duplicates.
15. Key-value pairs.
16. Using curly braces `{}`, with a colon `:` between each key and value.
17. Keys must be unique.
18. Yes.
19. The rules a programming language follows to write commands properly.
20. It ensures commands are written in a valid way that Python can understand.
:::

:::{seealso} Classes Activities
:class: dropdown
1. A class is a blueprint for creating objects.
2. Attributes and methods.
3. An attribute stores data in a class.
4. A method performs an action in a class.
5. `colour`, `wheels`
6. `drive()`, `brake()`
7. To define shared structure and behaviour for multiple car objects.
8. By calling the class name with parentheses, e.g. `Car()`
9. It creates a new object called `ferrari` from the `Car` class.
10. It allows shared code to be reused without repetition.
11. Repeating code.
12. It calls the `drive()` method on the `ferrari` object, passing `distance` as a value.
13. Because they have similar features but also differences.
14. Objects are created from classes and follow their structure.
15. In the Deepest Dungeon course.
:::

:::{seealso} Operations Activities
:class: dropdown
1. To perform actions on variables or values.
2. Arithmetic, assignment, comparison (others: logical, identity, membership, bitwise).
3. Perform basic maths with numbers.
4. Addition.
5. Whole number result of dividing x by y (floor division).
6. Control the order of operations, like in maths.
7. Exponentiation (power).
8. Assign or update the value of a variable.
9. Add 3 to the current value of `x`.
10. `=` sets a value; `+=` increases the value by adding.
11. `True` or `False`.
12. Checks if two values are not equal.
13. `True`
14. Returns `True` if both conditions are `True`.
15. Reverses the result of the condition `x < 5`.
16. `True` (since `x < 5` is true).
17. Whether two variables are the same object in memory.
18. Returns `True` if `x` and `y` refer to the same object.
19. `True`
20. If a value exists in a sequence like a list or string.
21. `True`
22. When you want to check that a value is not in a sequence.
23. `True`
:::

### Good Practice

:::{seealso} Dependability Solutions
:class: dropdown
1. Dependable code runs consistently under different conditions, handles errors gracefully, and avoids crashes, building user confidence and trust.
2. It helps others (or your future self) quickly understand, fix, or improve the code without breaking other parts.
3. Lower cognitive load makes the code easier to follow, reducing errors and making updates or collaboration simpler.
4. A dependency chain is when one module relies on another. Changes in any linked module can cause unexpected bugs or break the program.
5. Small functions are easier to test and debug. Good names and comments explain what code does, making it easier to work with.
6. Consistent style improves readability and helps teams follow the same structure, reducing mistakes and confusion.
7. It allows you to write code that handles invalid input or failures safely, preventing crashes and improving user experience.
8. Testing finds errors before users do, making sure the program behaves correctly and consistently.
9. Clear names show what variables or functions do, helping all team members quickly understand and use the code correctly.
10. Handling edge cases avoids unexpected crashes or bugs, making the program more robust and user-friendly.
:::

:::{seealso} Efficiency Solutions
:class: dropdown
1. Efficiency means completing tasks using the least amount of time and processing power.
2. The right data structure makes it faster to store and access data, improving speed.
3. Unnecessary steps slow down programs and waste resources.
4. Some algorithms use fewer steps to get to the solution, making them faster.
5. Nested loops take more time because they run many times for each outer loop run.
6. Small functions are easier to test, update, and reuse, making code faster and simpler.
7. Your code should still perform well even as the data grows; it should use minimal time and memory.
8. Code efficiency is about reducing resource use, which supports the speed and structure of algorithmic efficiency.
9. A `for` loop avoids repetition and runs faster than many repeated `if-then-else` checks.
10. Clear and simple code is easier to read and less likely to have mistakes that slow it down.
11. Functions reduce repeated code, making updates easier and programs more efficient.
12. Storing repeated results saves time by avoiding recalculating the same thing.
13. A dictionary is faster than a list for lookups because it finds items using keys.
14. Testing with different data sizes helps you find ways to make code faster and use fewer resources.
:::

:::{seealso} Effectiveness Solutions
:class: dropdown
1. Effectiveness measures how well an algorithm solves the intended problem.
2. Understanding the problem clearly ensures the solution is accurate and relevant.
3. Success criteria help you check if the solution works, like producing the correct output or meeting user needs.
4. Breaking the problem into smaller steps makes it easier to design and manage the algorithm.
5. Pseudocode or flowcharts help plan the logic before coding, reducing mistakes.
6. Clear and structured logic makes code easier to follow and less likely to have errors.
7. Testing with real, edge case, and invalid data ensures the algorithm handles all situations correctly.
8. If the algorithm doesn't work as expected, refine or fix it based on what you learned from the results.
9. User or tester feedback can show issues or improvements you didn’t notice, helping you make a better solution.
10. A desk check can work for simple problems, but complex problems need real testing to see if they function in all conditions.
:::

:::{seealso} Testing Activities
:class: dropdown
1. The main purpose of testing is to check that code performs as expected.
2. Testing helps ensure the solution solves the problem (effective), runs smoothly (efficient), and works reliably (dependable).
3. Testing should occur throughout development to catch and fix issues early and improve quality over time.
4. Exploratory testing is informal testing done by trying features without a set plan.
5. Exploratory testing helps spot unexpected issues and ensures the solution feels usable and effective.
6. Unit testing focuses on checking individual parts of code, such as functions or classes.
7. Unit testing improves dependability by catching errors close to where they occur.
8. Integrated testing checks how different components of the program work together.
9. Integrated testing is important because some problems only appear when parts of the system interact.
10. Using all three types of testing helps make the solution more reliable, accurate, and high-performing.
:::

:::{seealso} Debugging Solutions
:class: dropdown
1. Debugging is finding and fixing errors (bugs) in a program so it works correctly.
2. Bugs can cause crashes, unexpected behaviour, or incorrect results.
3. Python runs line-by-line, so one error can stop the whole program from continuing.
4. VSCode provides breakpoints, step controls, variable and watch panels, and a call stack viewer.
5. Click the "Run and Debug" tab, then select "Run and Debug" and choose "Python File."
6. A breakpoint pauses the code on a specific line; set one by clicking next to the line number.
7. The “Variables” panel shows the current values stored in variables while the program is paused.
8. “Step Over” runs the current line and moves to the next line in the same function.
9. “Step Into” enters a function call to let you debug inside that function.
10. “Step Out” runs the rest of a function and returns to where it was called.
11. Conditional breakpoints only pause when a set condition is true, helping catch specific errors.
12. An example is `y == 0`, which pauses the code only when `y` equals zero.
13. You can change variable values while paused to test scenarios or fix bugs on the fly.
14. The watch panel lets you track expressions or values as the program runs.
15. The call stack shows the order of function calls leading to the current line.
16. Print-based debugging is helpful for quick checks or when you’re unsure where the bug is.
17. Breakpoints pause the program, and the variables panel shows what’s happening at that moment.
18. Install the Python and Python Debugger extensions in VSCode.
19. Testing different values while paused helps understand bugs or test fixes without restarting.
20. These tools help spot issues earlier, understand program behaviour, and fix bugs faster.
:::

:::{seealso} Error Correction Activities
:class: dropdown
1. Error correction is the process of finding and fixing mistakes in code so the program runs correctly.
2. Developers get better at spotting and fixing errors through regular coding and experience.
3. The three main types of errors are syntax errors, runtime errors, and logic errors.
4. Syntax errors happen when the code doesn’t follow the rules of the Python language.
5. Syntax errors must be fixed before running the program because they stop the program from starting.
6. IDEs usually highlight syntax errors to help developers find and fix them quickly.
7. Common syntax errors include misspelled commands, undeclared variables, and missing brackets.
8. Runtime errors occur while the program is running, usually causing it to crash.
9. Dividing by zero causes a runtime error and stops the program.
10. Adding a number and a string causes a runtime error because they are incompatible types.
11. A runtime error happens if you try to access an index in a list that doesn’t exist.
12. Logic errors happen when the program runs but gives the wrong result or behaviour.
13. A logic error doesn’t crash the program, but it causes incorrect output or actions.
14. Using the wrong condition, like `< 5` instead of `<= 5`, can lead to incorrect program logic.
15. Misplaced brackets or incorrect operations can cause logic errors in calculations.
16. Reusing variable names incorrectly can cause unexpected results or overwrite important data.
17. An unintended infinite loop causes the program to keep running without stopping.
18. Using Boolean operators incorrectly can change the meaning of a condition and cause logic errors.
19. Using a variable before it’s declared results in a syntax error.
20. Poor program design can lead to logic errors because the structure of the code doesn’t match the intended logic.
:::

:::{seealso} Coding Conventions Activities
:class: dropdown
1. Code simplicity means writing code that is easy to read and understand.
2. Clear logic and meaningful names make code easier for others (and your future self) to follow.
3. Simple code is easier to work with, reducing mistakes and making it easier to improve.
4. Python naming rules require names to use only letters, numbers, and underscores, with no spaces, and not start with a number.
5. Variable names can’t start with a number because it breaks Python’s syntax rules.
6. Case-sensitive means `name` and `Name` are treated as different variables in Python.
7. Naming rules must be followed to run code, while naming conventions help others understand it.
8. `temperature_celsius` clearly describes what the value represents, while `x` gives no context.
9. `snake_case` uses lowercase letters and underscores, and it's used for variables and functions.
10. Constants should be written in `UPPER_CASE` with underscores, like `MAX_SIZE`.
11. `CamelCase` capitalises each word without underscores and is used for class names.
12. Python keywords have special meanings, so using them as variable names causes errors.
13. Comments are needed when code is complex or not immediately clear, even with good names.
14. A docstring is placed right after a function definition and explains what the function does.
15. A docstring should describe the function’s inputs, processes, and outputs.
16. IDEs use docstrings to show help messages, hints, and tooltips while coding.
17. Block comments explain specific sections of code that may be hard to understand at a glance.
18. They help other readers understand why a certain piece of code works the way it does.
19. Code portability means the same code works on different systems without changes.
20. Python is portable because it runs on many platforms like Windows, macOS, Linux, iOS, Android, and the web.
:::

:::{seealso} Good Programming Practice Solutions
:class: dropdown
**Refactored booking_system.py**

Refactored version of the **`booking_system.py`** file that follows good programming practices and addresses all activity tasks:

```python
import os

def clear_screen():
    """Clears the terminal screen in a cross-platform way."""
    os.system("cls" if os.name == "nt" else "clear")


def is_valid_seat(seat_number):
    """Returns True if seat number is between 0 and 50."""
    try:
        seat = int(seat_number)
        return 0 <= seat <= 50
    except ValueError:
        return False


def collect_bookings():
    """
    Collects booking information from users.

    Returns:
        list: A list of bookings in the format [(name, seat_number), ...]
    """
    bookings = []

    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue

        seat = input("Enter seat number (0–50): ").strip()
        if not is_valid_seat(seat):
            print("Invalid seat number.")
            continue

        bookings.append((name, seat))
        more = input("Add another booking? (y/n): ").lower().strip()
        if more == "n":
            break

    clear_screen()
    return bookings


def show_bookings(bookings):
    """Prints all collected bookings to the screen."""
    print("Your Bookings:")
    for booking in bookings:
        print(f"{booking[0]} - Seat {booking[1]}")


def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("Cinema Booking System")
        print("1. Book a Seat")
        print("2. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            bookings = collect_bookings()
            show_bookings(bookings)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()
```

---

**Summary of Fixes**

Style and Naming Issues:

- Changed function and variable names to follow `snake_case`
- Added clear, descriptive names
- Followed [PEP 8](https://peps.python.org/pep-0008/) for formatting

Maintainability Issues:

- Broke up long and unclear code into small, single-purpose functions
- Added `docstrings` and `block comments`
- Removed hardcoded platform-specific logic from main functions

Efficiency Problems:

- Removed repeated input validation logic
- Used return values and parameters to pass data cleanly between functions

| Error Type | Correction |
| --- | --- |
| Syntax Errors | missing colons<br>bad assignment (`=` instead of `==`) |
| Runtime Errors | unsafe `int()` conversions<br>use of `break` outside loops |
| Logic Errors | incorrect seat validation<br>improper input handling |

---

**Testing Plan Example**

| Test Type | Test |
| --- | --- |
| Exploratory Test | Input: blank name, out-of-range seat, enter "n" to exit loop<br>Result: All errors handled, loop exits properly |
| Unit Tests | 1. `is_valid_seat("25")` returns `True`<br>2. `is_valid_seat("hello")` returns `False` |
| Integrated Test | Run the full program, enter two valid bookings, then exit<br>Output: Prints both bookings accurately and confirms program flow |
:::

### Programming Paradigms

:::{seealso} Programming Paradigms Solutions
:class: dropdown
1. **Inheritance** – it lets `Car` reuse the code from `Vehicle`, reducing repetition and improving structure.
2. **MVC pattern** – separates data (Model) from display (View), making the app easier to manage and update.
3. **Event-driven programming** – event handlers respond to user actions like clicks or key presses.
4. One is working on the **View**, the other on the **Model** – MVC allows both to work independently without conflict.
5. **Event handler** – triggered by the event loop when the key press is detected.
6. **Object-Oriented Programming (OOP)** – allows the use of classes and objects to model shared and unique behaviours.
:::

## User Experience

### User Experience Introduction

:::{seealso} User Experience Activities
:class: dropdown
1. User Experience (UX) refers to the overall experience a person has when interacting with a digital product, including how easy it is to use, how efficient and satisfying the experience is, and whether it meets the user's needs and expectations.
2. User-first design is important because it ensures the solution meets the needs of the people using it, while developer-first or machine-first design can lead to frustration and poor usability.
:::

### Useability

:::{seealso} Useability Solutions
:class: dropdown
**Activity 1**

| Issue # | Usability Principle | Suggested Improvement |
| :--- | :--- | :--- |
| 1 | Safety | Move the 'Delete' button away from 'Save' and add a confirmation dialog before deletion. |
| 2  | Accessibility | Use a high-contrast colour scheme (e.g. black text on white background) and test using the Colour Contrast Analyser. |
| 3 | Learnability | Add an onboarding tutorial, tooltips, or a help screen with brief explanations. |
| 4 | Efficiency / Utility | Add a dropdown list or autocomplete for common subjects to save time and reduce errors. |
| 5 | Effectiveness / Safety | Prevent crashes by making due date optional or showing a clear error message before saving. |
| 6 | Effectiveness / Reliability | Fix the reminder system to ensure it works consistently, even after the app is closed. |
| 7 | Learnability / Accessibility  | Add text labels or tooltips to icons and use familiar symbols (e.g. trash can for delete). |
| 8 | Safety | Include a confirmation step before deleting tasks to avoid accidental loss. |
| 9 | Accessibility / Effectiveness | Increase button size and spacing for easier touch use, especially on mobile. |
| 10 | Safety / Utility | Instead of deleting completed tasks, move them to a “Completed” tab with an option to restore. |
:::

### Visual Communication 

:::{seealso} Alignment Activity Solution
:class: dropdown
**Examples of Alignment on the LEGO Website:**

- **Top Navigation Bar**:
  Menu items like “Shop,” “Discover,” “Help,” and the search and cart icons are horizontally aligned, creating a clean and organized header.

- **Product Grid Layout**:
  On category pages, products are aligned vertically in columns and horizontally in rows, making it easy to scan and compare items.

- **Homepage Banners**:
  Promotional text and buttons are aligned with images or backgrounds. For example, text is often left-aligned or centred depending on the layout, maintaining visual consistency.

- **Footer Links**:
  Links in the footer are aligned into neat columns under headings like “About Us,” “Support,” and “Legal,” allowing for quick navigation and readability.

- **Text Blocks and Images**:
  On product pages, text descriptions, prices, and buttons are left-aligned with the product image, ensuring a coherent flow of information.
:::

:::{seealso} Balance Activity Solution
:class: dropdown
**Examples of Balance on the LEGO Website:**

- **Homepage Hero Sections**:
  Large feature images are visually balanced with text boxes or call-to-action buttons placed on the opposite side, achieving symmetrical or asymmetrical balance.

- **Product Pages**:
  Images on the left and product information (name, price, reviews, buttons) on the right create a balanced layout that guides the user’s attention naturally.

- **Category Pages**:
  Products are evenly spaced in a grid format, ensuring visual weight is distributed across the screen, maintaining consistent spacing and size.

- **Navigation and Icons**:
  The logo, navigation menu, and icons (search, cart, account) are placed to balance each other across the top bar, preventing the header from feeling lopsided.

- **Mobile View**:
  Sections are stacked with equal spacing and centred elements, preserving balance in a vertical layout suited for smaller screens.
:::

:::{seealso} Contrast Activity Solution
:class: dropdown
**Examples of Contrast on the LEGO Website:**

- **Text and Background**:
  White or yellow text is used on dark backgrounds (e.g. banner images), and black or dark text on light backgrounds, making content easy to read.

- **Call-to-Action Buttons**:
  Buttons like “Add to Bag” or “Shop Now” are in bright colours (e.g. blue, yellow, or red) that stand out against the surrounding content.

- **Product Thumbnails**:
  Bold colours of LEGO sets contrast strongly with neutral backgrounds, making the products pop and attract attention.

- **Sale and Promotion Labels**:
  Discounts or special offers use red or yellow tags that contrast with the usual site colours, drawing the user’s eye immediately.

- **Hover Effects**:
  Interactive elements such as buttons or product cards use contrast changes (e.g. background darkens or border appears) to show they are clickable.
:::

:::{seealso} Harmony Activity Solution
:class: dropdown
**Examples of Harmony on the LEGO Website:**

- **Consistent Colour Palette**:
  The site uses LEGO’s signature colours (red, yellow, blue, black, white) throughout, creating a unified and familiar brand experience.

- **Typography**:
  Fonts are used consistently across headings, body text, and buttons, which helps maintain a harmonious and professional appearance.

- **Icon and Button Styles**:
  Icons (e.g. cart, user profile, search) and buttons share consistent shapes, outlines, and animations, contributing to a cohesive interface.

- **Spacing and Layout**:
  Margins, padding, and alignment are consistent across all pages, making each section feel like part of a unified design.

- **Product Presentation**:
  Product images follow the same framing, lighting, and background style, creating visual harmony across listings and pages.
:::

:::{seealso} Repetition Activity Solution
:class: dropdown
**Examples of Repetition on the LEGO Website:**

- **Navigation Structure**:
  The top menu bar with categories like “Shop,” “Discover,” and “Help” is repeated on every page, helping users know where to find information.

- **Product Cards**:
  Each product uses a repeated format: image, name, price, and “Add to Bag” button. This consistent structure makes browsing easier.

- **Icons and Buttons**:
  Icons (cart, user, search) and buttons use repeated shapes, sizes, and colours throughout the site for visual consistency.

- **Section Layouts**:
  Sections such as "Recommended for You," "Popular Sets," and "New Releases" follow a repeated horizontal scrolling format.

- **Colour and Branding**:
  LEGO’s red and yellow brand colours are repeated throughout the site in banners, buttons, and labels, reinforcing brand identity.
:::

:::{seealso} Hierarchy Activity Solution
:class: dropdown
**Examples of Hierarchy on the LEGO Website:**

- **Homepage Banners**:
  Large images with bold headlines and smaller subtext create a clear visual order, drawing attention to key promotions first.

- **Product Pages**:
  Product names appear in large, bold text, followed by price, reviews, and then detailed descriptions, guiding the user from most important to least.

- **Call-to-Action Buttons**:
  Buttons like “Add to Bag” or “Shop Now” are larger, brightly coloured, and centrally placed, making them stand out as the next step.

- Navigation Menu:
  Primary categories (e.g. “Shop,” “Discover”) are placed at the top, while subcategories appear only after interaction, showing importance levels.

- **Text Styling**:
  Fonts vary in size and weight — headings are bold and larger, while supporting details are smaller — helping users quickly scan for key info.
:::

:::{seealso} Proximity Activity Solution
:class: dropdown
**Examples of Proximity on the LEGO Website:**

- **Product Listings**:
  Product image, name, price, and “Add to Bag” button are grouped closely together, showing they belong to the same item.

- **Navigation Menu**:
  Related links such as “Shop by Age,” “Shop by Theme,” and “Offers” are grouped in dropdown menus, helping users find related content easily.

- **Checkout Section**:
  Shipping details, payment options, and order summary are placed near each other, showing they are part of the same process.

- **Homepage Sections**:
  Headings are positioned close to their related images and descriptions, clearly linking the content together.

- **Footer Links**:
  Information like “Customer Service,” “About Us,” and “Legal” are grouped under clear headings, showing their related purpose.
:::

:::{seealso} Colour Activity Solution
:class: dropdown
**Examples of Colour Use on the LEGO Website:**

- **Brand Identity**:
  LEGO’s primary colours (red, yellow, blue) are used consistently across the site to reinforce brand recognition and create harmony.

- **Contrast**:
  Bright colours (e.g. yellow buttons on dark backgrounds) are used to create contrast, making important elements like calls-to-action stand out.

- **Hierarchy**:
  Colour intensity and brightness are used to highlight what’s most important. For example, “Add to Bag” buttons are brighter than surrounding text, drawing attention first.

- **Repetition**:
  Consistent use of colour for buttons, icons, and headings helps users quickly recognise similar functions or sections across the site.

- **Grouping (Proximity and Colour)**:
  Background shades (e.g. white, grey, or coloured panels) are used to visually separate sections, aiding in grouping related content.
:::

:::{seealso} Form Activity Solution
:class: dropdown
**Examples of Form Use on the LEGO Website:**

- **Product Thumbnails**:
  LEGO sets are shown in 3D-rendered images or angled photos that emphasise their physical form, helping users visualise the product.

- **Buttons and Icons**:
  Rounded rectangles and consistent button shapes provide a familiar and clickable form, supporting usability and harmony.

- **Homepage Visuals**:
  Large banners feature LEGO models with clear form and structure, using shadows and depth to create visual interest and contrast.

- **Category Icons**:
  Icons representing age ranges, themes, or collections use simplified forms that are easy to recognise and differentiate.

- **Interactive Elements**:
  Hover effects on buttons and cards create a sense of movement and depth, reinforcing form through visual feedback.
:::

:::{seealso} Line Activity Solution
:class: dropdown
**Examples of Line Use on the LEGO Website:**

- **Dividers Between Sections**:
  Thin horizontal lines are used to separate content areas, helping to create clear structure and visual hierarchy.

- **Navigation Menus**:
  Lines and borders are used to group dropdown items, improving proximity and making relationships between links clearer.

- **Product Cards**:
  Subtle lines around product tiles or within cards separate image, title, price, and button, guiding the eye through the layout.

- **Grid Layouts**:
  Invisible or faint lines structure the grid of products, creating alignment and balance across the page.

- **Hover Effects and Underlines**:
  Interactive text links often use underlines or bottom borders on hover, using line to signal interactivity.
:::

:::{seealso} Proportion Activity Solution
:class: dropdown
**Examples of Proportion Use on the LEGO Website:**

- **Product Cards**:
  Images are larger than text and buttons, reflecting their importance and drawing users’ attention first.

- **Headings vs Body Text**:
  Headings are significantly larger than supporting text, establishing hierarchy and helping users scan pages easily.

- **Call-to-Action Buttons**:
  Buttons like “Add to Bag” or “Shop Now” are proportionally larger than nearby text to make them visually dominant and easily clickable.

- **Hero Banners**:
  Featured sections on the homepage use oversized images and bold text to emphasise new or promoted products.

- **Icons and UI Elements**:
  Icons are proportionally balanced with the text and buttons they relate to, maintaining visual harmony and clarity.
:::

:::{seealso} Scale Activity Solution
:class: dropdown
**Examples of Scale Use on the LEGO Website**

- **Hero Banners**:
  Large-scale images and headlines at the top of the homepage draw immediate attention to featured products or promotions.

- **Product Images**:
  Product images are scaled larger than text or price to highlight the product and help users view details clearly.

- **Call-to-Action Buttons**:
  Buttons like “Add to Bag” are scaled up compared to surrounding text, making them easy to notice and interact with.

- **Heading Sizes**:
  Main headings are larger than subheadings and body text, creating a clear hierarchy and improving readability.

- **Mobile Responsiveness**:
  On smaller screens, elements are rescaled to maintain usability and visual balance while keeping the most important items easy to tap.
:::

:::{seealso} Shape Activity Solution
:class: dropdown
**Examples of Shape Use on the LEGO Website:**

- **Buttons and Input Fields**:
  Rectangular buttons with slightly rounded corners are used consistently, creating a clear and approachable interface.

- **Icons**:
  Simple geometric shapes (circles, squares, and rectangles) are used for icons like search, cart, and profile, supporting clarity and consistency.

- **Product Images**:
  LEGO sets are often photographed in ways that highlight their blocky, angular shapes, reinforcing the brand’s visual identity and creating harmony.

- **Content Blocks**:
  Sections of content are arranged in rectangular containers, helping users recognise grouped information and maintaining alignment.

- **Promotional Badges**:
  Shapes like stars or rounded tags are used to highlight promotions or featured products, creating visual contrast and drawing attention.
:::

:::{seealso} Space Activity Solution
:class: dropdown
**Examples of Space Use on the LEGO Website:**

- **Whitespace Around Elements**:
  Generous spacing between images, text, and buttons helps reduce clutter, making the content easier to read and improving overall clarity.

- **Product Grids**:
  Consistent spacing between product cards ensures balance and alignment, making it easy to scan and compare items.

- **Section Separation**:
  Clear space between homepage sections (e.g. banners, featured sets, and categories) defines each area and guides the user’s flow down the page.

- **Navigation and Dropdowns**:
  Menu items are spaced out to prevent accidental clicks and improve accessibility, especially on mobile devices.

- **Text Blocks**:
  Paragraphs and headings are spaced with clear margins and line spacing, enhancing readability and visual hierarchy.
:::

:::{seealso} Tone Activity Solution
:class: dropdown
**Examples of Tone Use on the LEGO Website:**

- **Backgrounds and Overlays**:
  Soft greys and muted tones are used behind text and product sections to maintain contrast while ensuring readability and a clean, modern look.

- **Product Photography**:
  Lighting and colour tone in product images are consistent, using bright and vibrant tones that reflect LEGO’s playful and energetic brand.

- **Typography Tone**:
  Bold, cheerful colours like red, yellow, and white are used in headlines and calls to action, reinforcing a friendly and enthusiastic tone.

- **Hover Effects**:
  Subtle tonal shifts when hovering over buttons or links signal interactivity while maintaining a consistent visual style.

- **Seasonal and Promotional Themes**:
  Darker or lighter tones may be used in themed promotions (e.g. Halloween, Christmas) to reflect mood while staying within the LEGO aesthetic.
:::


:::{seealso} Texture Activity Solution
:class: dropdown
**Examples of Texture Use on the LEGO Website:**

- **Product Images**:
  High-resolution photos show the surface detail of LEGO bricks — their gloss, studs, and seams — giving a sense of physical texture and realism.

- **Background Graphics**:
  Some banners and themed sections use illustrated or photographic textures (e.g. bricks, walls, packaging) to add depth and visual interest.

- **Hover Effects**:
  Subtle shadowing or lighting changes on hover create the illusion of tactile response, enhancing interactivity through implied texture.

- **Thematic Pages**:
  Pages for specific sets or franchises (e.g. Star Wars, Technic) may include gritty, smooth, or metallic textures in the background to match the theme’s tone.

- **Contrast and Depth**:
  Textured visuals are used sparingly to contrast with flat design elements, helping key content stand out without overwhelming the user.
:::

### Impacts

:::{seealso} Personal Impacts Solution
:class: dropdown
**Activity 1: Fitness Tracker**

Positive Impacts:

- Improved awareness of health metrics (steps, heart rate, sleep)
- Motivation to achieve daily activity goals

Negative Impacts:

- Increased stress and anxiety from unmet goals
- Obsessive behaviour affecting mental health
- Disrupted work-life balance due to constant checking

Refinements:

- Introduce “rest days” or flexible goals
- Provide positive feedback without pressure
- Add mental health check-ins or screen-time warnings

---

**Activity 2: Study App**

Positive Impacts:

- Helps Jamie stay organised with study tasks
- Improves digital literacy through regular use

Negative Impacts:

- Privacy risk from data collection
- Financial pressure to upgrade to premium
- Distracting ads reduce usability

Refinements:

- Limit ad tracking and data collection
- Offer ad-free version for education users
- Improve transparency in privacy policy

---

**Activity 3: VR Social Platform**

Positive Impacts:

- Enhances social interaction in a safe space
- May reduce social anxiety for some users

Negative Impacts:

- Avoidance of real-life interactions
- Excessive screen time leading to fatigue
- Risk of emotional over-reliance on digital spaces

Refinements:

- Add usage time limits or reminders to log off
- Encourage real-life meetups or offline goals
- Include features to track emotional well-being
:::

:::{seealso} Social Impacts Solutions
:class: dropdown
**Activity 1: Facial Recognition in Public Spaces**

Equity & Inclusion:

- Studies show facial recognition is significantly less accurate for people with darker skin tones, women, and young people. This can lead to disproportionate targeting, mistaken identity, and harassment, particularly affecting minority and vulnerable groups.
- People from culturally and linguistically diverse (CALD) backgrounds may be overrepresented in databases used for surveillance, reinforcing systemic bias.

Well-being & Safety:

- Although promoted as a safety tool, the system may create anxiety and discomfort. Citizens may feel they are constantly monitored, even when not doing anything wrong.
- It can erode public trust in government institutions and law enforcement, especially among communities with a history of being unfairly policed.

Unintended Societal Effects:

- Normalisation of surveillance may discourage protest and free expression.
- Increased social division as people perceive they are being unfairly watched, especially if surveillance is heavier in lower-income or high-diversity areas.
- Sets a precedent for expanding surveillance technologies without strong public oversight.

Recommendations:

- Implement strict policies defining when and where facial recognition can be used.
- Require transparency about how data is stored, who has access, and for how long.
- Mandate third-party bias audits and ban use in schools or areas not proven to benefit from it.
- Provide clear opt-out mechanisms or alternatives for those who do not consent to be scanned.

---

**Activity 2: AI Hiring Tool**

Economic Participation:

- Automating hiring processes can save time and reduce some biases, but often also reduces job opportunities for people with non-traditional experience or resumes (e.g. career changers, refugees, older adults).
- If the AI prefers characteristics based on previous successful hires (e.g. attending elite schools), it reinforces existing barriers to economic mobility.

Equity & Inclusion:

- Marginalised groups (e.g. women, First Nations people, people with disabilities) may be excluded due to algorithmic bias in resume screening.
- AI trained on biased historical hiring data may unintentionally penalise applicants based on name, gender, or cultural background.
- Neurodivergent applicants or those with non-linear career paths may be filtered out unfairly.

Social Justice:

- AI hiring lacks transparency; candidates don’t know how decisions are made, and there may be no way to appeal or request human review.
- Raises legal and ethical concerns under anti-discrimination laws, especially if fairness was not considered in the AI's design.

Recommendations:

- Require human review at critical stages to catch unfair rejections.
- Use diverse training data and conduct regular audits to identify discriminatory outcomes.
- Clearly inform applicants how AI is used and provide meaningful opt-out or appeal options.
- Engage legal and ethical experts when designing or purchasing AI systems.

---

**Activity 3: School Communication App**

Community & Culture:

- The app strengthens parent–teacher communication for tech-savvy families, increasing engagement and transparency.
- However, it weakens relationships with families who lack devices, don’t speak English well, or feel intimidated by digital tools. These families may feel excluded from the school community.

Equity & Inclusion:

- Digital divide is a major issue: low-income households may not have smartphones or internet. Remote or Indigenous communities may have limited connectivity.
- Migrant parents or carers with low literacy may struggle with apps in English.
- Children in these homes miss updates, permission notes, and homework alerts, increasing inequality.

Education Access and Fairness:

- Homework reminders, timetable updates, or absence notifications may never reach some families, leading to lower attendance, missed assignments, and disengagement.
- Some students may be embarrassed that their families don’t use the app, affecting confidence and sense of belonging.

Recommendations:

- Provide printed newsletters and SMS updates for families without app access.
- Translate communications into relevant community languages.
- Survey families to identify barriers to access and target support.
- Offer school workshops on digital literacy for parents.
- Design the app to function on low-bandwidth connections and older devices.
:::

:::{seealso} Economic Impacts Solutions
:class: dropdown
**Activity 1: Digital Tax Filing System**

Economic Productivity:

- Businesses save time on paperwork and manual calculations, reducing admin overhead.
- The Australian Taxation Office also reduces manual processing, increasing speed and accuracy of returns.
- Integration with accounting software means less duplication and fewer errors across the system.

Public Revenue & Policy:

- Improved compliance through automated prompts and reduced opportunities for errors or fraud.
- Broader tax base coverage due to ease of use for freelancers and small businesses.
- Potential need to update tax regulations to align with digital record-keeping and enforcement.

Cost-Benefit & ROI:

- Initial development costs may be high, but savings in processing and increased revenue offset these over time.
- Reduced costs for physical infrastructure (e.g. fewer tax offices and mailing systems).
- High return on investment if adoption is widespread.

Employment & Workforce:

- Less need for front-counter staff and manual data entry roles.
- New roles created in software development, cybersecurity, and digital customer support.
- Upskilling programs required for current tax office staff.

---

**Activity 2: E-Commerce Platform for Rural SMEs**

Market Growth & Trade:

- Enables rural producers to reach urban and international customers directly, bypassing middlemen.
- Increases potential for exports of artisan goods, local produce, and niche products.
- Stimulates competition and innovation among regional businesses.

Inclusion & Access:

- Reduces geographic disadvantage by levelling the playing field for remote communities.
- Supports Indigenous-owned or women-led rural enterprises to access new markets.
- Requires support for internet access and digital literacy to be truly inclusive.

Employment & Workforce:

- New jobs in order fulfilment, digital marketing, product design, and customer service.
- Rural youth may see more reason to remain in their communities with online income opportunities.
- Requires training programs to build e-commerce and logistics skills.

Resilience & Innovation:

- Builds economic resilience by diversifying rural income sources.
- Encourages innovation through digital entrepreneurship.
- Helps communities adapt to agricultural downturns or climate-related challenges by tapping into non-farming revenue.

---

**Activity 3: AI Automation in Manufacturing**

Economic Productivity:

- AI systems increase output speed and reduce waste through precise quality control.
- Operational costs decrease due to fewer errors and downtime.
- Global competitiveness improves, attracting foreign investment and increasing exports.

Employment & Workforce:

- Low-skilled jobs (e.g. manual inspection, warehouse roles) are displaced.
- High demand for data analysts, AI engineers, and robotics technicians.
- Requires strong national focus on reskilling and vocational education reform to prevent unemployment.

Resilience & Innovation:

- Automated systems adapt quickly to changes in demand or disruptions in supply chains.
- AI encourages innovation in product design and customisation.
- Stronger ability to compete with advanced economies in the global tech-driven market.

Public Revenue & Policy:

- Decline in payroll tax from lost jobs may impact revenue.
- Potential for new tax policies targeting automation or AI-driven productivity.
- Public investment needed in training subsidies, social safety nets, and digital infrastructure.
:::

:::{seealso} Algorithm Solutions
:class: dropdown
**Activity 1: Sorting Student Names**

1. Take a list of all student names
2. Compare the first two names
3. If they are out of order, swap them
4. Repeat the comparison for the next pair
5. Continue until the entire list is sorted
6. Repeat the process if needed until no more swaps are made

---

**Activity 2: Vending Machine Simulation**

1. Display available items and their prices
2. Wait for the user to select an item
3. Ask the user to insert money
4. Check if the inserted amount is equal to or greater than the item price
5. If not enough, ask for more money
6. If enough, dispense the item
7. Give change if needed

---

**Activity 3: Password Strength Checker**

1. Get the password input from the user
2. Check if the password is at least a minimum number of characters (e.g. 8)
3. Check if it contains at least one uppercase letter
4. Check if it contains at least one number
5. Check if it contains at least one special character (e.g. !, @, #)
6. If all rules are met, mark as "Strong"; otherwise, mark as "Weak"
:::

## Data

### Data Introduction

:::{seealso} Data Activities
:class: dropdown
1. Data-driven solutions collect or access quality data, query that data, and interpret it to provide insight.
2. The DIKW Pyramid represents how raw data is transformed into wisdom through context, experience, and action.
3. Information is data with added context such as who, what, when, and where.
4. Applying action to knowledge transforms it into wisdom.
5. Value increases up the DIKW Pyramid because each level adds more meaning and usefulness.
6. 3000mm becomes wisdom when you realise it won’t fit in your car and decide to get it delivered.
7. Data-driven programming involves filtering, transforming, and aggregating structured data.
8. The three layers are external (UI), logical (data organisation), and internal (storage systems).
9. The external layer shows the user interface and represents data in a meaningful way.
10. The logical layer ensures data integrity, reliability, and validity.
:::

### Data Principles

:::{seealso} Data Management Activities
:class: dropdown
1. The two key factors are the timeliness of data acquisition and the ownership of the data.
2. Personal ownership relates to individual data, corporate ownership to organisational data, and public ownership to government or shared public data.
3. Data integrity means keeping data accurate, complete, consistent, and protected from unauthorized changes or damage.
4. Data must be complete, accurate, up to date, consistent, secure, and relevant.
5. A data anomaly is an error or inconsistency that can affect accuracy, completeness, or consistency in a database.
6. Insertion anomalies prevent adding data without unnecessary information, deletion anomalies cause loss of important data, and update anomalies create inconsistencies during changes.
7. Proper design, normalization, and data validation reduce anomalies and improve data reliability.
8. Threats include malware (viruses, worms, Trojans, ransomware, spyware, adware, rootkits), data theft, identity theft, and invasion of privacy.
9. User-level access control limits user access based on roles, enforces policies, and allows monitoring of activities to prevent unauthorized use.
10. Encryption is a reversible process using a key to scramble and unscramble data, while hashing is a one-way process that cannot be reversed, used for secure password storage.
:::

:::{seealso} Data Representation Solutions
:class: dropdown
1. Representation refers to how different types of data, like text and numbers, are converted into a format (usually 0s and 1s) that computers can understand.
2. ASCII represents each letter, number, or symbol as a specific number, like 'A' being 65.
3. Unicode is preferred because it can represent characters from almost all languages, as well as emojis and special symbols.
4. Unicode can represent non-English characters, emojis, and symbols from global languages that ASCII cannot.
5. Knowing whether your data uses ASCII or Unicode ensures it is interpreted and displayed correctly.
6. Consistent data formats ensure accuracy and reliability when storing and using data in a database.
7. 100,000 can also be represented as \$10^5\$; both are the same value but different formats.
8. A data format must be decided early to ensure consistency across all records in a database.
9. The international standard for dates is `yyyy-mm-dd`, known as ISO 8601.
10. In the 24-hour system, 1:15pm is written as 13:15; in the 12-hour system, it’s written as 1:15pm.
11. Time formatting uses H/h for hours, m for minutes, s for seconds, and A for AM/PM.
12. 0 represents a required digit, while 9 represents an optional digit between 0 and 9.
13. A common mobile number format is 0000 000 000.
14. Currency often uses two decimal places, such as \$90.00.
:::

### Structuring Data

:::{seealso} Database Types Solutions
:class: dropdown
1. A flat file database stores data in a simple table with rows and columns, where each row is a record and each column is a field.
2. Flat file databases can't handle complex relationships because they only use a single table with no links between data.
3. Flat file databases use one table without relationships, while relational databases use multiple linked tables with predefined relationships.
4. Data in a relational database is organized into tables with rows representing records and columns representing attributes.
5. A primary key is a unique column in a table that identifies each row.
6. A foreign key is a primary key from one table used in another table to create a relationship between them.
7. SQL is used to add, update, delete, and retrieve data in relational databases.
8. ACID stands for Atomicity, Consistency, Isolation, and Durability.
9. Atomicity ensures that all steps in a transaction are completed or none are, preventing partial changes.
10. Consistency ensures that a transaction moves the database from one valid state to another, following the rules of the schema.
11. Isolation prevents interference between concurrent transactions so each behaves as if it's the only one running.
12. Durability makes sure committed changes are permanent and survive system crashes.
13. A data value is the actual piece of information in a cell of a table.
14. Relational databases are good for business and web apps because they handle structured data and complex relationships efficiently.
:::

:::{seealso} Normalisation Solutions
:class: dropdown
1. The main goal of database normalisation is to minimise data redundancy and eliminate anomalies by organising data into smaller, related tables.
2. Data redundancy is the unnecessary repetition of data, which increases database size and risks data integrity.
3. An insertion anomaly happens when adding new data requires repeating existing data, leading to inefficiency and potential errors.
4. A deletion anomaly occurs when removing one dataset unintentionally deletes related information that should have been kept.
5. Update anomalies cause inconsistencies when a change isn't applied everywhere, resulting in conflicting data about the same entity.
6. Normalisation reduces redundancy by breaking large tables into smaller ones and linking them through common fields.
7. The “Divide and Rule” approach means splitting a large table into multiple smaller tables, each focused on one concept.
8. The STUDENTS TABLE is split into a Student Table (`rollno`, `name`, `branch`) and a Branch Table (`branch`, `hod`, `office_tel`).
9. Normalisation solves the insertion anomaly by allowing new student entries without repeating branch details, which are stored separately.
10. After normalisation, updating the HOD requires a change in only one place—the Branch Table—ensuring consistency for all students.
:::

:::{seealso} First Normal Form Solutions
:class: dropdown
**Table 1**

| SaleID | Region | ProductName | ProductPrice |
| --- | --- | --- | --- |
| 301 | East | Laptop | 999 |
| 302 | West | Phone | 799 |
| 303 | North | Tablet | 599 |
| 304 | South | Monitor | 299 |
| 305 | East | Mouse | 49 |

**Table 2**

| BookID | Title | Author | Available |
| --- | --- | --- | --- |
| 401 | Python Basics | John | TRUE |
| 401 | Python Basics | Maria | TRUE |
| 402 | Data Science Intro | Alice | TRUE |
| 403 | SQL in Practice | Robert | FALSE |
| 403 | SQL in Practice | Emma | FALSE |
| 403 | SQL in Practice | Lee | FALSE |
| 404 | Web Dev Essentials | Sophia | TRUE |
| 405 | Coding with Kids | Chris | FALSE |
| 405 | Coding with Kids | Dana | FALSE |

**Table 3**

| EmployeeID | Name | Phone | Email |
| --- | --- | --- | --- |
| 201 | Oliver White | 0400123456 | NULL |
| 202 | Jack Smith | NULL | jack@example.com |
| 203 | Emily Rose | 0499123456 | NULL |
| 204 | Grace Blue | NULL | grace@email.com |
| 205 | Harry Gray | 0420123456 | NULL |

**Table 4**

| OrderID | CustomerName | Item |
| --- | --- | --- |
| 101 | Emma Stone | Laptop |
| 101 | Emma Stone | Mouse |
| 102 | Liam Gray | Phone |
| 103 | Ava Green | Tablet |
| 103 | Ava Green | Stylus |
| 104 | Noah Brown | Monitor |
| 105 | Mia Black | Keyboard |
| 105 | Mia Black | Mousepad |
:::

:::{seealso} Second Normal Form Solutions
:class: dropdown
**Table 1**

Enrolments Table

| student_id | course_id | grade |
| --- | --- | --- |
| 101 | C01 | B |
| 102 | C02 | A |
| 103 | C01 | C |
| 104 | C03 | B |
| 105 | C02 | B |

Courses Table

| course_id | course_title   |
| --- | --- |
| C01 | Web Design |
| C02 | Data Structures |
| C03 | Networking |

**Table 2**

Transactions Table

| customer_id | product_id | quantity |
| --- | --- | --- |
| C01 | P01 | 2 |
| C02 | P02 | 1 |
| C03 | P01 | 1 |
| C04 | P03 | 3 |
| C05 | P02 | 1 |

Products Table

| product_id | product_name |
| --- | --- |
| P01 | Smartphone |
| P02 | Laptop |
| P03 | Headphones |

**Table 3**

Borrowings Table

| member_id | book_id | borrow_date |
| --- | --- | --- |
| M01 | B01 | 2024-01-01 |
| M02 | B02 | 2024-01-05 |
| M03 | B01 | 2024-01-06 |
| M04 | B03 | 2024-01-07 |
| M05 | B02 | 2024-01-08 |

Books Table

| book_id | book_title      |
| --- | --- |
| B01 | Python Basics |
| B02 | SQL Fundamentals |
| B03 | Java Programming |

**Table 4**

Attendance Table

| participant_id | session_id | attended |
| --- | --- | --- |
| P01 | S01 | Yes |
| P02 | S02 | No |
| P03 | S01 | Yes |
| P04 | S03 | Yes |
| P05 | S02 | Yes |

Sessions Table

| session_id | session_topic    |
| ---| --- |
| S01 | Cybersecurity |
| S02 | Web Accessibility |
| S03 | Cloud Computing |
:::

:::{seealso} Third Normal Form Solutions
:class: dropdown
**Table 1**

Employee Table

| employee_id | employee_name | department_id |
| --- | --- | --- |
| E01 | Alice | D01 |
| E02 | Bob | D02 |
| E03 | Charlie | D01 |
| E04 | Dana | D03 |
| E05 | Ethan | D02 |

Department Table

| department_id | department_name |
| --- | --- |
| D01 | Marketing |
| D02 | IT |
| D03 | HR |

**Table 2**

Book Table

| book_id | title | publisher_id |
| --- | --- | --- |
| B01 | Learn SQL | P01 |
| B02 | Python in Action | P02 |
| B03 | Web Design Pro | P01 |
| B04 | Java for Teens | P03 |
| B05 | HTML Basics | P02 |

Publisher Table

| publisher_id | publisher_name |
| --- | --- |
| P01 | TechBooks |
| P02 | CodeWorks |
| P03 | DevPress |

**Table 3**

Customer Table

| customer_id | name  | suburb_code |
| --- | --- | --- |
| C01 | Mia | S01 |
| C02 | Jake | S02 |
| C03 | Ruby | S01 |
| C04 | Noah | S03 |
| C05 | Chloe | S02 |

Suburb Table

| suburb_code | suburb_name |
| --- | --- |
| S01 | Southport |
| S02 | Ashmore |
| S03 | Burleigh |

**Table 4**

Product Table

| product_id | product_name | category_id |
| --- | --- | --- |
| PR01 | Mouse | CAT01 |
| PR02 | Keyboard | CAT01 |
| PR03 | Monitor | CAT02 |
| PR04 | Webcam | CAT03 |
| PR05 | Headset | CAT03 |
:::

:::{seealso} Full Normalisation Solution
:class: dropdown
Student Table

| student_id | student_name |
| --- | --- |
| S001 | Ali |
| S002 | Bella |
| S003 | Caleb |
| S004 | Diana |
| S005 | Ethan |

Subject Table

| subject_id | subject_name | teacher_name | department_id |
| --- | --- | --- | --- |
| SUB01 | Maths | Mr. Kay | D01 |
| SUB02 | English | Ms. Smith | D02 |
| SUB03 | History | Dr. Lee | D02 |

Department Table

| department_id | department_name |
| --- | --- |
| D01 | Science |
| D02 | Humanities |

Enrolment Table

| student_id | subject_id |
| --- | --- |
| S001 | SUB01 |
| S001 | SUB02 |
| S002 | SUB02 |
| S002 | SUB03 |
| S003 | SUB01 |
| S003 | SUB03 |
| S004 | SUB01 |
| S004 | SUB02 |
| S004 | SUB03 |
| S005 | SUB02 |
:::

### Managing and Manipulating Data

## Data Transmission

### Data Privacy

:::{seealso} General Privacy Solutions
:class: dropdown
1. Collection and sale of personal data, should address:
  - Lack of informed consent
  - Limited user understanding of terms and conditions
  - Transparency issues with companies
  - Ethical concerns of data being used or sold without clear permission
2. Risks from poor data storage and security should address:
  - Data breaches as targets for hackers
  - Identity theft
  - Financial loss
  - Reputational damage and emotional distress
3. Responsible data handling practices should address:
  - Transparency about data use and sharing
  - Clear communication with users
  - Building trust through honesty
  - User confidence and stronger relationships
:::

:::{seealso} Data as a Commodity Solutions
:class: dropdown
1. How is information similar to and different from traditional physical commodities like oil or gold?

   - Similarities: has economic value, can be traded, drives industries
   - Differences: intangible, can be copied/shared infinitely, low marginal cost

2. What characteristics make data valuable as an economic resource in the digital age?

   - Intangibility
   - Tradability (databases, reports, software, media)
   - Value creation (informs decisions, competitive advantage)
   - Market dynamics (supply, demand, private/public goods)
   - Low marginal cost of reproduction

3. What ethical and legal concerns can arise from treating personal data as a tradable commodity?

   - Exploitation of individuals’ digital footprints
   - Lack of informed consent in data collection
   - Privacy violations and surveillance
   - Risk of data misuse by third parties
   - Regulatory and legal compliance issues
:::

:::{seealso} Handling Personal Data Solutions
:class: dropdown
1. **Privacy Violations – How can collecting data without proper consent infringe on privacy?**

   - Collecting without authorization or consent exposes sensitive information
   - Breaches confidentiality
   - Even anonymized data can sometimes be re-identified, leading to privacy breaches

2. **Informed Consent – What makes informed consent critical for ethical data collection?**

   - Individuals must clearly understand what is being collected
   - They need to know how the data will be used
   - They should be told with whom the data may be shared
   - Many consent processes are inadequate because terms are too complex or unclear

3. **Data Security – Why is data security an ethical obligation for organizations?**

   - Prevents unauthorized access to data
   - Reduces risks of breaches or leaks
   - Protects individuals from identity theft
   - Prevents financial harm
   - Reduces reputational damage to individuals and organizations
   - High-profile breaches highlight the importance of robust security

4. **Bias and Discrimination – How can poor data handling reinforce bias?**

   - Datasets can be unrepresentative
   - Algorithms may perpetuate or amplify bias if not carefully managed
   - Leads to unfair or discriminatory outcomes
   - Facial recognition has been criticised for racial bias and inaccuracies

5. **Transparency and Accountability – Why are both needed in ethical data collection?**

   - Organizations must clearly state what data is collected
   - Must explain why it is collected
   - Must explain how it will be used
   - Transparency enables informed choices by individuals
   - Lack of transparency erodes trust and can lead to misuse or abuse

6. **Manipulative and Exploitative Practices – How can data be misused unethically?**

   - Used for manipulative marketing
   - Enables psychological profiling
   - Can drive social manipulation
   - Undermines individual autonomy
   - Can threaten democratic processes

7. **Data Ownership and Control – What are the debates about who owns personal data?**

   - Ongoing debate over whether individuals or organizations own data
   - Issues of who has the right to control its use
   - Increasingly important as data becomes a valuable asset

8. **Data Minimization and Purpose Limitation – Why should organizations limit what data they collect?**

   - Only collect data necessary for a specific purpose
   - Do not retain data longer than needed
   - Helps balance commercial interests with protecting individual rights

9. **Fairness in Use and Retention – Why is using data beyond original intent unethical?**

   - Using data for other purposes breaches fairness principles
   - Lack of explicit consent for new uses is unethical
   - Even if thought beneficial, it erodes user trust

10. **Legal and Regulatory Compliance – How do global laws influence ethical handling of personal data?**

    - GDPR (EU): explicit consent, minimization, rights to access/delete, data portability, breach notification, heavy penalties
    - US: mix of federal sectoral laws (HIPAA, GLBA, COPPA, FERPA, FCRA) and state laws (CCPA, CDPA, Colorado Privacy Act)
    - China: PIPL with strict consent, minimization, cross-border restrictions, severe penalties
    - Australia: Privacy Act & APPs requiring transparency, data quality/security, access/correction rights, cross-border limits
    - International influence: GDPR drives cookie consent popups, COPPA shapes age restrictions on social media
:::

:::{seealso} APP Solutions
:class: dropdown
1. Why do the Australian Privacy Principles exist, and what overall purpose do they serve?
   - Govern how organizations and government agencies handle personal information
   - Ensure privacy, transparency, and accountability
   - Protect individual rights in collection, use, storage, and disclosure

2. How do the APPs balance individual rights with the needs of organizations and government agencies?

   - Give individuals rights to access, correction, and privacy
   - Allow organizations to collect and use data where necessary for functions
   - Impose safeguards such as consent, limitation, and accountability

3. What might happen to public trust if organizations consistently fail to follow the APPs?

   - Erosion of user confidence
   - Increased concern about privacy and misuse of information
   - Potential withdrawal from services or complaints to regulators

4. How do the APPs connect with global privacy frameworks, such as the GDPR?

   - Share common principles: consent, minimization, access, correction, security
   - Influence of GDPR on international data protection practices
   - Help Australian organizations align with global standards

5. Why is it important for organizations to maintain a clear and up-to-date privacy policy?

   - Open and transparent management of personal information
   - Requirement for clearly expressed and current privacy policy

6. In what situations might an individual reasonably choose to deal with an organization anonymously or under a pseudonym?

   - APP requires option of anonymity or pseudonymity
   - Exceptions: impracticable or unlawful to do so

7. What limits are placed on organizations when collecting personal information?

   - Collect only information necessary for functions
   - Must be collected by lawful and fair means

8. How should an organization handle personal information it receives that it did not ask for?

   - Assess whether it could have been collected under APP 3
   - If not, must destroy or de-identify it

9. What information must an organization provide to an individual when collecting their personal information?

   - Notify individual at time of collection
   - Purpose of collection
   - Any third parties with whom data may be shared

10. Under what conditions can an organization use or disclose personal information for purposes other than the original collection?

   - Use or disclose only for the collected purpose
   - Exceptions apply in specific lawful cases

11. What obligations do organizations have if they use personal information for direct marketing?

   - Only use under certain conditions
   - Must provide simple opt-out option

12. What steps must organizations take before sending personal information overseas?

   - Take reasonable steps to ensure overseas recipients comply with APPs

13. Why are organizations restricted in their use of government-related identifiers such as Medicare numbers?

   - Cannot adopt, use, or disclose government identifiers
   - Limited exceptions where permitted by law

14. What steps must organizations take to ensure the personal information they collect is accurate and complete?

    - Take reasonable steps to ensure accuracy
    - Ensure information is up-to-date
    - Ensure information is complete

15. What kinds of measures should organizations implement to protect personal information?

    - Protect against misuse and interference
    - Prevent loss of information
    - Guard against unauthorized access, modification, or disclosure

16. What rights do individuals have to access their personal information, and what are the exceptions?
   - Right to access personal information held by organization
   - Subject to lawful exceptions

17. How should organizations handle requests to correct inaccurate or misleading personal information?

   - Take reasonable steps to correct information
   - Ensure it is accurate, up-to-date, complete, relevant, not misleading
:::

:::{seealso} Open Data Solutions
:class: dropdown
1. What is open data, and how is it typically made available?

   - Freely available for anyone to access, use, modify, and share
   - Published by governments, public institutions, or private organizations
   - Provided in accessible, machine-readable formats

2. What are the key features that make data truly "open"?

   - Freely accessible to all, regardless of user or purpose
   - Usable, reusable, and redistributable without restrictions
   - Structured for easy analysis and integration with other datasets

3. How does open data promote transparency and accountability in governments and organizations?

   - Enables citizens to scrutinize actions and performance
   - Increases transparency and allows public oversight
   - Example: showing school performance or government spending to empower communities

4. In what ways can open data drive innovation and contribute to economic growth?

   - Stimulates creation of new products, services, and business models
  
   - Fosters entrepreneurship and job creation
   - Example: release of weather and GPS data created new industries and billions in value

5. How does open data improve public services and government efficiency?

   - Sharing data across agencies improves decision-making
   - Reduces duplication of effort
   - Identifies unnecessary spending
   - Improves overall service delivery

6. Why is open data important for scientific research and collaboration?

   - Accelerates discovery by enabling validation of findings
   - Allows researchers to build upon existing work
   - Encourages collaboration across disciplines and borders

7. How can open data empower individuals and communities to make informed decisions?

   - Provides access to relevant information
   - Enables informed choices
   - Supports participation in civic life
   - Helps advocate for community needs

8. What role does open data play in encouraging social welfare and civic participation?

   - Informs public debate
   - Supports evidence-based policy
   - Enables social innovation
   - Improves social outcomes

9. What are some major open data sources available in Australia at national, state, and local government levels?

   - National: Data.gov.au, ABS, NationalMap
   - State/Territory: Data.NSW, Data.VIC, Data.Qld, DataSA, DataWA, LIST (Tasmania), DataACT, NT Open Data Portal
   - Council: Brisbane, Gold Coast, Logan, Redland open data portals

10. What is de-identification, and why is it important when publishing open data?

    - Removing or altering personal information so individuals cannot be identified
    - Protects privacy while allowing analysis and research
    - Helps organizations comply with laws like APPs or GDPR
    - Enables freer data sharing for research, policy, and innovation

11. What are the key steps involved in de-identifying data before it is released?

    - Removing direct identifiers (names, addresses, phone numbers, emails, Medicare numbers)
    - Modifying or generalizing indirect identifiers (e.g., age ranges instead of birth dates, partial removal of postcodes)
    - Applying data masking or perturbation (e.g., swapping data, adding noise, aggregating)

12. How does de-identification help organizations comply with privacy laws such as the APPs or GDPR?

    - Reduces the risk that individuals can be identified
    - Meets requirements of privacy laws regarding personal data handling
    - Allows safe sharing of data for research, policy-making, and innovation

13. What are the limitations and risks associated with de-identification of open data?

    - Not foolproof—re-identification still possible
    - Advances in analytics and other datasets can expose identities
    - Greater risk when datasets are rich or unique

14. Why must de-identification be treated as a continuous process rather than a one-time action?

    - New technologies create new re-identification risks
    - Additional datasets may combine to reveal identities
    - Requires regular review and updating to stay effective
:::

## Python Skills

### PyQt

### Working with CSV

### Type Hints

### Querying Databases

### Creating Databases

### Populating Databases

### Working with JSON and XML

### Requests

### OurAPI

### Ciphers

### Hashing

### Checksums

## SQL Skills

:::{seealso} SELECT Solutions
:class: dropdown
```{literalinclude} 08_sql/assets/SELECT/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/SELECT/Activity_2.sql
:language: sql
```

```{literalinclude} 08_sql/assets/SELECT/Activity_3.sql
:language: sql
```

```{literalinclude} 08_sql/assets/SELECT/Activity_4.sql
:language: sql
```

```{literalinclude} 08_sql/assets/SELECT/Activity_5.sql
:language: sql
```
:::

:::{seealso} WHERE Activities
:class: dropdown
**Using the Movies database**
```{literalinclude} 08_sql/assets/WHERE/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/WHERE/Activity_2.sql
:language: sql
```

```{literalinclude} 08_sql/assets/WHERE/Activity_3.sql
:language: sql
```

```{literalinclude} 08_sql/assets/WHERE/Activity_4.sql
:language: sql
```

```{literalinclude} 08_sql/assets/WHERE/Activity_5.sql
:language: sql
```

**Using the Repairs database**
```{literalinclude} 08_sql/assets/WHERE/Activity_6.sql
:language: sql
```

```{literalinclude} 08_sql/assets/WHERE/Activity_7.sql
:language: sql
```

**Using the World database**
```{literalinclude} 08_sql/assets/WHERE/Activity_8.sql
:language: sql
```

```{literalinclude} 08_sql/assets/WHERE/Activity_9.sql
:language: sql
```

```{literalinclude} 08_sql/assets/WHERE/Activity_10.sql
:language: sql
```
:::

:::{seealso} Filters and Aggregators Solutions
:class: dropdown
**Using the Movies database**
```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_2.sql
:language: sql
```

```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_3.sql
:language: sql
```

```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_4.sql
:language: sql
```

```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_5.sql
:language: sql
```

```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_6.sql
:language: sql
```

```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_7.sql
:language: sql
```

```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_8.sql
:language: sql
```

```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_9.sql
:language: sql
```

```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_10.sql
:language: sql
```
:::

:::{seealso} ORDER BY Solutions
:class: dropdown
**Using the Movies database**
```{literalinclude} 08_sql/assets/filters_and_aggregators/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/ORDER_BY/Activity_2.sql
:language: sql
```

```{literalinclude} 08_sql/assets/ORDER_BY/Activity_3.sql
:language: sql
```

**Using the School Database**

```{literalinclude} 08_sql/assets/ORDER_BY/Activity_4.sql
:language: sql
```

```{literalinclude} 08_sql/assets/ORDER_BY/Activity_5.sql
:language: sql
```

```{literalinclude} 08_sql/assets/ORDER_BY/Activity_6.sql
:language: sql
```
:::

:::{seealso} GROUP BY and HAVING Solutions
:class: dropdown
**Using the Movies database**
```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_2.sql
:language: sql
```

```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_3.sql
:language: sql
```

**Using the School database**

```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_4.sql
:language: sql
```

```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_5.sql
:language: sql
```

**Using the Shares database**

```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_6.sql
:language: sql
```

```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_7.sql
:language: sql
```

**Using the Chinook database**

```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_8.sql
:language: sql
```

```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_9.sql
:language: sql
```

```{literalinclude} 08_sql/assets/GROUP_BY_and_HAVING/Activity_10.sql
:language: sql
```
:::

:::{seealso} Subqueries Solutions
:class: dropdown
**Using the Schools database**
```{literalinclude} 08_sql/assets/subqueries/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/subqueries/Activity_2.sql
:language: sql
```

```{literalinclude} 08_sql/assets/subqueries/Activity_3.sql
:language: sql
```

```{literalinclude} 08_sql/assets/subqueries/Activity_4.sql
:language: sql
```

```{literalinclude} 08_sql/assets/subqueries/Activity_5.sql
:language: sql
```

**Repairs database**

```{literalinclude} 08_sql/assets/subqueries/Activity_6.sql
:language: sql
```

```{literalinclude} 08_sql/assets/subqueries/Activity_7.sql
:language: sql
```

```{literalinclude} 08_sql/assets/subqueries/Activity_8.sql
:language: sql
```

```{literalinclude} 08_sql/assets/subqueries/Activity_9.sql
:language: sql
```

```{literalinclude} 08_sql/assets/subqueries/Activity_10.sql
:language: sql
```
:::

:::{seealso} JOIN Solutions
:class: dropdown
**Using Repairs database**
```{literalinclude} 08_sql/assets/JOIN/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/JOIN/Activity_2.sql
:language: sql
```

```{literalinclude} 08_sql/assets/JOIN/Activity_3.sql
:language: sql
```

```{literalinclude} 08_sql/assets/JOIN/Activity_4.sql
:language: sql
```

**Using the Chinook database**

```{literalinclude} 08_sql/assets/JOIN/Activity_5.sql
:language: sql
```

```{literalinclude} 08_sql/assets/JOIN/Activity_6.sql
:language: sql
```

```{literalinclude} 08_sql/assets/JOIN/Activity_7.sql
:language: sql
```

**Using the Schools database**

```{literalinclude} 08_sql/assets/JOIN/Activity_8.sql
:language: sql
```

```{literalinclude} 08_sql/assets/JOIN/Activity_9.sql
:language: sql
```

```{literalinclude} 08_sql/assets/JOIN/Activity_10.sql
:language: sql
```
:::

:::{seealso} CREATE TABLE Solutions
:class: dropdown
**Activity 1**
```{literalinclude} 08_sql/assets/CREATE/Activity_1a.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_1b.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_1c.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_1d.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_1e.sql
:language: sql
```

---

**Activity 2**

```{literalinclude} 08_sql/assets/CREATE/Activity_2a.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_2b.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_2c.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_2d.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_2e.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_2f.sql
:language: sql
```

---

**Activity 3**

```{literalinclude} 08_sql/assets/CREATE/Activity_3a.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_3b.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_3c.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_3d.sql
:language: sql
```

---

**Activity 4**

```{literalinclude} 08_sql/assets/CREATE/Activity_4a.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_4b.sql
:language: sql
```

```{literalinclude} 08_sql/assets/CREATE/Activity_4c.sql
:language: sql
```
:::

:::{seealso} INSERT INTO Solutions
:class: dropdown
**Movies Database**
```{literalinclude} 08_sql/assets/INSERT/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/INSERT/Activity_2.sql
:language: sql
```

**Schools Database**
```{literalinclude} 08_sql/assets/INSERT/Activity_3.sql
:language: sql
```

```{literalinclude} 08_sql/assets/INSERT/Activity_4.sql
:language: sql
```

```{literalinclude} 08_sql/assets/INSERT/Activity_5.sql
:language: sql
```

**Chinook Database**
```{literalinclude} 08_sql/assets/INSERT/Activity_6.sql
:language: sql
```

```{literalinclude} 08_sql/assets/INSERT/Activity_7.sql
:language: sql
```

```{literalinclude} 08_sql/assets/INSERT/Activity_8.sql
:language: sql
```

```{literalinclude} 08_sql/assets/INSERT/Activity_9a.sql
:language: sql
```

```{literalinclude} 08_sql/assets/INSERT/Activity_9b.sql
:language: sql
```

```{literalinclude} 08_sql/assets/INSERT/Activity_10a.sql
:language: sql
```

```{literalinclude} 08_sql/assets/INSERT/Activity_10b.sql
:language: sql
```
:::

:::{seealso} UPDATE Statement Solutions
:class: dropdown
**World Database**

```{literalinclude} 08_sql/assets/UPDATE/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/UPDATE/Activity_2.sql
:language: sql
```

```{literalinclude} 08_sql/assets/UPDATE/Activity_3.sql
:language: sql
```

**Shares Database**

```{literalinclude} 08_sql/assets/UPDATE/Activity_4.sql
:language: sql
```

```{literalinclude} 08_sql/assets/UPDATE/Activity_5.sql
:language: sql
```

```{literalinclude} 08_sql/assets/UPDATE/Activity_6.sql
:language: sql
```

**Chinook Database**

```{literalinclude} 08_sql/assets/UPDATE/Activity_7.sql
:language: sql
```

```{literalinclude} 08_sql/assets/UPDATE/Activity_8.sql
:language: sql
```
:::

:::{seealso} DELETE Solutions
:class: dropdown
**School Database**

```{literalinclude} 08_sql/assets/DELETE/Activity_1.sql
:language: sql
```

```{literalinclude} 08_sql/assets/DELETE/Activity_2.sql
:language: sql
```

**Repairs Database**

```{literalinclude} 08_sql/assets/DELETE/Activity_3.sql
:language: sql
```

```{literalinclude} 08_sql/assets/DELETE/Activity_4.sql
:language: sql
```

**Chinook Database**

```{literalinclude} 08_sql/assets/DELETE/Activity_5a.sql
:language: sql
```

```{literalinclude} 08_sql/assets/DELETE/Activity_5b.sql
:language: sql
```

```{literalinclude} 08_sql/assets/DELETE/Activity_5c.sql
:language: sql
```

```{literalinclude} 08_sql/assets/DELETE/Activity_6a.sql
:language: sql
```

```{literalinclude} 08_sql/assets/DELETE/Activity_6b.sql
:language: sql
```

```{literalinclude} 08_sql/assets/DELETE/Activity_6c.sql
:language: sql
```

```{literalinclude} 08_sql/assets/DELETE/Activity_6d.sql
:language: sql
```

```{literalinclude} 08_sql/assets/DELETE/Activity_6e.sql
:language: sql
```
:::