from tkinter import ttk
import customtkinter as ctk
import pyautogui as gui
import time as t
import win32api
import win32con

# Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
page = ctk.CTk()
page.geometry("750x375")
page.title("Main Page")
page.resizable(False, False)

# Idk yet what

# Commands
def test():
    #state = win32api.GetKeyState(0x01)
    if win32api.GetKeyState(0x01): 
        cords = gui.position()
        print(cords)

def pickLocation():
    test()
# Desing
leftFrame = ctk.CTkFrame(page, width=400)
leftFrame.grid()
#rightFrame = ctk.CTkFrame(page, width=400, height=400, border_color="red", border_width=5).grid(column=1, row=0)
#check1 = ctk.CTkCheckBox(leftFrame, text="", checkbox_width=50, width=0)
#check1.grid(column=0, row=0, padx=5, pady=5)
# row 0
buttonPick = ctk.CTkButton(leftFrame, text="Pick location", command=pickLocation)
buttonPick.grid(row=0, padx=5, pady=5, columnspan=2, sticky="we")
# row 1
labelX = ctk.CTkLabel(leftFrame, text="X")
labelX.grid(column=0, row=1, sticky="w", padx=15, pady=5)
entryX = ctk.CTkEntry(leftFrame, width=50)
entryX.grid(column=0, row=1, padx=1, pady=5)

labelY = ctk.CTkLabel(leftFrame, text="Y")
labelY.grid(column=1, row=1, sticky="w", padx=15, pady=5)
entryY = ctk.CTkEntry(leftFrame, width=50)
entryY.grid(column=1, row=1, padx=1, pady=5)
# row 2
labelMouseB = ctk.CTkButton(leftFrame, text="Mouse button: ")
labelMouseB.grid(column=0, row=2, padx=5, pady=5)
comboMouseB =  ctk.CTkComboBox(leftFrame, values=["Left", "Right"], state="readonly") #combobox.bind('<<ComboboxSelected>>', callback)
comboMouseB.set("Left")
comboMouseB.grid(column=1, row=2, padx=5, pady=5)
# row 3
labelTimeMS = ctk.CTkLabel(leftFrame, text="Time to sleep (MS): ")
labelTimeMS.grid(column=0, row=3, padx=5, pady=5)
entryTimeMS = ctk.CTkEntry(leftFrame)
entryTimeMS.grid(column=1, row=3, sticky="e", padx=20, pady=5)
# row 4
buttonAdd = ctk.CTkButton(leftFrame, text="Add position")
buttonAdd.grid(columnspan=2, row= 4, padx=5, pady=5, sticky="we")
# row 5
checkRepeat = ctk.CTkCheckBox(leftFrame, text="Repeat")
checkRepeat.grid(column=0, row=5, padx=5, pady=5)
entryTimeRepeat = ctk.CTkEntry(leftFrame)
entryTimeRepeat.grid(column=1, row=5, sticky="e", padx=20, pady=5)
# row 6
checkUntil = ctk.CTkCheckBox(leftFrame, text="Reapeat until stopped")
checkUntil.grid( columnspan=2, row=6, padx=5, pady=5)
# row 7
buttonStart = ctk.CTkButton(leftFrame, text="Start Clicking (F9)")
buttonStart.grid(columnspan=2, row= 7, padx=5, pady=5, sticky="we")
# row 8
buttonStop = ctk.CTkButton(leftFrame, text="Stop Clicking (F9)")
buttonStop.grid(columnspan=2, row= 8, padx=5, pady=5, sticky="we")
# row 9
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

page.mainloop()