import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, bg='darkgray')
frame.place(relwidth=1, relheight=1)

root.title('Welcome Window')
root.geometry('600x400+50+50')

tk.mainloop()