from tkinter import ttk
import customtkinter as ctk

# Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
page = ctk.CTk()
page.geometry("750x375")
page.title("Main Page")
page.resizable(False, False)

# Functions

# Desing

## create all of the main containers
leftFrame = ctk.CTkFrame(page, width=400)
leftFrame.grid()
#rightFrame = ctk.CTkFrame(page, width=400, height=400, border_color="red", border_width=5).grid(column=1, row=0)

check1 = ctk.CTkCheckBox(leftFrame, text="", checkbox_width=50, width=0)
check1.grid(column=0, row=0, padx=5, pady=5)
button1 = ctk.CTkButton(leftFrame)
button1.grid(column=1, row=0, padx=5, pady=5)

label1 = ctk.CTkLabel(leftFrame, text="X")
label1.grid(column=0, row=1, sticky="w", padx=15, pady=5)
entry1 = ctk.CTkEntry(leftFrame, width=50)
entry1.grid(column=0, row=1, padx=1, pady=5)

label2 = ctk.CTkLabel(leftFrame, text="Y")
label2.grid(column=1, row=1, sticky="w", padx=15, pady=5)
entry2 = ctk.CTkEntry(leftFrame, width=50)
entry2.grid(column=1, row=1, padx=1, pady=5)

label3 = ctk.CTkButton(leftFrame, text="Mouse button: ")
label3.grid(column=0, row=2, padx=5, pady=5)
combo1 =  ctk.CTkComboBox(leftFrame, values=["Left", "Right"], state="readonly") #combobox.bind('<<ComboboxSelected>>', callback)
combo1.set("Left")
combo1.grid(column=1, row=2, padx=5, pady=5)

label4 = ctk.CTkLabel(leftFrame, text="Time to sleep (MS): ")
label4.grid(column=0, row=3, padx=5, pady=5)
entry3 = ctk.CTkEntry(leftFrame)
entry3.grid(column=1, row=3, sticky="e", padx=20, pady=5)

button2 = ctk.CTkButton(leftFrame, text="Add position")
button2.grid(columnspan=2, row= 4, padx=5, pady=5, sticky="we")

check2 = ctk.CTkCheckBox(leftFrame, text="Repeat")
check2.grid(column=0, row=5, padx=5, pady=5)
entry3 = ctk.CTkEntry(leftFrame)
entry3.grid(column=1, row=5, sticky="e", padx=20, pady=5)

check2 = ctk.CTkCheckBox(leftFrame, text="Reapeat until stopped")
check2.grid( columnspan=2, row=6, padx=5, pady=5)

button3 = ctk.CTkButton(leftFrame, text="Start Clicking (F9)")
button3.grid(columnspan=2, row= 7, padx=5, pady=5, sticky="we")
button4 = ctk.CTkButton(leftFrame, text="Stop Clicking (F9)")
button4.grid(columnspan=2, row= 8, padx=5, pady=5, sticky="we")
button5 = ctk.CTkButton(leftFrame, text="Options")
button5.grid(columnspan=2, row= 9, padx=5, pady=5, sticky="we")

cols = ("x", "y", "l/r", "delay")
tree = ttk.Treeview(page, columns=cols, show='headings', height=17) #IMPORTANT
tree.column("x", width=100)
tree.heading("x", text="X")

tree.column("y", width=100)
tree.heading("y", text="Y")

tree.column("l/r", width=100)
tree.heading("l/r", text="L/R")

tree.column("delay", width=100)
tree.heading("delay", text="Delay (MS)")

tree.grid(column=3, row=0 ,rowspan=9, sticky="nw", padx=5, pady=7)





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