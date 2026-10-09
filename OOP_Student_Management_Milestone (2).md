# AI Backend Engineering Journey --- OOP Milestone

**Milestone:** Python OOP Practice --- Student Management System\
**Project status:** Completed\
**Language:** Python\
**Repository:** `Ai_Backend_Engineering_Journey`

------------------------------------------------------------------------

## 1. Milestone Summary

I practiced Python Object-Oriented Programming (OOP) by building a small
Student Management System. The project stores student information,
displays student details, checks pass/fail status, assigns a simple
grade label, and updates marks.

This milestone helped me practice writing a class, creating multiple
objects, using instance attributes, defining methods, and applying
conditional statements.

## 2. What I Learned

-   **Class:** Created a `Student` class as a blueprint for student
    objects.
-   **Object:** Created separate objects for Sujan, Kamal, and Rahim.
-   **Constructor (`__init__`):** Initialized each student's name, roll
    number, and marks.
-   **`self`:** Accessed the current object's attributes and methods.
-   **Instance variables:** Used `self.name`, `self.roll`, and
    `self.marks` to store each student's own data.
-   **Methods:** Created methods to display information, determine a
    grade, update marks, and check pass/fail status.
-   **Conditional statements:** Used `if`, `elif`, and `else` to make
    decisions based on marks.
-   **Updating object data:** Changed Sujan's marks from 85 to 90 using
    a method.
-   **Multiple objects:** Used one class to create multiple students
    with independent data.
-   **Code organization:** Used clear method names and printed section
    headings to make output easier to read.

## 3. Project Features

1.  Store student name, roll number, and marks.
2.  Display a student's information.
3.  Show a grade label based on marks.
4.  Check whether a student passes or fails.
5.  Update a student's marks.
6.  Manage multiple students independently.

## 4. Grade and Result Rules

### Grade label (`show_grade`)

          Marks Output
  ------------- -----------
    80 or above Excellent
         33--79 Pass
       Below 33 Fail

### Pass/fail (`show_result`)

          Marks Result
  ------------- --------
    33 or above Pass
       Below 33 Fail

**Note:** These are practice rules for this project, not an official
grading system. `show_grade()` and `show_result()` overlap for some
marks; they are kept separate because both methods were practiced.

## 5. Complete Project Code

Save the following code as **`student_management.py`**.

``` python
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def show_info(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)

    def show_grade(self):
        if self.marks >= 80:
            print("Excellent")
        elif self.marks >= 33:
            print("Pass")
        else:
            print("Fail")

    def update_marks(self, marks):
        self.marks = marks

    def show_result(self):
        if self.marks >= 33:
            print("Pass")
        else:
            print("Fail")


# Create student objects
student1 = Student("Sujan", 10, 85)
student2 = Student("Kamal", 6, 65)
student3 = Student("Rahim", 11, 25)


# Display Student 1
print("--- Student 1 ---")
student1.show_info()
student1.show_result()
student1.show_grade()

# Display Student 2
print("\n--- Student 2 ---")
student2.show_info()
student2.show_result()
student2.show_grade()

# Display Student 3
print("\n--- Student 3 ---")
student3.show_info()
student3.show_result()
student3.show_grade()


# Update Sujan's marks
print("\n--- After Updating Sujan's Marks ---")
student1.update_marks(90)
student1.show_info()
student1.show_grade()
```

## 6. How to Run

Open a terminal in the folder where `student_management.py` is saved,
then run:

``` bash
python student_management.py
```

If your system uses the `py` launcher, you can also try:

``` bash
py student_management.py
```

## 7. Expected Output

``` text
--- Student 1 ---
Name: Sujan
Roll: 10
Marks: 85
Pass
Excellent

--- Student 2 ---
Name: Kamal
Roll: 6
Marks: 65
Pass
Pass

--- Student 3 ---
Name: Rahim
Roll: 11
Marks: 25
Fail
Fail

--- After Updating Sujan's Marks ---
Name: Sujan
Roll: 10
Marks: 90
Excellent
```

## 8. Suggested Folder Structure

Keep the project separate from your general notes:

``` text
Ai_Backend_Engineering_Journey/
├── README.md
└── Python/
    ├── notes.md
    ├── practice.py
    └── Projects/
        └── Student_Management_System/
            ├── README.md
            └── student_management.py
```

If your existing repository uses a different structure, keep it
consistent rather than moving files unnecessarily.

## 9. Completion Checklist

-   [x] Created a `Student` class.
-   [x] Used `__init__()` to initialize student data.
-   [x] Created multiple student objects.
-   [x] Displayed student information with `show_info()`.
-   [x] Used conditions to determine grade labels.
-   [x] Checked pass/fail status.
-   [x] Updated marks through `update_marks()`.
-   [x] Ran the program and checked its output.
-   [ ] Rebuild the project once without copying the code.
-   [ ] Upload the project files to GitHub.

## 10. What to Practice Next

Try these optional improvements one at a time:

1.  Ask the user to enter a student's name, roll, and marks using
    `input()`.
2.  Validate that marks are between 0 and 100.
3.  Add a method that returns the grade instead of printing it directly.
4.  Add a method to display all details in one place.
5.  Store students in a list and display them with a loop.

Do not add every feature at once. Practice one improvement, test it, and
then continue.

------------------------------------------------------------------------

**Milestone reflection:**\
I completed a beginner-level Python OOP project and practiced classes,
objects, constructors, `self`, instance variables, methods, conditional
logic, and updating object data. My next goal is to recreate this
project independently and continue with the remaining Python syllabus
before starting a dedicated revision phase.
