# Tulip Library - Python GUI Application
# Freelance project for a small local library management system
# Developer: Hafsa Eldakrory
# Description:
# A desktop application built using Python (Tkinter & Pillow)
# to manage library memberships, book categories, and generate invoices dynamically.

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import font
from PIL import ImageTk, Image

# ---------------- Main Interface ----------------
interface1 = Tk()
interface1.title("Tulip Library")
interface1.geometry('1100x990')
interface1.config(background="#466884")

# Title
interface1_welcome = Label(interface1, text="Tulip Library",
                            fg="#fff4c6", background="#466884",
                            font=('Gill Sans', 25))
interface1_welcome.place(x=150, y=55)

# Logo
try:
    logoLibrary = Image.open("logolibrary.png")
    new_size = logoLibrary.resize((130, 130))
    image = ImageTk.PhotoImage(new_size)
    logoLibrary_label = Label(master=interface1, image=image)
    logoLibrary_label.place(x=500, y=40)
except:
    pass  # Skip logo if not found

# Introduction
introLabel = Label(interface1,
                   text="Tulip Library is a modern library system that offers a wide selection of books "
                        "and personalized services for its members.",
                   background="#466884", fg="#fff4c6", font=('Times New Roman', 20))
introLabel.place(x=50, y=250)

# ---------------- User Info Section ----------------
def create_entry(label_text, x, y):
    label = Label(interface1, text=label_text,
                  background="#466884", fg="#fff4c6",
                  font=('Times New Roman', 20))
    label.place(x=x, y=y)
    entry = Entry(interface1, width=20, font=('Times New Roman', 20))
    entry.place(x=x + 130, y=y)
    return entry

enteryName = create_entry("Full Name", 80, 400)
enteryPassword = create_entry("Password", 520, 400)
enteryAge = create_entry("Age", 80, 470)
enteryMembership = create_entry("Membership (yes/no)", 520, 470)

# ---------------- Gallery Page ----------------
def goGallery():
    interface2 = Toplevel(interface1)
    interface2.title("Gallery")
    interface2.geometry('1050x930')
    interface2.config(background="#f9f9f9")

    Label(interface2, text="Gallery:",
          fg="#466884", font=('Gill Sans', 30)).place(x=60, y=60)
    Label(interface2, text="Please choose your favourite category:",
          font=('Times New Roman', 22)).place(x=60, y=120)

    options = ["Historical", "Crimes"]
    combo_font = font.Font(size=20, weight="bold")
    combo = Combobox(interface2, values=options, width=20, font=combo_font)
    combo.place(x=60, y=200)

    def show_books(eve):
        option = combo.get()
        Label(interface2, text="Available Books:",
              font=('Times New Roman', 22, 'bold')).place(x=60, y=300)
        if option == "Historical":
            books = ["The Essential Rumi", "The Muqaddimah", "No God But God"]
        else:
            books = ["In Cold Blood", "Murder on the Express", "The Silence of the Lambs"]

        x = 60
        for book in books:
            Label(interface2, text=f"• {book}", font=('Times New Roman', 20)).place(x=x, y=350)
            x += 280

    combo.bind("<<ComboboxSelected>>", show_books)

    # Book & Student Entries
    Label(interface2, text="Book Name:", font=('Times New Roman', 22)).place(x=60, y=520)
    bookNameEntry = Entry(interface2, width=15, font=('Times New Roman', 22))
    bookNameEntry.place(x=300, y=520)

    Label(interface2, text="Are you a student?", font=('Times New Roman', 22)).place(x=60, y=620)
    areStudentEntry = Entry(interface2, width=15, font=('Times New Roman', 22))
    areStudentEntry.place(x=300, y=620)

    # ---------------- Invoice Page ----------------
    def invoiceFunction():
        interface3 = Toplevel(interface2)
        interface3.title("Invoice")
        interface3.geometry('800x930')
        interface3.config(background="#f7f7f7")

        Label(interface3, text="Invoice",
              fg="#466884", font=('Gill Sans', 30)).place(x=60, y=60)
        Label(interface3, text=f"Name: {enteryName.get()}",
              font=('Times New Roman', 22)).place(x=60, y=160)
        Label(interface3, text=f"Age: {enteryAge.get()}",
              font=('Times New Roman', 22)).place(x=60, y=260)

        # Calculate price based on category & discounts
        class Calculation:
            def calcPrice(self):
                option = combo.get()
                member = enteryMembership.get().lower()
                student = areStudentEntry.get().lower()
                price = 50 if option == "Historical" else 40

                if member == "yes" and student == "yes":
                    return round(price * 0.9, 2)
                return price

        total_price = Calculation().calcPrice()
        Label(interface3, text=f"Book Name: {bookNameEntry.get()}",
              font=('Times New Roman', 22)).place(x=60, y=360)
        Label(interface3, text=f"Total Price: {total_price} SR",
              font=('Times New Roman', 22)).place(x=60, y=460)

        Label(interface3, text="Thank you for choosing Tulip Library!\n"
                               "We hope you enjoy your reading experience.",
              font=('Times New Roman', 20), justify=LEFT).place(x=60, y=550)

        Button(interface3, text="Close", font=('Times New Roman', 15),
               command=interface3.destroy).place(x=100, y=720)

    Button(interface2, text="Generate Invoice",
           command=invoiceFunction, font=('Times New Roman', 15)).place(x=200, y=700)

# ---------------- Main Buttons ----------------
Button(interface1, text="Go to Gallery", font=('Times New Roman', 15),
       padx=1, pady=3, command=goGallery).place(x=210, y=540)

interface1.mainloop()
