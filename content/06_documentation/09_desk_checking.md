# Desk Checking 📝

:::{dropdown} Learning Goals
By the end of this section you will:
- understand the importance of deskchecking
- know how to deskcheck branching code
- know how to deskcheck iterative code
:::

Desk checking is a manual (non computerised) technique for checking the logic of an algorithm. The person performing the desk check effectively acts as the computer, using pen and paper to record results. The desk checker carefully follows the algorithm being careful to rigidly adhere to the logic specified. The desk check can expose problems with the algorithm.

Desk checks are useful to check an algorithm (before coding) thereby confirming that the algorithm works as expected and reduces the likelihood of creating programs with logic errors. Another benefit of a desk check is that it confirms to the programmer/designer that the algorithm performs as intended.

:::{hint} Types of programming errors
:class: dropdown
There are three categories of computer errors: 

- **Syntax errors**:
    - occur due to violations of language grammar rules, eg. failing to put quotes around a string.
    - typically identified and corrected using development environment feedback
- **Runtime errors**
    - arise during program execution due to unexpected conditions, eg. the user entering a string instead of a integer.
    - require condition checks and error handling mechanisms for resolution
- **Logic errors**: 
    - result in incorrect outcomes due to flaws in the program's design or logic, eg. a condition using `>` instead of `<`.
    - requires thorough testing and debugging to understand and correct the program's behaviour.
:::

A desk check is normally done as a table with columns for:

- Pseudo code line number - Pseudo code doesn't normally have lines numbers, but these are necessary in a desk check to specify the line(s) being executed
- One column per variable used.
  - The columns should be in alphabetical order on variable name with the variable name at the top of the column.
  - As the algorithm is executed, the new values of the variables are put in the appropriate column.
  - Show working for calculations.
  - If variable names consist of a number of words it is permissible to put a space between each word in the name so that the name fits better in the column by wrapping to the next line. e.g. the variable column heading discount Price could be used rather than the actual variable name discountPrice.
- condition column.
  - The result of the condition will be true (T) or false (F).
  - As the algorithm is executed, conditions are evaluated and the details are recorded in the column.
  - Show working when evaluating the conditions.
  - This is used whenever a condition is evaluated - IF WHILE or FOR statements all have explicit or implicit conditions.
- Input/Output
  - used to show what is input by the user and displayed by the program.
  - Show inputs with: the variable name, a "?" and the value input e.g. price ? 200.
  - Show outputs with the variable name, an =, and the value displayed (or just the value displayed) e.g. discountPrice= 180 .

## Branching Example

Consider the following pseudocode:

``` pseudocode
1 BEGIN calcPrice()
2    INPUT price
3    IF price > 100 THEN
4        discount = price * 15 / 100
5        price = price - discount
6    ENDIF
7    DISPLAY price
8 END
```

Since it has branching logic, you will need to run a test for each of the branches (in this case two).

Inputs: price = \$200  
Correct results: price = \$170

| Line # | discount | price | Conditions | Input/Output |
| :--- | :--- | :--- | :--- | :--- |
| 1 | | | | |
| 2 |  | `200` |  | `price ? 200` |
| 3 |  | `200` | `price > 100 ? T `|  |
| 4 | `200 * 15 / 100 = 30` | `200` |  |  |
| 5 | `30` | `200 - 30 = 170` |  |  |
| 6 | `30` | `170` |  |  |
| 7 | `30` | `170` |  | `price = 170` |
| 8 | `30` | `170` |  |  |

Inputs: price = \$50  
Correct results: price = \$50.
  
| Line # | discount | price | Conditions | Input/Output |
| :--- | :--- | :--- | :--- | :--- |
| 1 | | | | |
| 2 | | `50` | | `price ? 50` |
| 3 | | `50` | `price > 100 ? F` | |
| 6 | | `50` | | |
| 7 | | `50` | | `price = 50` |
| 8 | | `50` | | |

## Iteration Example

Consider the following pseudocode:

``` pseudocode
1 BEGIN calcSquares()
2    DISPLAY "X", "X Squared"
3    FOR x = 1 TO 3
4        xSquared = x * x
5        DISPLAY x, xSquared
6    NEXT x
7    ENDFOR
8    DISPLAY "-----------"
9 END
```

| Line # | x | xSquared | Conditions | Input/Output |
| :--- | :--- | :--- | :--- | :--- |
| 1 | | | | |
| 2 | | | | `X, X Squared` |
| 3 | `1` | | `1 <= 3 ? T` | |
| 4 | `1` | `1 * 1 = 1` | | |
| 5 | `1` | | | `x = 1`, `xSquared = 1` |
| 6 | `1 + 1 = 2` | | | |
| 3 | `2` | | `2 <= 3 ? T` | |
| 4 | `2` | `2 * 2 = 4` | | |
| 5 | `2` | | | `x = 2`, `xSquared = 4` |
| 6 | `2 + 1 = 3` | | | |
| 3 | `3` | | `3 <= 3 ? T` | |
| 4 | `3` | `3 * 3 = 9` | | |
| 5 | `3` | | | `x = 3`, `xSquared = 9` |
| 6 | `3 + 1 = 4` | | | |
| 4 | | | `3 <= 3 ? F` | |
| 8 | | | | `DISPLAY "-----------"` |
| 9 | | | | |

:::{seealso} Desk Check Activities
:class: dropdown
Use desk checking to identify the logic errors in the following pseudocode algorithms. The correct results are given for each algorithm. You should be able to identify the line(s) of code that cause the incorrect results and explain why the error occurs.

**Activity 1**
```{code}
:linenos:
BEGIN check_pass
    INPUT mark
    IF mark > 50 THEN
        OUTPUT "Pass"
    ELSE
        OUTPUT "Fail"
    ENDIF
END
```

**Activity 2**
```{code}
:linenos:
BEGIN sum_five_numbers
    DECLARE count AS INTEGER
    FOR count = 1 TO 5
        INPUT num
        total = total + num
    NEXT count
    OUTPUT total
END
```

**Activity 3**
```{code}
:linenos:
BEGIN countdown
    INPUT n
    WHILE n > 0
        OUTPUT n
        n = n + 1
    ENDWHILE
    OUTPUT "Done"
END
```

**Activity 4**
```{code}
:linenos:
BEGIN user_login
    DECLARE login_attempts AS INTEGER = 3

    WHILE login_attempts < 0
        INPUT user_name
        INPUT user_password

        IF is_valid(user_name, user_password) THEN
            OUTPUT "Login successful"
            RETURN
        ENDIF

        login_attempts = login_attempts + 1
        OUTPUT "Invalid. " + login_attempts + " attempts left."
    ENDWHILE

    OUTPUT "Try again later"
END
```

**Activity 5**
```{code}
:linenos:
BEGIN grade_score
    INPUT mark

    IF mark >= 50 THEN
        OUTPUT "C"
    ELSE IF mark >= 70 THEN
        OUTPUT "B"
    ELSE IF mark >= 85 THEN
        OUTPUT "A"
    ELSE
        OUTPUT "D"
    ENDIF
END
```

**Activity 6**
```{code}
:linenos:
BEGIN check_pass
    INPUT mark
    IF mark > 50 THEN
        OUTPUT "Pass"
    ELSE
        OUTPUT "Fail"
    ENDIF
END
```
:::