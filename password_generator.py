import random
import string


# -----------------------------
# RULE FUNCTIONS
# -----------------------------
# These are higher-order rule functions.
# Each rule checks if a password satisfies a condition.

def rule_has_upper(password):
    return any(char.isupper() for char in password)

def rule_has_lower(password):
    return any(char.islower() for char in password)

def rule_has_digit(password):
    return any(char.isdigit() for char in password)

def rule_has_symbol(password):
    return any(char in string.punctuation for char in password)


def validate_password(password, rules):
    """
    Check password against a list of rule functions.
    """
    return all(rule(password) for rule in rules)


# -----------------------------
# PASSWORD GENERATION
# -----------------------------

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """
    Generate password until it satisfies all selected rules.
    """

    characters = ""
    rules = []

    if use_upper:
        characters += string.ascii_uppercase
        rules.append(rule_has_upper)

    if use_lower:
        characters += string.ascii_lowercase
        rules.append(rule_has_lower)

    if use_digits:
        characters += string.digits
        rules.append(rule_has_digit)

    if use_symbols:
        characters += string.punctuation
        rules.append(rule_has_symbol)

    if characters == "":
        return None

    while True:
        password = "".join(random.choice(characters) for _ in range(length))

        if validate_password(password, rules):
            return password


# -----------------------------
# USER INPUT
# -----------------------------

def get_user_preferences():
    """
    Collect user preferences for password generation.
    """

    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length <= 0:
                print("Password length must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    return length, use_upper, use_lower, use_digits, use_symbols


# -----------------------------
# SAVE USERNAME + PASSWORD
# -----------------------------

def save_credentials(username, password):
    """
    Save username and password to a file.
    """

    with open("saved_passwords.txt", "a") as file:
        file.write(f"{username} : {password}\n")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():

    while True:

        print("\n=== Password Generator ===")
        print("1. Generate password")
        print("2. Generate and save username/password")
        print("3. Quit")

        choice = input("Select option: ")

        if choice == "1":

            length, use_upper, use_lower, use_digits, use_symbols = get_user_preferences()

            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

            if password is None:
                print("Error: Must select at least one character type.")
            else:
                print("Generated Password:", password)

        elif choice == "2":

            username = input("Enter username: ")

            length, use_upper, use_lower, use_digits, use_symbols = get_user_preferences()

            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

            if password is None:
                print("Error: Must select at least one character type.")
            else:
                save_credentials(username, password)
                print("Username and password saved.")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()