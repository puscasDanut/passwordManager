from tkinter import *
import os
from tkinter import messagebox
from password_generator import generate_password
from pyperclip import copy
import json

main_dir = os.path.dirname(__file__)

if __name__ == '__main__':
    window = Tk()
    window.config(padx=20, pady=20)
    window.title("Pușcaș Password Manager")
    logo = PhotoImage(file=main_dir + "./logo.png")
    icon = PhotoImage(file=main_dir + "./icon.png")
    window.iconphoto(False, icon)

    def find_credentials():
        website = website_input.get().title()
        try:
            with open(main_dir + "./passwords.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="You didn't register any passwords!")
        else:
            password_available = False
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=f"Credentials for {website}", message=f"Username/Email: {email}"
                                                                                f"\nPassword: {password}")
                password_available = True
            if not password_available:
                messagebox.showinfo(title="Password not available", message=f"You didn't register any credentials for {website}")

    def write_password(data):
        with open(main_dir + "./passwords.json", mode="w") as file:
            json.dump(data, file, indent=4)

    def fill_password():
        new_password = generate_password()
        password_input.delete(0, END)
        password_input.insert(0, new_password)
        copy(new_password)

    def save_credentials():
        website = website_input.get().title()
        username = username_input.get()
        password = password_input.get()
        new_data = {
            website: {
                "email": username,
                "password": password,
            }
        }

        if website == "" or password == "":
            messagebox.showinfo(title="Error", message="All fields are required!")
        else:
            try:
                with open(main_dir + "./passwords.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                write_password(new_data)
            else:
                data.update(new_data)
                write_password(data)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


    canvas = Canvas(width=200, height=200)
    canvas.create_image(100, 100, image=logo)
    canvas.grid(column=1, row=0)

    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)

    website_input = Entry(width=30)
    website_input.grid(column=1, row=1)
    website_input.focus()

    search_button = Button(text="Search", command=find_credentials)
    search_button.grid(column=2, row=1, padx=(0, 60))

    username_label = Label(text="Email/Username:")
    username_label.grid(column=0, row=2)

    username_input = Entry(width=35)
    username_input.grid(column=1, row=2, columnspan=2, padx=(0, 85))
    username_input.insert(0, "username@your.domain")

    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3)

    password_input = Entry(width=30, show="*")
    password_input.grid(column=1, row=3)

    password_generate = Button(text="Generate", height=1, command=fill_password)
    password_generate.grid(column=2, row=3, padx=(0, 60))

    add_credentials = Button(text="Add Credentials", width=36, command=save_credentials)
    add_credentials.grid(column=0, row=4, columnspan=3)

    window.mainloop()
