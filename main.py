import tkinter as tk
import tribe_data


def inactive_members_panel():
    clear(menu_frame)
    menu_frame.pack_forget()
    main_frame.pack()
    tk.Checkbutton(main_frame, text="show only inactive").grid(row=0, column=0)
    tk.Button(main_frame, command=main_window, text="Back").grid(row=1, column=0)


def rank_panel():
    clear(menu_frame)
    menu_frame.pack_forget()
    main_frame.pack()
    tk.Text(main_frame).grid(row=0, column=0)
    tk.Entry(main_frame, text='World number').grid(row=1, column=0)
    tk.Entry(main_frame, text='Tribe Id').grid(row=2, column=0)
    tk.Button(main_frame, text='Show ranking').grid(row=3, column=0)
    tk.Button(main_frame, text='Back', command=main_window).grid(row=4, column=0)


def conquerors_panel():
    clear(menu_frame)
    menu_frame.pack_forget()
    main_frame.pack()
    tk.Text(main_frame).grid(row=0, column=0)
    tk.Entry(main_frame, text='World number').grid(row=1, column=0)
    tk.Entry(main_frame, text='Conquerors count').grid(row=2, column=0)
    tk.Button(main_frame, text='Show conquerors').grid(row=3, column=0)
    tk.Button(main_frame, text='Back', command=main_window).grid(row=4, column=0)


def main_window():
    clear(main_frame)
    main_frame.pack_forget()
    menu_frame.pack()
    tk.Button(menu_frame, text='Show inactive members', command=inactive_members_panel).grid(row=0, column=0)
    tk.Button(menu_frame, text='Show players ranking', command=rank_panel).grid(row=1, column=0)
    tk.Button(menu_frame, text='Show Last conquerors', command=conquerors_panel).grid(row=2, column=0)


def clear(object):
    elements = object.winfo_children()
    for e in elements:
        e.destroy()

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Menu')
    main_frame = tk.Frame(window)
    menu_frame = tk.Frame(window)
    main_window()
    tk.mainloop()



