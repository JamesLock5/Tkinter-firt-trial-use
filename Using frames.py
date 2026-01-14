import tkinter as tk

root = tk.Tk()
root.title('Using Frames')
root.geometry('500x500')

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 5)


root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)


label1 = tk.Label(root, text= 'LABEL', relief = 'solid')
label1.grid(row = 0, column = 0, columnspan = 3, sticky = 'ewsn', padx = 5, pady = 5)


left_frame = tk.Frame(root, relief = 'solid', borderwidth = 5)
left_frame.grid(row = 1, column = 0, sticky = 'nsew',  padx = 5, pady = 5)
left_frame.rowconfigure(0, weight = 1)
left_frame.rowconfigure(1, weight = 1)
left_frame.rowconfigure(2, weight = 1)
left_frame.grid_propagate(False)


right_frame = tk.Frame(root, relief = 'solid', borderwidth = 5)
right_frame.grid(row = 1, column = 1, sticky = 'nsew', padx = 5, pady = 5)
right_frame.rowconfigure(0, weight = 1)
right_frame.rowconfigure(1, weight = 1)
right_frame.grid_propagate(False)

entry1 = tk.Entry(left_frame)
entry1.grid(row = 0, column = 0, padx = 50, pady =5)

entry2 = tk.Entry(left_frame)
entry2.grid(row = 1, column = 0, padx = 50, pady =5)

entry3 = tk.Entry(left_frame)
entry3.grid(row = 2, column = 0, padx = 50, pady =5)

entry4 = tk.Entry(right_frame)
entry4.grid(row = 0, column = 0, padx = 50, pady =5)

entry5 = tk.Entry(right_frame)
entry5.grid(row = 1, column = 0, padx = 50, pady =5)
















root.mainloop()
