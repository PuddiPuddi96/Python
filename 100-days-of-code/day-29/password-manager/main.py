from pyperclip import copy
from random import choice, randint, shuffle
from tkinter import Button, Canvas, END, Entry, Label, messagebox, PhotoImage, Tk

# ---------------------------- CONSTANTS ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- UTILS ------------------------------- #
def check_input():
    website = entry_website.get()
    username = entry_email_username.get()
    password = entry_password.get()

    if website is None or not website or username is None or not username or password is None or not password:
        messagebox.showinfo(title="OPS", message="Please make sure you haven't left any fields empty.")
        return False
    return True

def clear_form():
    entry_website.delete(0, END)
    entry_password.delete(0, END)

    entry_website.focus()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = []

    password_list.extend([choice(LETTERS) for _ in range(randint(10, 15))])
    password_list.extend([choice(SYMBOLS) for _ in range(randint(5, 10))])
    password_list.extend([choice(NUMBERS) for _ in range(randint(5, 10))])

    shuffle(password_list)
    password = ''.join(password_list)

    entry_password.insert(0, password)

    copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if not check_input():
        return
    
    website = entry_website.get()
    username = entry_email_username.get()
    password = entry_password.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")

    if not is_ok:
        return
    
    with open(file="./output/data.txt", mode="a") as password_file:
        password_file.write(f"{website} | {username} | {password}\n")
    clear_form()
        
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./asset/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)

entry_email_username = Entry(width=35)
entry_email_username.grid(row=2, column=1, columnspan=2)
entry_email_username.insert(0, "d.b.strianese96@hotmail.com")

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
