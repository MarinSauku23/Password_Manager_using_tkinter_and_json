import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- SEARCH DATA ------------------------------- #


def find_password():
    website_info = website_entry.get()
    email_username_info = email_username_entry.get()
    password_info = password_entry.get()
    new_data = {website_info: {
        "email": email_username_info,
        "password": password_info
    }
    }

    try:
        with open("data.json", "r") as info_file:
            data = json.load(info_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
        with open("data.json", "w") as info_file:
            json.dump(new_data, info_file, indent=4)
    else:
        if website_info in data:
            messagebox.showinfo(title=website_info, message=f"Email: {data[website_info]['email']}\n"
                                                                f"Password: {data[website_info]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               '-', '_', '=', '+', '[', ']', '{', '}', '|',
               ';', ':', "'", '"', ',', '.', '/', '<', '>', '?', '`', '~']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]

    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_information():
    website_info = website_entry.get()
    email_username_info = email_username_entry.get()
    password_info = password_entry.get()
    new_data = {website_info: {
        "email": email_username_info,
        "password": password_info
    }}

    if len(website_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_info, message=f"These are the details entered:\n"
                                                           f"Email: {email_username_info}\n"
                                                           f"Password: {password_info}\n"
                                                           f"Is it ok to save?")

        try:
            with open("data.json", "r") as info_file:
                data = json.load(info_file)
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json", "w") as info_file:
                json.dump(new_data, info_file, indent=4)

        else:
            with open("data.json", "w") as info_file:
                json.dump(data, info_file, indent=4)

        finally:
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
my_pass_image = PhotoImage(file="logo.png")
canvas.create_image(80, 100, image=my_pass_image)
canvas.grid(column=1, row=0)

#"Website" Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e")

#"Email/Username" Label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2, sticky="e")

#"Password" Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e")

#Website Frame
website_search_frame = Frame(window)
website_search_frame.grid(column=1, columnspan=2, row=1, sticky="w")

#Website Entry
website_entry = Entry(website_search_frame, width=22)
website_entry.pack(side=LEFT)
website_entry.focus()

#"Search" button
search_button = Button(website_search_frame, text="Search", width=10, command=find_password)
search_button.pack(side=LEFT, padx=(0, 0))

#"Email/Username" Entry
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, columnspan=2, row=2, sticky="w")
email_username_entry.insert(0, "pini.sauku@gmail.com")

#Password Frame
password_frame = Frame(window)
password_frame.grid(column=1, row=3, columnspan=2, sticky="w")

#"Password" Entry
password_entry = Entry(password_frame, width=17)
password_entry.pack(side=LEFT)

#"Generate Password" button
generate_password = Button(password_frame, text="Generate Password", command=generate_password)
generate_password.pack(side=LEFT, padx=(0, 0))

#"Add" button
add_button = Button(text="Add", width=30, command=save_information)
add_button.grid(column=1, columnspan=2, row=4)





window.mainloop()