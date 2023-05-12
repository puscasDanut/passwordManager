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
    canvas.grid(column=1, row=1)

    window.mainloop()
