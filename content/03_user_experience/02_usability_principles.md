# Usability

:::{dropdown} Learning Goals
By the end of this section you will:
- Understand why useability is important
- Understand  
:::

> Usability is a measure of how well a specific user in a specific context can use a product/design to achieve a defined goal effectively, efficiently and satisfactorily. Designers usually measure a design's usability throughout the development process — from wireframes to the final deliverable. {cite}`interactiondesignfoundation_2014_what`

A design's usability depends on how well its features accommodate users' needs and contexts. It is important because it makes digital solutions easy, efficient, safe and satisfying for users to learn and use, improving user experience and ensuring the solution meets user needs.

In Digital Solutions we will focus on five usability principles (use the mnemonic **usale**):

- utility
- safety
- accessibility
- learnability
- effectiveness

## Utility

Utility is about whether the digital solution includes all the features users need to complete their tasks. It doesn’t matter how easy something is to use if it doesn’t do what the user actually needs.

Utility depends on user needs and the purpose of the solution.

Consider the following when evaluating utility:

- **Relevance**: Include all and only the features that meet user needs.
- **Completeness**: Make sure users can complete their tasks without needing other tools or workarounds.
- **Availability**: Ensure the necessary features are available at the right time.
- **Appropriateness**: Features should suit the task and context the user is working in.

**Example of Utility in a Digital Solution:**

A school app lets students check their timetable, but it doesn’t include a way to view assessment due dates. Even if the app is easy to use, it fails the utility principle because it lacks a key function students need to manage their workload. To improve utility, the app should include an assessment calendar or integration with task reminders.

## Safety

Safety means designing digital solutions that help prevent serious user errors and allow easy recovery if something goes wrong. It protects users from losing data, making dangerous choices, or damaging the system.

When evaluating safety, consider:

- How many errors do users make?
- How serious are those errors?
- How easily can users recover?

Examples of designing for safety:

- Not placing the **delete** button next to the **save** button.
- Allowing users to undo actions (e.g. **Ctrl+Z** in word processors).
- Using combo boxes or radio buttons to limit risky input.
- Making text fields wide enough to clearly show the whole entry.

It's best to prevent errors before they happen. Every interface is different, so safety features should match the specific risks of that solution.

Focus on these four areas:

- **Error Prevention**: Design interfaces that reduce the chance of mistakes.
- **Error Recovery**: Make it easy for users to fix errors (e.g. undo, cancel).
- **Warning Systems**: Alert users before they make irreversible or risky changes.
- **Well-being**: Avoid causing stress, frustration, or physical strain.

**Example of Safety in a Digital Solution:**

An online form asks users to upload documents. The **submit** and **clear all** buttons are placed side by side. A student accidentally clicks **clear all** and loses everything.

This fails the **error prevention** and **error recovery** principles.

To improve safety:

- Add a confirmation message before clearing all data.
- Move the **clear all** button away from **submit**.
- Allow users to recover deleted files or auto-save progress.

## Accessibility

Accessibility means making sure your digital solution can be used by as many people as possible, including people with diverse abilities, including those with visual, auditory, motor, and cognitive impairments.

We use the **POUR** principles to guide accessibility:

- **Perceivable**: Users must be able to see or hear the information. This includes things like captions for videos, readable fonts, or adjustable colour contrast. For this course, we will check font contrast using the [Colour Contrast Analyser (CCA)](https://www.tpgi.com/color-contrast-checker/).
- **Operable**: Users must be able to use all parts of the solution, even without a mouse. This means allowing keyboard navigation or voice commands.
- **Understandable**: Content and navigation should be easy to read and follow. Avoid confusing layouts or unclear instructions.
- **Robust**: The solution should work with different devices and assistive technologies (like screen readers), even as technology changes.

**Example of Accessibility in a Digital Solution:**

A university website uses a navigation menu that only works with a mouse hover. Students using keyboard navigation or screen readers can’t access these links. This fails the **Operable** principle. To improve accessibility, the site should allow keyboard tabbing through the menu and include clear focus indicators. In addition, if the site uses light grey text on a white background, it may fail the **Perceivable** principle. Using the Colour Contrast Analyser can help ensure text is readable for users with vision impairments.

## Learnability

Learnability is about how easy it is for a user to learn how to use your digital solution. A learnable interface feels familiar, matches user expectations, and helps new users become confident quickly.

Ask:

- Is the system intuitive?
- Does it follow patterns users already know?

**Strategies to improve learnability:**

- **Consistent Design**: Use similar layouts, colours, icons and labels across the whole interface.
- **Familiar Patterns**: Match user expectations (e.g. online shops should feel like shops, games should use arrow keys or WASD).
- **Clear Language**: Use simple words and avoid technical jargon.
- **Intuitive Navigation**: Menus and buttons should be clearly labelled and easy to find.
- **Helpful Feedback**: Give visual signals when something works (or doesn’t), like colour changes or messages.
- **Guided Help**: Use pop-ups, tooltips, or short tutorials to show users how to use new features.

**Example of Learnability in a Digital Solution:**

A new photo editing app uses unfamiliar icons and places the save button under a hidden menu. Users struggle to find basic tools and give up quickly.

This fails the **learnability** principle because the interface doesn't match common design patterns.

To improve learnability:

- Use familiar icons (e.g. floppy disk for save, scissors for crop)
- Place key tools in visible, consistent locations
- Include a short tutorial on first use to guide new users through the interface.

## Effectiveness

Effectiveness is about whether users can complete their tasks successfully using your digital solution.

A solution is effective when it:

- Works reliably every time
- Produces the correct output
- Helps users finish tasks without confusion or mistakes

Even if a system has all the right features (utility), it may still be ineffective if it’s unreliable or hard to use.

To improve effectiveness, focus on:

- Goal Achievement: Can users complete the task?
- Accuracy: Are there few or no errors?
- Efficiency: Is it done in a reasonable amount of time?
- Quality of Outcome: Does the output meet user expectations?

**Example of Effectiveness in a Digital Solution:**

A budgeting app includes all the right features—expense tracking, income input, and charting—but users report that the charts don’t update correctly and saved data sometimes disappears.

This fails the **effectiveness** principle because the system is unreliable, even though it has high utility.

To improve effectiveness:

- Fix bugs so data is saved and updated correctly
- Ensure outputs like graphs are accurate and update in real time
- Test that all features work consistently under normal use conditions

:::{seealso} Useability Activities
:class: dropdown
**Activity 1**

You are designing a *Homework Tracker App* for high school students. The app should help users:

- Add, view, and edit homework tasks
- Sort tasks by subject or due date
- Set reminders for upcoming deadlines
- Mark tasks as complete

Your team must evaluate the design to ensure it meets usability expectations for students aged 13–17, including those with accessibility needs.

Review the following issues. For each one:

- Identify the usability principle it relates to
- Suggest a specific improvement

Usability Issues:
1. The ‘Delete Task’ button is located directly next to the ‘Save’ button.
2. The app uses light grey text on a white background.
3. There is no help screen, onboarding, or tooltips for new users.
4. Users must type the subject name each time; no dropdown or autocomplete is provided.
5. The app crashes if a due date isn’t entered.
6. Reminders don’t always appear, especially if the app was recently closed.
7. The navigation icons are not labelled and use unfamiliar symbols.
8. There is no confirmation message when deleting a task.
9. Some buttons are too small to tap easily on mobile.
10. Completed tasks are deleted automatically with no option to review or restore them later.

---

**Activity 2**

Log into to Student Cafe and identify useability issues:

For each one:

- Identify the usability principle it relates to
- Suggest a specific improvement
:::
