# Testing

:::{dropdown} Learning Goals
By the end of this section you will:
- understand the importance of testing and documenting this testing
- know how to perform and document unit tests
- know how to perform and document integrated test
:::

In the [Good Programming Practice section](../02_coding/03_good_practice.md) we have already mentioned the three different types of testing:

- Exploratory testing
- Unit testing
- Integrated testing

Unit testing and integrated testing are excellent evidence of problem solving, refinement and justification for evaluation. In such, it is important to document this testing.

:::{warning} Teacher's marking considerations
:class: dropdown
No one always gets their code right the first time. Your testing should show both your successful and unsuccessful tests. The unsuccessful test and the subsequent resolution of the problem significantly contributes to the **effective refinements and recommendations** part of the **Evaluating Criteria** in FIA2, FIA3, IA2 and IA3.
:::

## Unit testing

Unit testing is a method where individual parts of a program, called units, are tested to ensure they work correctly. 

Imagine a program as a complex machine made of smaller parts, like gears. Each gear needs to work perfectly for the whole machine to function. In unit testing, developers write tests for these 'gears' &ndash; which could be functions or methods &ndash; to check if they perform as expected when given certain inputs. 

If a test fails, it means there's a problem with that part of the code, and it needs fixing before it can be used with other parts of the program. If unit passes all the tests, then the programmer can be confident that any future errors are not caused by this unit, therefore will not need to test it again unless its code is changed.

This approach helps catch errors early and simplifies debugging, making the development process more efficient and the final program more reliable.

### Performing Unit Tests

Follow these steps to run your unit tests:

1. **Complete a function or component**:
   - Once you have completed a function or component, you can test it. 
   - If the code calls other parts of your code, you need to ensure that code has previously passed a unit test.
2. **Plan test cases**:
   - Think of different situations the function should handle:
     - Normal/expected input
     - Boundary cases - values are at the edge of acceptable ranges, such as the smallest or largest valid number
     - Invalid input
3. **Run the function manually**:
   - Use print statements to run your function with your test cases.
   - You make create a sperate Python file for testing
4. **Compare actual vs expected output**
   - Check if what the function returned matches what you expected. 
   - If not, investigate the error.
5. **Refine your code if needed**
   - If it failed any test, change the code and test again.
6. **Record results**
   - Keep a simple table of results:

| Test case | Input | Expected Outcome | Actual Outcome | Pass/Fail | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | add(2, 3) | 5 | 5 | Pass | n/a |
| 2 | add(-1, 1) | 0 | 0 | Pass | n/a |
| 3 | add("a", 2) | Error | Crash | Fail | used `try except` block |
| 3 | add("a", 2) | Error | Error | Pass | n/a |

:::{seealso} Unit Testing Activities
:class: dropdown
**Activity 1**
Run a unit test on the following code:

``` {code}python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
```

---

**Activity 2**
Run a unit test on the following code:

``` {code}python
def average(a, b, c):
    return a + b + c / 3
```
:::

## Integrated testing

Integration testing is a phase in software testing where individual pieces of an application, often called units or modules, are combined and tested together as a group. The main goal of this testing is to check if these different parts work well together. For example, in a social media app, integration testing might involve checking if the part that handles user logins correctly interacts with the part that shows friends' posts. 

Integration testing allows testers to find and fix problems where the different parts of the software fail to properly communicate or work together.

In your projects, you will use integrated testing to ensure the [effectiveness](../03_user_experience/02_usability_principles.md#effectiveness) of your solution. 

### Performing Integrated Tests

Follow these steps to run your integrated tests:

1. **Identify components to test together**
   - E.g. user input &rarr; processing &rarr; database update &rarr; output display.

2. **List success criteria**
   - Use the ones you defined during solution planning (e.g. "Data must save correctly", "User sees confirmation message").
3. **Create test scenarios**
   - Describe real-world situations that involve multiple parts:
     - "Student logs in and updates their profile"
     - "User submits a form and sees a result"
4. **Run each scenario manually**
   - Follow the full process like an actual user would.
5. **Check system behaviour against each success criterion**
   - Did all components trigger correctly?
   - Was the result correct and visible to the user?
   - Did the system handle errors?
6. **Refine solution if needed**
   - Fix issues and re-test until all success criteria are met.
7. **Record results**
   - Keep a simple table of results:

| Scenario | Expected Outcome | Pass/Fail | Action |
| --- | --- | --- | --- |
| Student submits feedback form | Data saved to database | Pass | n/a |
| Student submits feedback form | Confirmation displayed | Pass | n/a |
| Student submits feedback form | System prevents blank submission | Fail | added UI error message |
| Student submits feedback form | System prevents blank submission | Pass | n/a |

:::{seealso} Integrated Testing Activities
:class: dropdown
**Activity 1**

Students use a web form to book spots in school events. Submitted data is stored in a database, and a confirmation message is displayed.

Plan integrated tests that cover the following:

- What components need to work together?
- What are the success criteria for each step?
- What data will you use to test?

Include in your design:

- 3 test scenarios with clear input data
- Expected results for database and confirmation messages
- How you will check if data is saved and output is correct

---

**Activity 2**

Staff view a weather dashboard that pulls live data from an API, stores it in a school-hosted database, and allows export of daily reports.

Plan how to test the full system working together:

- What components must integrate (e.g. login, API, database, report)?
- What success criteria should be met at each stage?
- What could go wrong?

Include in your design:

- 3 test scenarios that involve multiple components
- Test inputs and expected outcomes
- How to record if the system passed or failed each step
:::
