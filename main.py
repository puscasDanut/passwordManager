from tkinter import *
import os

main_dir = os.path.dirname(__file__)

if __name__ == '__main__':

    window = Tk()
    window.config(padx=20, pady=20)
    window.title("Pușcaș Password Manager")
    logo = PhotoImage(file=main_dir+"./logo.png")
    icon = PhotoImage(file=main_dir+"./icon.png")
    window.iconphoto(False, icon)

    canvas = Canvas(width=200, height=200)
    canvas.create_image(100, 100, image=logo)
    canvas.grid(column=1, row=0)

    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)

    website_input = Entry(width=35)
    website_input.grid(column=1, row=1, columnspan=2)

    username_label = Label(text="Email/Username:")
    username_label.grid(column=0, row=2)

    username_input = Entry(width=35)
    username_input.grid(column=1, row=2, columnspan=2)

    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3)

    password_input = Entry(width=21)
    password_input.grid(column=1, row=3)

    password_generate = Button(text="Generate", height=1)
    password_generate.grid(column=2, row=3, padx=(0, 30))

    add_credentials = Button(text="click", width=36)
    add_credentials.grid(column=0, row=4, columnspan=3)


    window.mainloop()
