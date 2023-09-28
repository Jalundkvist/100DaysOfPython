from tkinter import *

LABELS = ["Website", "Username", "Password"]

        
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Root window
root = Tk()
root.title("pw manager")
root.config(pady=20, padx=20)


# Logo
logo = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_img)
logo.grid(column=1, row=0)

# Entries
entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2)
entry_username = Entry()
entry_username.grid(column=1, row=2, columnspan=2)
entry_password = Entry()
entry_password.grid(column=1, row=3)
# Buttons
button_generate = Button(text="Generate password")
button_generate.grid(column=2, row=3)

# Labels
# Create labels for each name and place them in column 0 with increasing row numbers
for i, name in enumerate(LABELS, start=1):
    label = Label(root, text=name)
    label.grid(row=i, column=0, sticky="w")



root.mainloop()
