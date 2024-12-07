from tkinter import Entry, Button, Label, Tk

FONT_LABEL = ("Arial", 16, "normal")

def converter():
    miles = float(miles_input.get())
    km = miles * 1.609
    output_label.config(text=f"{km}")

window = Tk()
window.minsize(height=300, width=500)
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT_LABEL, width=7)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=FONT_LABEL, width=9)
is_equal_label.grid(column=0, row=1)

output_label = Label(text="0", font=FONT_LABEL)
output_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT_LABEL)
km_label.grid(column=2, row=1)

button_calculate = Button(text="Calculate", command=converter, width=7)
button_calculate.grid(column=1, row=2)

window.mainloop()
