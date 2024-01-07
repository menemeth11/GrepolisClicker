from tkinter import ttk
import customtkinter as ctk

# Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
page = ctk.CTk()
page.geometry("800x400")
page.title("Main Page")
page.resizable(False, False)

# Functions

# Desing
mainFrame = ctk.CTkFrame(page, width=800, height=400, border_color="red", border_width=5).grid()

leftFrame = ctk.CTkFrame(mainFrame, width=200, height=400, border_color="green", border_width=3).grid(column=0, rowspan=0)




'''

widgetsFrame = ctk.CTkFrame(mainFrame, border_color="green", border_width=44, width=400, height=200)
widgetsFrame.grid(row=0, column=0)

nameEntry = ctk.CTkEntry(widgetsFrame, placeholder_text="test1234")
nameEntry.grid(row=0, column=0)
'''
'''
frame = ttk.Frame(page)
frame.pack()

widgetsFrame = ttk.LabelFrame(frame, text="inseret:")
widgetsFrame.grid(row=0, column=0)

nameEntry = ttk.Entry(widgetsFrame)
nameEntry.insert(0, "Name")
nameEntry.grid(row=0, column=0, sticky="ew")
'''
'''
tree = ttk.Treeview(mainFrame)
tree['columns'] = ("X", "Y", "L/R", "Delay (MS)")

## Format Columns
tree.column("X", width= 100)
tree.column("Y", width= 100)
tree.column("L/R", width= 100)
tree.column("Delay (MS)", width= 100)
tree.column("#0", width= 10)

## Create Headers
tree.heading("X", text="X")
tree.heading("Y", text="Y")
tree.heading("L/R", text="L/R")
tree.heading("Delay (MS)", text="Delay (MS)")
tree.heading("#0", text=".")

## Add elements
#tree.insert(parent="", index="end", idd=0, text="Hi", values=(6, 9, "L", 100))

## Do it!
tree.pack()
'''



page.mainloop()