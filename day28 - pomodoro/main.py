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
reps = 0
rest_counter = 0
timer = None


def bring_to_front():
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)


def timer_reset():
    # Timer mechanism to reset the timer
    global reps, rest_counter
    window.after_cancel(timer)
    label_title.config(text='Timer', fg=GREEN)
    canvas.itemconfig(label_timer, text=f"00:00")
    label_checkbox.config(text='')
    rest_counter, reps = 0, 0


def timer_start():
    # Timer mechanism to start the timer
    global reps, rest_counter
    reps += 1
    bring_to_front()
    if reps > 8:
        timer_reset()
    elif reps == 8:
        label_title.config(text='Long break!', fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        rest_counter += 1
        label_checkbox.config(text=CHECKMARK * rest_counter)
        label_title.config(text='Short break!', fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        label_title.config(text='Work!', fg=GREEN)


def countdown(seconds):
    """ Countdown mechanism for the timer """
    global timer
    mm, ss = divmod(seconds, 60)
    canvas.itemconfig(label_timer, text=f"{mm:02d}:{ss:02d}")
    if seconds > 0:
        timer = window.after(1000, countdown, seconds-1)  # Call update_timer after 1000 milliseconds (1 second)
    else:
        timer_start()


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
