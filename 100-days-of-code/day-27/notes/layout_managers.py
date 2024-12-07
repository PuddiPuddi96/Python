from tkinter import *

def button_clicked():
    print("i got clicked")
    my_label.config(text=input.get())


window = Tk()
window.title("My firt GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #Padding for entire window

#Label
my_label = Label(text="I am a lable", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.place(x=0, y=0) #(0,0) top left
my_label.grid(column=0, row=0) #Top left
my_label.config(padx=50, pady=50) #Padding for label

#Button
button_1 = Button(text="Click me", command=button_clicked)
button_1.grid(column=1, row=1)

button_2 = Button(text="Click me 2", command=button_clicked)
button_2.grid(column=2, row=0)

#Entry
entry = Entry()
print(entry.get())
entry.grid(column=3, row=2)

window.mainloop()
