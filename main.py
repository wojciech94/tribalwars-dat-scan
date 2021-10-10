import tkinter as tk
from tkinter import scrolledtext
import tribe_data


def inactive_members_panel():
    clear(menu_frame)
    menu_frame.pack_forget()
    window.title("Inactive members panel")
    main_frame.pack()
    fon = ("TIMES", 16)
    fonb = ("TIMES", 16, "bold")
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    sct = scrolledtext.ScrolledText(main_frame, width=90, height=11, wrap=tk.WORD, bg="#FFF2E5")
    sct.grid(row=3, columnspan=3, padx=10, pady=10)
    chb = tk.BooleanVar()
    tk.Checkbutton(main_frame, text="Show only inactive", bg='#FFDAB3', variable=chb, font=fonb).grid(row=0, column=0)
    tk.Label(main_frame, text="World number", bg='#FFDAB3', font=fonb, padx=2, pady=2).grid(row=1, column=0)
    worldEntry = tk.Entry(main_frame, font=fon, bg="#FFF2E5", )
    worldEntry.grid(row=1, column=1)
    tk.Label(main_frame, bg='#FFDAB3', text="Tribe", font=fonb, padx=2, pady=2).grid(row=2, column=0)
    idEntry = tk.Entry(main_frame, bg="#FFF2E5", font=fon)
    idEntry.grid(row=2, column=1)
    tk.Button(main_frame, text="Show Tribes Id", bg="#FFF2E5", font=fon,
              command=lambda: get_top(worldEntry.get(), sct)).grid(row=1, column=2, padx=5, pady=5)
    tk.Button(main_frame, text='Show Players', bg="#FFF2E5", font=fon,
              command=lambda: show_tribe_data(worldEntry.get(), idEntry.get(), sct, False, chb.get())) \
        .grid(row=2, column=2, padx=5, pady=5)
    tk.Button(main_frame, command=main_window, bg="#FFF2E5", text="Back to menu", font=fon).grid(row=4, column=1)


def rank_panel():
    clear(menu_frame)
    menu_frame.pack_forget()
    window.title("Rank Panel")
    main_frame.pack()
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    fon = ("TIMES", 16)
    fonb = ("TIMES", 16, "bold")
    tx = scrolledtext.ScrolledText(main_frame, width=90, height=11, wrap=tk.WORD, bg="#FFF2E5")
    tx.grid(row=3, columnspan=5, padx=20, pady=20)
    tk.Label(main_frame, text='Enter World number', bg='#FFDAB3', font=fonb).grid(row=0, column=0, padx=5, pady=5)
    wn = tk.Entry(main_frame, bg="#FFF2E5")
    wn.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(main_frame, text='Enter Tribe Id', bg='#FFDAB3', font=fonb).grid(row=1, column=0, padx=5, pady=5)
    idp = tk.Entry(main_frame, bg="#FFF2E5")
    idp.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(main_frame, text='Show World Tribes', font=fon, bg="#FFF2E5", command=lambda: get_top(wn.get(), tx)) \
        .grid(row=0, column=3, padx=5, pady=5)
    tk.Button(main_frame, text='Show ranking', font=fon, command=lambda: show_tribe_data(wn.get(), idp.get(), tx, True),
              bg="#FFF2E5").grid(row=1, column=3, padx=5, pady=5)
    tk.Button(main_frame, text='Back to menu', font=fon, bg="#FFF2E5", command=main_window).grid(row=4, columnspan=5,
                                                                                                 padx=5, pady=5)


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


def show_tribe_data(world_number, idp, stxt, showranking, showInactive=False):
    stxt.tag_configure('center', justify='center')
    if world_number.isnumeric() and len(world_number) > 0:
        if idp.isnumeric() and len(idp) > 0:
            if showranking:
                txt = tribe_data.show_rank_stats(world_number, idp)
            else:
                txt = tribe_data.show_inactive_members(world_number, idp, showInactive)
            stxt.delete('1.0', tk.END)
            stxt.insert('1.0', txt)
            stxt.tag_add('center', '1.0', tk.END)
        else:
            txt = "No corresponding Id. " \
                  "Make sure you enter correct Id\n" \
                  "If you don't see Top Tribe Id's. " \
                  "Use Show World Tribe Button\n" \
                  "World Tribe should be numeric value"
            stxt.delete('1.0', tk.END)
            stxt.insert('1.0', txt)
            stxt.tag_add('center', '1.0', tk.END)
    else:
        txt = "Cannot find specific World. " \
              "Make sure you enter\n" \
              "correct number (1-165). " \
              "World should be numeric value"
        stxt.delete('1.0', tk.END)
        stxt.insert('1.0', txt)
        stxt.tag_add('center', '1.0', tk.END)


def conquerors_panel():
    clear(menu_frame)
    menu_frame.pack_forget()
    main_frame.pack()
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    fon = ("TIMES", 16)
    fonb = ("TIMES", 16, "bold")
    tx = scrolledtext.ScrolledText(main_frame, width=90, height=11, wrap=tk.WORD, bg="#FFF2E5")
    tx.grid(row=4, columnspan=4, padx=5, pady=5)
    tk.Label(main_frame, text='Enter world number', bg='#FFDAB3', font=fonb) \
        .grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    tk.Label(main_frame, text='Enter conquerors count', bg='#FFDAB3', font=fonb) \
        .grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    e1 = tk.Entry(main_frame, font=fon)
    e1.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
    e2 = tk.Entry(main_frame, font=fon)
    e2.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
    tk.Button(main_frame, text='Show last conquerors', font=fon, bg='#FFDAB3',
              command=lambda: set_conquerors_data(e1.get(), e2.get(), tx)).grid(row=3, column=1, columnspan=2, padx=5,
                                                                                pady=5)
    tk.Button(main_frame, text='Back', font=fon, bg='#FFDAB3',
              command=main_window).grid(row=5, column=1, columnspan=2, padx=5, pady=5)


def set_conquerors_data(world_number, count, stxt):
    stxt.tag_configure('center', justify='center')
    if world_number.isnumeric() and len(world_number) > 0:
        if count.isnumeric() and int(count) > 0:
            txt = tribe_data.find_enemy_conquerors(world_number, count)
        else:
            txt = "Conquerors count must be more than 0"
    else:
        txt = "Cannot find specific World. " \
              "Make sure you enter\n" \
              "correct number (1-165). " \
              "World should be numeric value"
    stxt.delete('1.0', tk.END)
    stxt.insert('1.0', txt)
    stxt.tag_add('center', '1.0', tk.END)


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
    tk.Button(menu_frame, text='Show inactive members', font=fon, bg="#FFCC99", command=inactive_members_panel).grid(
        row=1, column=1,
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
