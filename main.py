import tkinter as tk
import tkinter.font
from tkinter import scrolledtext
import tribe_data


def inactive_members_panel():
    clear(menu_frame)
    menu_frame.pack_forget()
    main_frame.pack()
    chb = tk.BooleanVar()
    tk.Checkbutton(main_frame, text="Show only inactive", variable=chb).grid(row=0, column=0)
    ent1 = tk.Entry(main_frame)
    ent1.grid(row=1, column=0)
    ent2 = tk.Entry(main_frame)
    ent2.grid(row=2, column=0)
    tk.Button(main_frame, text='Show Players',
              command=lambda: tribe_data.show_inactive_members(ent1.get(), ent2.get(), chb.get())).grid(row=3, column=0)
    tk.Button(main_frame, command=main_window, text="Back").grid(row=4, column=0)


def rank_panel():
    clear(menu_frame)
    menu_frame.pack_forget()
    window.title("Rank Panel")
    main_frame.pack()
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    fon = ("TIMES", 16)
    fonb = ("TIMES", 16, "bold")
    tx = scrolledtext.ScrolledText(main_frame, width=90, height=11, wrap=tk.WORD, bg="#FFF2E5")
    tx.grid(row=3, columnspan=2, padx=20, pady=20)
    tk.Label(main_frame, text='Enter World number', bg='#FFDAB3', font=fonb).grid(row=0, column=0, padx=5, pady=5)
    wn = tk.Entry(main_frame, bg="#FFF2E5")
    wn.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(main_frame, text='Enter Tribe Id', bg='#FFDAB3', font=fonb).grid(row=1, column=0, padx=5, pady=5)
    idp = tk.Entry(main_frame, bg="#FFF2E5")
    idp.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(main_frame, text='Show World Tribes', font=fon, command=lambda: get_top(wn.get(), tx)).grid(row=2,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5)
    tk.Button(main_frame, text='Show ranking', font=fon, command=lambda: show_ranks(wn.get(), idp.get(), tx)).grid(
        row=2, column=1, padx=5, pady=5)
    tk.Button(main_frame, text='Back to menu', font=fon, command=main_window).grid(row=4, columnspan=2, padx=5, pady=5)


def get_top(world_number, stxt):
    if len(world_number) > 0 and world_number.isnumeric():
        txt = tribe_data.show_active_tribe(world_number)
        stxt.tag_configure('center', justify='center')
        stxt.delete('1.0', tk.END)
        stxt.insert('1.0', txt)
        stxt.tag_add('center', '1.0', tk.END)
    else:
        txt = 'Enter correct world number'
        stxt.tag_configure('center', justify='center')
        stxt.delete('1.0', tk.END)
        stxt.insert('1.0', txt, 'center')
        stxt.tag_add('center', '1.0', tk.END)


def show_ranks(world_number, idp, stxt):
    if world_number.isnumeric() and len(world_number) > 0:
        if idp.isnumeric() and len(idp) > 0:
            txt = tribe_data.show_rank_stats(world_number, idp)
            stxt.delete('1.0', tk.END)
            stxt.insert('1.0', txt)
        else:
            txt = "No corresponding Id. " \
                  "Make sure you enter correct Id\n" \
                  "If you don't see Top Tribe Id's. " \
                  "Use Show World Tribe Button\n" \
                  "World Tribe should be numeric value"
            stxt.delete('1.0', tk.END)
            stxt.insert('1.0', txt)
    else:
        txt = "Cannot find specific World. " \
              "Make sure you enter\n" \
              "correct number (1-165). " \
              "World should be numeric value"
        stxt.delete('1.0', tk.END)
        stxt.insert('1.0', txt)


def conquerors_panel():
    clear(menu_frame)
    menu_frame.pack_forget()
    main_frame.pack()
    tk.Text(main_frame, height=3).grid(row=0, column=0)
    tk.Entry(main_frame, text='World number').grid(row=1, column=0)
    tk.Entry(main_frame, text='Conquerors count').grid(row=2, column=0)
    tk.Button(main_frame, text='Show conquerors').grid(row=3, column=0)
    tk.Button(main_frame, text='Back', command=main_window).grid(row=4, column=0)


def main_window():
    clear(main_frame)
    main_frame.place_forget()
    main_frame.pack_forget()
    menu_frame.pack()
    window.title("Menu Panel")
    fon = ("TIMES", 16)
    tx = tk.Text(menu_frame, height=10, width=40, font=fon)
    tx.grid(row=0, column=1, padx=20, pady=20, columnspan=3)
    tx.configure(bg='#FFF5E4')
    tx.tag_configure('center', justify='center')
    info = "Welcome in tribe data analizer.\n" \
           "This program is allow to show some data\n" \
           "for the browser game 'www.plemiona.pl'.\n" \
           "Choose any button to do an action\n" \
           "Show inactive members - You can see inactive\n" \
           "players of choosen tribe\n" \
           "Show players ranking - You can see ranking\n" \
           "statistics of choosen Tribe\n" \
           "Show last conquerors - You can see the last\n" \
           "conquerors of choosen world"
    tx.insert(tk.END, info, 'center')
    tk.Button(menu_frame, text='Show inactive members', font=fon, bg="#FFCC99",  command=inactive_members_panel).grid(row=1, column=1,
                                                                                                       padx=5, pady=5)
    tk.Button(menu_frame, text='Show players ranking', font=fon, bg="#FFCC99", command=rank_panel).grid(row=1, column=2,
                                                                                                        padx=5, pady=5)
    tk.Button(menu_frame, text='Show Last conquerors', font=fon, bg="#FFCC99", command=conquerors_panel).grid(row=1,
                                                                                                              column=3,
                                                                                                              padx=5,
                                                                                                              pady=5)


def clear(object):
    elements = object.winfo_children()
    for e in elements:
        e.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('800x480')
    window.configure(bg='#FFDAB3')
    window.title("Menu Panel")
    menu_frame = tk.Frame(window)
    main_frame = tk.Frame(window)
    main_frame.configure(bg='#FFDAB3')
    menu_frame.configure(bg='#FFDAB3')
    main_window()
    tk.mainloop()
