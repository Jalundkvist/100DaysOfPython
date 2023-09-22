from tkinter import *
from time import sleep
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = '✅'

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_start():
    countdown(5)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    canvas.itemconfig(label_timer, text=count)
    #global remaining_seconds
    if remaining_seconds > 0:
        mm, ss = divmod(remaining_seconds, 60)
        timer_label.config(text=f"Time remaining: {mm:02d}:{ss:02d}")
        remaining_seconds -= 1
        root.after(1000, update_timer)  # Call update_timer after 1000 milliseconds (1 second)
    else:
        timer_label.config(text="Time's up!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=canvas_tomato)
label_timer = canvas.create_text(100, 122, text='00:00', font=('Arial', '26', 'bold'), fill='white')
canvas.grid(column=1, row=1)

label_title = Label(text='Timer', font=('Arial', '30', 'bold'), highlightthickness=0)
label_title.config(bg=YELLOW, fg=GREEN)
label_title.grid(column=1, row=0)

label_checkbox = Label(text='', font=('Arial', '20', 'bold'), highlightthickness=0)
label_checkbox.config(bg=YELLOW, fg=GREEN)
label_checkbox.grid(column=1, row=4)

button_start = Button(text='Start', command=timer_start, highlightthickness=0)
button_start.grid(column=0, row=3)

button_reset = Button(text='Reset', command=timer_reset, highlightthickness=0)
button_reset.grid(column=3, row=3)


window.mainloop()
