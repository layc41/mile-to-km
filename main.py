from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def converter():
    num_of_km = 1.609344 * float(input.get())
    value_in_km.config(text=f"{num_of_km}")


# Labels
miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

value_in_km = Label(text="0")
value_in_km.grid(column=1, row=1)

# Entry
input = Entry()
input.grid(column=1, row=0)

# Button
calculate_btn = Button(text="Calculate", command=converter)
calculate_btn.grid(column=1, row=2)






window.mainloop()