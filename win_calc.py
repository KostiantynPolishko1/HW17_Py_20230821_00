from tkinter import *
from tkinter import ttk
from win_calc_function import *


def window_calculator(data: dict) -> None:
    def win_h_info(value: int, logic: bool) -> None:

        label_h_info.grid(row=1, column=3)

        if not logic:
            txt, color = 'not correct', '#ff0000'
            label_h_info.grid(row=1, column=4)
        elif logic and value == 0:
            txt, color = 'fill data', '#0048ff'
            label_h_info.grid(row=1, column=4)
        elif data['win_size']['h_min'] <= value <= data['win_size']['h_max']:
            txt, color = '', ''
        else:
            txt, color = 'min ' + str(data['win_size']['h_min']) if value < data['win_size']['h_min'] else 'max ' + str(data['win_size']['h_max']), '#0048ff'
            label_h_info.grid(row=1, column=4)

        label_h_error['text'] = txt
        label_h_error['foreground'] = color

    def win_w_info(value: int, logic: bool) -> None:

        label_w_info.grid(row=2, column=3)

        if not logic:
            txt, color = 'not correct', '#ff0000'
            label_w_info.grid(row=2, column=4)
        elif logic and value == 0:
            txt, color = 'fill data', '#0048ff'
            label_w_info.grid(row=2, column=4)
        elif data['win_size']['w_min'] <= value <= data['win_size']['w_max']:
            txt, color = '', ''
        else:
            txt, color = 'min ' + str(data['win_size']['w_min']) if value < data['win_size']['w_min'] else 'max ' + str(data['win_size']['w_max']), '#0048ff'
            label_w_info.grid(row=2, column=4)

        label_w_error['text'] = txt
        label_w_error['foreground'] = color

    def cost():
        price_profile = data['profile_price']['Steko']  # nominal price depend of profile
        cost_str = '0'

        value_h, logic_h = check_val_int(entry_h.get())
        win_h_info(value_h, logic_h)
        value_w, logic_w = check_val_int(entry_w.get())
        win_w_info(value_w, logic_w)

        if not value_h == 0 and not value_w == 0:
            # win_height = check_win_min_max(value_h, data['win_size']['h_min'], data['win_size']['h_max'])
            # win_width = check_win_min_max(value_w, data['win_size']['w_min'], data['win_size']['w_max'])
            if data['win_size']['h_min'] <= value_h <= data['win_size']['h_max'] and data['win_size']['w_min'] <= \
                    value_w <= data['win_size']['w_max']:
                cost_str = ((int(value_h) * int(value_w)) * 10**-6) * price_profile

        label_cost['text'] = str(int(cost_str))

    def clear_data() -> None:
        entry_h.delete(0, END)
        entry_w.delete(0, END)

        label_h_error['text'] = ''
        label_h_error['foreground'] = ''
        label_h_info.grid(row=1, column=3)

        label_w_error['text'] = ''
        label_w_error['foreground'] = ''
        label_w_info.grid(row=2, column=3)

    print('\twindow_calculator')

    window = Tk()
    window.title('CALCULATOR of PLASTIC WINDOW')
    window.geometry('950x650')

    label_s = ttk.Label(text='size h x w')

    label_h = ttk.Label(text='height mm')
    label_h_info = ttk.Label(text='ref: 1100...1800 mm', foreground='#18c73e')
    label_h_error = ttk.Label(text='', foreground='')

    label_w = ttk.Label(text='width mm')
    label_w_info = ttk.Label(text='ref: 950...1700 mm', foreground='#18c73e')
    label_w_error = ttk.Label(text='', foreground='')

    label_price = ttk.Label(text='price uah')
    label_cost = ttk.Label(text='0')

    label_s.grid(row=0, column=0)

    label_h.grid(row=1, column=1)
    label_h_info.grid(row=1, column=3)
    label_h_error.grid(row=1, column=3)

    label_w.grid(row=2, column=1)
    label_w_info.grid(row=2, column=3)
    label_w_error.grid(row=2, column=3)

    label_price.grid(row=3, column=1)
    label_cost.grid(row=3, column=2)

    entry_h = Entry(width=10)
    entry_w = Entry(width=10)
    entry_h.grid(row=1, column=2)
    entry_w.grid(row=2, column=2)

    btn_cost = ttk.Button(text='calculate cost', command=cost)
    btn_clear = ttk.Button(text='clear', command=clear_data)
    btn_cost.grid(row=3, column=3)
    btn_clear.grid(row=4, column=3)

    window.mainloop()
