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

#check1 = ctk.CTkCheckBox(leftFrame, text="", checkbox_width=50, width=0)
#check1.grid(column=0, row=0, padx=5, pady=5)
buttonPick = ctk.CTkButton(leftFrame, text="Pick location")
buttonPick.grid(row=0, padx=5, pady=5, columnspan=2, sticky="we")

labelX = ctk.CTkLabel(leftFrame, text="X")
labelX.grid(column=0, row=1, sticky="w", padx=15, pady=5)
entryX = ctk.CTkEntry(leftFrame, width=50)
entryX.grid(column=0, row=1, padx=1, pady=5)

labelY = ctk.CTkLabel(leftFrame, text="Y")
labelY.grid(column=1, row=1, sticky="w", padx=15, pady=5)
entryY = ctk.CTkEntry(leftFrame, width=50)
entryY.grid(column=1, row=1, padx=1, pady=5)

labelMouseB = ctk.CTkButton(leftFrame, text="Mouse button: ")
labelMouseB.grid(column=0, row=2, padx=5, pady=5)
comboMouseB =  ctk.CTkComboBox(leftFrame, values=["Left", "Right"], state="readonly") #combobox.bind('<<ComboboxSelected>>', callback)
comboMouseB.set("Left")
comboMouseB.grid(column=1, row=2, padx=5, pady=5)

labelTimeMS = ctk.CTkLabel(leftFrame, text="Time to sleep (MS): ")
labelTimeMS.grid(column=0, row=3, padx=5, pady=5)
entryTimeMS = ctk.CTkEntry(leftFrame)
entryTimeMS.grid(column=1, row=3, sticky="e", padx=20, pady=5)

buttonAdd = ctk.CTkButton(leftFrame, text="Add position")
buttonAdd.grid(columnspan=2, row= 4, padx=5, pady=5, sticky="we")

checkRepeat = ctk.CTkCheckBox(leftFrame, text="Repeat")
checkRepeat.grid(column=0, row=5, padx=5, pady=5)
entryTimeRepeat = ctk.CTkEntry(leftFrame)
entryTimeRepeat.grid(column=1, row=5, sticky="e", padx=20, pady=5)

checkUntil = ctk.CTkCheckBox(leftFrame, text="Reapeat until stopped")
checkUntil.grid( columnspan=2, row=6, padx=5, pady=5)

buttonStart = ctk.CTkButton(leftFrame, text="Start Clicking (F9)")
buttonStart.grid(columnspan=2, row= 7, padx=5, pady=5, sticky="we")
buttonStop = ctk.CTkButton(leftFrame, text="Stop Clicking (F9)")
buttonStop.grid(columnspan=2, row= 8, padx=5, pady=5, sticky="we")
buttonOptions = ctk.CTkButton(leftFrame, text="Options")
buttonOptions.grid(columnspan=2, row= 9, padx=5, pady=5, sticky="we")

#label5 = ctk.CTkLabel(leftFrame, text="Queued Cursor Positions")
#label5.grid(column=3, row=0, padx=5, pady=5)

cols = ("x", "y", "l/r", "delay")
tree = ttk.Treeview(page, columns=cols, show='headings', height=17) #IMPORTANT
tree.column("x", width=100, stretch=False)
tree.heading("x", text="X")

tree.column("y", width=100, stretch= False)
tree.heading("y", text="Y")

tree.column("l/r", width=100)
tree.heading("l/r", text="L/R")

tree.column("delay", width=100)
tree.heading("delay", text="Delay (MS)")


tree.grid(column=3, row=0, rowspan=9, sticky="nw", padx=5, pady=7)





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