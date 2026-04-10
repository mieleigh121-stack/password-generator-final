import tkinter as tk
import random
import string


# -------- PASSWORD GENERATION --------
def generate_password():
    length = int(length_entry.get())

    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase
    if lower_var.get():
        characters += string.ascii_lowercase
    if digit_var.get():
        characters += string.digits
    if symbol_var.get():
        characters += string.punctuation

    if characters == "":
        result_label.config(text="Select at least one option!")
        return

    while True:
        password = "".join(random.choice(characters) for _ in range(length))

        # Ensure at least one of each selected type
        if (not upper_var.get() or any(c.isupper() for c in password)) and \
           (not lower_var.get() or any(c.islower() for c in password)) and \
           (not digit_var.get() or any(c.isdigit() for c in password)) and \
           (not symbol_var.get() or any(c in string.punctuation for c in password)):
            break

    result_label.config(text=password)


# -------- SAVE PASSWORD --------
def save_password():
    username = username_entry.get()
    password = result_label.cget("text")

    with open("saved_passwords.txt", "a") as file:
        file.write(f"{username} : {password}\n")

    result_label.config(text="Saved!")
def save_password():
    username = username_entry.get()
    password = result_label.cget("text")

    if username == "" or password == "":
        result_label.config(text="Enter username and generate password first!")
        return

    with open("saved_passwords.txt", "a") as file:
        file.write(f"Username: {username} | Password: {password}\n")

    result_label.config(text="Saved!")


def view_saved_passwords():
    try:
        with open("saved_passwords.txt", "r") as file:
            saved_data = file.read()
    except FileNotFoundError:
        saved_data = "No saved passwords found."

    saved_window = tk.Toplevel(window)
    saved_window.title("Saved Usernames & Passwords")
    saved_window.geometry("450x300")

    tk.Label(saved_window, text="Saved Usernames & Passwords", font=("Arial", 14)).pack(pady=10)

    text_box = tk.Text(saved_window, wrap="word", width=50, height=15)
    text_box.pack(pady=10)
    text_box.insert("1.0", saved_data)
    text_box.config(state="disabled")

# -------- GUI SETUP --------
window = tk.Tk()
window.title("Password Generator App")
window.geometry("350x400")

# Title
tk.Label(window, text="Password Generator", font=("Arial", 16)).pack(pady=10)

# Username
tk.Label(window, text="Username:").pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Length
tk.Label(window, text="Password Length:").pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Options
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(window, text="Uppercase", variable=upper_var).pack()
tk.Checkbutton(window, text="Lowercase", variable=lower_var).pack()
tk.Checkbutton(window, text="Digits", variable=digit_var).pack()
tk.Checkbutton(window, text="Symbols", variable=symbol_var).pack()

# Buttons
tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)
tk.Button(window, text="Save Username & Password", command=save_password).pack()
tk.Button(window, text="View Saved Passwords", command=view_saved_passwords).pack(pady=10)

# Result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
window.mainloop()