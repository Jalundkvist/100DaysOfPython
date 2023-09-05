from tkinter import *

LABEL_FONT = ("Arial", 16, "normal")


def create_label(text: str, row: int, column: int, pad_x=(0, 0), pad_y=(0, 0)):
    """
    Creates a label from the tkinter package.
    :param text: labels text
    :param row: Relative X-position
    :param column: Relative Y-position
    :param pad_x: padding around label
    :param pad_y: padding around label
    :return: tkinter label
    """
    new_label = Label(text=text, font=LABEL_FONT)
    new_label.grid(row=row, column=column, padx=pad_x, pady=pad_y)
    return new_label


def compute(output_label: Label, entry_input: Entry):
    """
    Converts miles to Km with tkinter label and entry
    :param output_label: label to update with value
    :param entry_input: entry for miles
    :return: N/A
    """
    try:
        output_label.config(text=(str(float(entry_input.get())*1.609)))
    except ValueError as err:
        output_label.config(text='Not a number')


def main():
    # Create Tk window
    window = Tk()
    window.title("Miles to Kilometer Converter")
    window.config(padx=20, pady=25)

    # Create all labels
    label_equals = create_label('equals', 1, 0)
    label_miles = create_label('Miles', 0, 2)
    label_km = create_label('Km', 1, 2)
    label_result = create_label('0', 1, 1)

    # create entry for input
    input_value = Entry(width=10)
    input_value.insert(END, string='Enter miles')
    input_value.grid(row=0, column=1)

    # create button
    button_calculate = Button(text='Calculate', command=lambda: compute(label_result, input_value))
    button_calculate.grid(row=2, column=1)

    # tk mainloop
    window.mainloop()


if __name__ == '__main__':
    main()
