import tkinter as tk

answer = ""

def buy_window():
    buy = tk.Tk()

    #color window
    buy_frame = tk.Frame(buy, bg='lightgreen')
    buy_frame.place(relwidth=1, relheight=1)

    buy.title('Quote Window')
    buy.geometry('600x400+100+100')

    name = tk.StringVar()

    #textinput
    name_label = tk.Label(buy, text='Select your option:')
    name_label.pack(ipadx=10, ipady=10)

    #input
    name_entry = tk.Entry(buy, textvariable=name)
    name_entry.pack(fill='x', expand=True)
    name_entry.focus()

    #Lable that appears after shopping
    answer_label = tk.Label(buy, text='Thank you for shopping!')
    answer_label.pack(ipadx=10, ipady=10)
    answer_label.pack_forget()

    #buttons
    answer_button = tk.Button(
        buy,
        text='Buy',
        command=lambda: answer_label.pack()
    )

    answer_button.pack(
        ipadx=50,
        ipady=5,
        expand=True
    )

    #exit button
    exit_button = tk.Button(
        buy,
        text='Leave',
        command=lambda: buy.destroy()
    )

    exit_button.pack(
        ipadx=50,
        ipady=5,
        expand=True
    )

root = tk.Tk()

#color window
frame = tk.Frame(root, bg='yellow')
frame.place(relwidth=1, relheight=1)

root.title('Welcome Window')
root.geometry('600x400+50+50')

#images
question_label = tk.Label(root, text='Do you want a wrench or a hammer?')
question_label.pack(ipadx=10, ipady=10)

wrench_photo = tk.PhotoImage('./images/tools2.png')
wrench = tk.Label(
    root,
    image=wrench_photo,
    text='Wrench',
    compound='top'
)
wrench.pack()

hammer_photo = tk.PhotoImage('./images/tools3.png')
hammer = tk.Label(
    root,
    image=hammer_photo,
    text='Hammer',
    compound='top'
)
hammer.pack()

#buttons
quote_button = tk.Button(
    root,
    text='Buy something',
    command=buy_window
)

quote_button.pack(
    ipadx=50,
    ipady=5,
    expand=True
)

exit_button = tk.Button(
    root,
    text='Leave',
    command=lambda: root.destroy()
)

exit_button.pack(
    ipadx=50,
    ipady=5,
    expand=True
)

tk.mainloop()