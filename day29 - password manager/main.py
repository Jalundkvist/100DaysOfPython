from tkinter import *
from tkinter import messagebox
import random

LABELS = ["Website:", "Username:", "Password:"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, END)
    password = []
    no_letters, no_numbers, no_symbols = [random.randint(4, 10) for _ in range(3)]
    password += [random.choice(letters) for _ in range(no_letters)]
    password += [random.choice(numbers) for _ in range(no_numbers)]
    password += [random.choice(symbols) for _ in range(no_symbols)]
    print(password)
    random.shuffle(password)
    password = ''.join(password)
    entry_password.insert(index=0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    data = [entry_website.get(), entry_username.get(), entry_password.get()]
    for text in data:
        if len(text) == 0:
            messagebox.showinfo(title="Big yikes", message="Dont leave any of the fields empty.")
            return

    is_ok = messagebox.askokcancel(title=data[0], message=f"These are the details entered: \nEmail: {data[1]} "
                                                          f"\nPassword: {data[2]} \nIs it ok to save?")
    if is_ok:
        write_to_file(data, "data.txt")
        entry_website.delete(0, END)
        entry_password.delete(0, END)


def write_to_file(data, data_file="textfile.txt"):
    with open(data_file, "a") as file:
        file.write("------------------------\n")
        for index, label_name in enumerate(LABELS):
            file.write(f"{label_name} {data[index]}\n")


# ---------------------------- UI SETUP ------------------------------- #
# Root window
root = Tk()
root.title("pw manager")
root.config(pady=25, padx=25)

# Logo
logo = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
logo.create_image(70, 100, image=logo_img)
logo.grid(column=1, row=0, columnspan=2)

# Labels
# Create labels for each name and place them in column 0 with increasing row numbers
for i, name in enumerate(LABELS, start=1):
    label = Label(root, text=name)
    label.grid(column=0, row=i, sticky="w")

# Entries
entry_website = Entry(width=52)
entry_website.grid(column=1, row=1, columnspan=2, sticky="w")

entry_username = Entry(width=52)
entry_username.grid(column=1, row=2, columnspan=2, sticky="w")

entry_password = Entry(width=33)
entry_password.grid(column=1, row=3, columnspan=1, sticky="w")

# Buttons
button_generate = Button(text="Generate password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=53, command=save_password)
button_add.grid(column=0, row=4, columnspan=3)

root.mainloop()
