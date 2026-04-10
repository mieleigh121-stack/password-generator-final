# Midterm Process Report

Total Time Spent
Approximately 10–12 hours were spent designing, coding, debugging, and testing the password generator project.

Most Time-Consuming Part
The most time-consuming part was modifying the password generation logic to enforce rules such as requiring at least one character from each selected category while keeping the program organized and readable.

How Work Could Have Been More Efficient
We would say the development could have been more efficient by writing tests earlier and implementing features incrementally instead of modifying large sections of the code at once.

Libraries / Starter Code
The Python random and string libraries were essential for generating characters and building the password character pool. Starter code and LLM assistance were used to create the initial structure, but significant modifications were made including adding rule validation, password regeneration logic, saving credentials to a file, and implementing higher-order functions.

Testing
A unit test suite using Python’s unittest module was implemented to verify password length, digits-only generation, rule validation, and correct behavior when no character types are selected. All tests pass successfully.