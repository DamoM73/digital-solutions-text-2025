# FIAE - Exam

:::{dropdown} Learning Goals
By the end of this section you will:
- know the conditions and format of the Unit 2 exam
- know the topics and types of questions to prepare for
- know how to use perusal time and manage your time in the exam
:::

:::{tip} Exam Details
- Technique: Examination – combination response
- Unit: Unit 2 Application and data solutions
- Conditions:
  - Duration: 120 minutes
  - Perusal: 10 minutes
  - A separate stimulus book is provided
- Format:
  - Section 1: 10 multiple choice questions
  - Section 2: 5 short response questions
  - Section 3: 1 extended response question with 4 parts
- Marks:
  - Retrieving and comprehending: 6
  - Analysing: 7
  - Synthesising and evaluating: 8
  - Communicating: 4
  - Total: 25
:::

## What to expect

The exam comes in three books:

- **Multiple choice question book**: the Section 1 questions. This book isn't marked.
- **Question and response book**: where we write all our answers, including the multiple choice answers.
- **Stimulus book**: the scenarios, database tables, diagrams and screenshots that the questions refer to.

### Section 1: Multiple choice

Each question has four options. Fill in the answer bubble for our choice completely in the question and response book, using a 2B pencil. If we change our mind, erase the first answer completely.

### Section 2: Short response

Short response questions test one topic each. They often refer to the stimulus book. Answer in full sentences, except where the question asks for something else, such as SQL code, a table or a diagram.

### Section 3: Extended response

The extended response question gives us a scenario in the stimulus book, then asks us to develop parts of a solution for it. Each part builds on the parts before it. For example, a later part may ask us to use the diagram we drew in an earlier part.

:::{important} Each part builds on the last
:class: dropdown
If we're not happy with an earlier part, we shouldn't let it stop us. Make the best attempt we can, then use it for the later parts rather than leaving them blank.
:::

## Types of questions

Prepare for questions that ask us to:

- recognise and describe concepts, such as the DIKW pyramid, the usability principles and the data principles
- apply the usability and visual communication principles to a design, explaining what isn't working and how we would improve it
- write SQL queries for a database shown in the stimulus, including filters, aggregates, grouping, joins and subqueries, as well as statements that add or change data
- normalise tables into first, second and third normal form
- choose appropriate data types for data, and develop data dictionaries
- draw Level 0 and Level 1 data flow diagrams
- draw entity relationship diagrams for a scenario
- develop Input, Process, Output (IPO) tables that use SQL

## Topics covered

| Topic | Pages |
| --- | --- |
| DIKW pyramid | [](../04_data/01_intro.md) |
| Data principles | [](../04_data/02_data_principles.md) |
| Normalisation | [](../04_data/03_structuring_data.md) |
| Managing and manipulating data | [](../04_data/04_manipulating_data.md) |
| Usability principles | [](../03_user_experience/02_usability_principles.md) |
| Visual communication | [](../03_user_experience/03_visual_communication.md) |
| IPO tables | [](../02_coding/01_intro.md) |
| Data flow diagrams | [](../06_documentation/10_dfd.md) |
| Entity relationship diagrams | [](../06_documentation/11_erd_rs.md) |
| Data dictionaries | [](../06_documentation/12_data_dictionaries.md) |
| SQL | [](../08_sql/01_intro.md), [](../08_sql/02_select.md), [](../08_sql/03_where.md), [](../08_sql/04_filters_and_aggregators.md), [](../08_sql/05_order_by.md), [](../08_sql/06_group_by_and_having.md), [](../08_sql/07_subqueries.md), [](../08_sql/08_join.md), [](../08_sql/09_create.md), [](../08_sql/10_insert.md), [](../08_sql/11_update.md), [](../08_sql/12_delete.md) |

## Exam technique

### Perusal time

We can't write anything during the 10 minutes of perusal time. Use it to:

- read every question, and note how many marks each one is worth
- read the stimulus book, and match each stimulus to the questions that use it
- read the extended response question carefully, and start planning the diagrams in our head
- decide which questions to answer first

### Managing time

- Spend time in proportion to the marks. A question worth twice as many marks deserves about twice as much time.
- Don't spend too long on one question. If we get stuck, move on and come back to it.
- The number of lines for each question gives an idea of how long the answer should be.
- If we run out of space, use the additional pages at the back of the question and response book, and write the question number we're answering.

### Answering questions

- Look at the cognitive verb in each question. *Identify* needs a short answer, *explain* needs reasons, and *develop* or *symbolise* needs a complete diagram, table or code.
- Answer every part of the question. If a question asks three things about each item, give all three for every item.
- Refer to the stimulus. Use the exact table and field names from the stimulus in SQL queries and diagrams.
- Follow the conventions for each diagram, such as the DFD symbols, ERD cardinality and the primary and foreign keys.
- Write SQL clearly, with each clause on a new line, so the marker can follow our logic.

:::{hint} Practise writing SQL by hand
:class: dropdown
In the exam we write SQL on paper, with no computer to check it. Practise writing queries by hand, then check them in DB Browser for SQLite. Pay attention to the details that are easy to get wrong without a computer, such as commas between field names, quotes around text values and the `ON` clause in joins.
:::

## Practice

:::{seealso} Practice Scenario
:class: dropdown
A school canteen wants to digitise its lunch ordering system. Students will place orders online. The system checks if items are in stock, records payment, and sends the confirmed order to the kitchen. At pickup time, the kitchen marks the order as completed.

**Question 1**

Create a Level 0 data flow diagram that represents the scenario.

**Question 2**

Create an entity relationship diagram that represents the scenario.

**Question 3**

Using your ERD from Question 2, write SQL queries to meet the following requirements.

1. List all menu items that have a stock quantity less than 10.
2. Display all orders placed by a specific student, including the order date and total cost.
3. Update the stock quantity of an item after a student purchase is made.
4. Find the total number of completed orders prepared by the kitchen today.
5. Retrieve the names and prices of all items ordered but not yet marked as completed.
:::

### Practice Exam 1

- [Practice Exam 1](./assets/fia4/FIA4_Practice_Exam_1.docx)
- [Practice Exam 1 Marking Schema](./assets/fia4/FIA4_Practice_Exam_1_Marking_Schema.docx)

### Practice Exam 2

- [Practice Exam 2](./assets/fia4/FIA4_Practice_Exam_2.docx)
- [Practice Exam 2 Marking Schema](./assets/fia4/FIA4_Practice_Exam_2_Marking_Schema.docx)
