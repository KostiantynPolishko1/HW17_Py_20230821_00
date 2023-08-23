from tkinter import *
from tkinter import ttk


def win_calc() -> None:

    def cost():
        price_profile = 1000  # nominal price depend of profile
        cost_str = ((int(entry_h.get()) * int(entry_w.get()))*(10**-6)) * price_profile
        label_cost['text'] = str(int(cost_str))

    print('\twindow_calculator')

    window = Tk()
    window.title('CALCULATOR of PLASTIC WINDOW')
    window.geometry('950x650')

    label_s = ttk.Label(text='size h x w')
    label_h = ttk.Label(text='height mm')
    label_w = ttk.Label(text='width mm')
    label_price = ttk.Label(text='price uah')
    label_cost = ttk.Label(text='0.0')
    label_s.grid(row=0, column=0)
    label_h.grid(row=1, column=1)
    label_w.grid(row=2, column=1)
    label_price.grid(row=3, column=1)
    label_cost.grid(row=3, column=2)

    entry_h = Entry(width=10)
    entry_w = Entry(width=10)
    entry_h.grid(row=1, column=2)
    entry_w.grid(row=2, column=2)

    btn_cost = ttk.Button(text='calculate cost', command=cost)
    btn_cost.grid(row=3, column=4)

    window.mainloop()
