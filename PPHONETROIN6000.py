from tkinter import *
from tkinter import ttk
root = Tk()
root.title('PPHONE TROIN 6000')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


ttk.Label(mainframe, text="I AM PPHONETROIN 6000").grid()
ttk.Button(mainframe, text="PPHONE TROIN 6000").grid()
root.mainloop()