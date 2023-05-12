from tkinter import *
import os
from tkinter import messagebox
from password_generator import generate_password
from pyperclip import copy

main_dir = os.path.dirname(__file__)

if __name__ == '__main__':
    window = Tk()
    window.config(padx=20, pady=20)
    window.title("Pușcaș Password Manager")
    logo = PhotoImage(file=main_dir + "./logo.png")
    icon = PhotoImage(file=main_dir + "./icon.png")
    window.iconphoto(False, icon)

    def fill_password():
        new_password = generate_password()
        password_input.delete(0, END)
        password_input.insert(0, new_password)
        copy(new_password)

    def save_credentials():
        website = website_input.get()
        username = username_input.get()
        password = password_input.get()

        if website == "" or password == "":
            messagebox.showinfo(title="Error", message="All fields are required!")
            response = False
        else:
            response = messagebox.askokcancel(title="Confirm credentials",
                                              message=f"Website: {website}\nEmail/Username: {username}"
                                                      f"\nPassword: {password}")

        if response:
            with open(main_dir + "./passwords.txt", mode="a") as file:
                file.writelines(f"Website: {website} | Email/Username: {username}"
                                f" | Password: {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


    canvas = Canvas(width=200, height=200)
    canvas.create_image(100, 100, image=logo)
    canvas.grid(column=1, row=0)

    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)

    website_input = Entry(width=35)
    website_input.grid(column=1, row=1, columnspan=2)
    website_input.focus()

    username_label = Label(text="Email/Username:")
    username_label.grid(column=0, row=2)

    username_input = Entry(width=35)
    username_input.grid(column=1, row=2, columnspan=2)
    username_input.insert(0, "username@your.domain")

    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3)

    password_input = Entry(width=21, show="*")
    password_input.grid(column=1, row=3)

    password_generate = Button(text="Generate", height=1, command=fill_password)
    password_generate.grid(column=2, row=3, padx=(0, 30))

    add_credentials = Button(text="Add Credentials", width=36, command=save_credentials)
    add_credentials.grid(column=0, row=4, columnspan=3)

    window.mainloop()
