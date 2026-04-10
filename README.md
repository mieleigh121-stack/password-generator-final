# Password Generator – CMPS 1100 Midterm

## Description
This project is a terminal-based password generator written in Python. Users can generate passwords of a chosen length and select which character types to include (uppercase, lowercase, digits, and symbols).

The program also allows users to save usernames and generated passwords to a file.

## Features
- Generate passwords with customizable length
- Choose character types
- Enforce password rules using higher-order functions
- Regenerate passwords until rules are satisfied
- Save usernames and passwords to a file

## Higher-Order Functions
Password rules are implemented as functions (ex: must contain uppercase). These rule functions are stored in a list and checked using:
all(rule(password)for rule in rules)

This makes the system flexible and allows new rules to be added easily.

## Security Note
This project is for educational purposes only and is not fully secure.

- It uses Python’s `random` module which is not cryptographically secure.
- Saved passwords are stored in plain text.

## How to Run
python password_generator.py

## Run Tests
python-m unittest test_password_generator.py