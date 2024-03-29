from tkinter import ttk
import customtkinter as ctk
import pyautogui as gui
import time as t
from tkinter import messagebox
import time
import win32api
import win32con

# Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
page = ctk.CTk()
page.geometry("750x380")
page.title("Main Page")
page.resizable(False, False)

# Idk yet what

# Commands
def test(event):
    if win32api.GetKeyState(0x01) < 0:
        x, y = win32api.GetCursorPos()
        print(f"Cords({x}, {y})")

def pickLocation():
    page.bind("<Button-1>", test)

    #buttonPick.after(1000)
    #if win32api.GetKeyState(0x01): 
    #    x, y = win32api.GetCursorPos()
    #    print(f"Cords({x}, {y})")


def xd(time):
    if time < 0:
        return
    labelYet.configure(text =str(time))
    labelYet.after(1000,xd(time-1))
    print("I'm here")

def start():
    #0 - empty | 1 - mark
    if checkRepeat.get() == 0 and checkUntil.get() == 0:
        messagebox.showerror("Error","Chose repeat type!")
        return
    elif checkRepeat.get() == 1 and checkUntil.get() == 1:
        messagebox.showerror("Error","Chose only one click type!")
        checkRepeat.deselect()
        checkUntil.deselect()
        return
    
    if checkRepeat.get() == 1:
        try:
            repeat = int(entryTimeRepeat.get())
            xd(repeat)
            #for i in range(0, repeat):
            #    labelYet.configure(text = f"Clicks: {i}")
            #    labelYet.after(500)
        except:
            messagebox.showerror("Error","Set repeat time. Only numbers!")
    else:
        pass



    print("Done")

    #x = entryX.get()
    #y = entryY.get()
    #print(f"Clicking {x}|{y}")

## Tree commands
def addTotree():
    try:       
        tree.insert("", "end", iid=None, value=(int(entryX.get()), int(entryY.get()), comboMouseB.get(), int(entryTimeMS.get()))) # valuse x,y, r/l, delay
        entryX.delete(0, "end")
        entryY.delete(0, "end")
        comboMouseB.set("Left")
        entryTimeMS.delete(0, "end")
    except:
        messagebox.showerror("Error","Only Numbers!")
        entryX.delete(0, "end")
        entryY.delete(0, "end")
        comboMouseB.set("Left")
        entryTimeMS.delete(0, "end")


def delete():
    if len(tree.selection()) != 0:
        x = tree.selection()
        for record in x:
            tree.delete(record)
    else:
        for record in tree.get_children():
            tree.delete(record)



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
entryX = ctk.CTkEntry(leftFrame, width=50) ##?
entryX.grid(column=0, row=1, padx=1, pady=5)

labelY = ctk.CTkLabel(leftFrame, text="Y")
labelY.grid(column=1, row=1, sticky="w", padx=15, pady=5)
entryY = ctk.CTkEntry(leftFrame, width=50) ## ?
entryY.grid(column=1, row=1, padx=1, pady=5)
# row 2
labelMouseB = ctk.CTkLabel(leftFrame, text="Mouse button: ")
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
buttonAdd = ctk.CTkButton(leftFrame, text="Add position", command=addTotree)
buttonAdd.grid(columnspan=2, row= 4, padx=5, pady=5, sticky="we")
# row 5
checkRepeat = ctk.CTkCheckBox(leftFrame, text="Repeat")
checkRepeat.grid(column=0, row=5, padx=5, pady=5, sticky="w")

entryTimeRepeat = ctk.CTkEntry(leftFrame)
entryTimeRepeat.grid(column=1, row=5, sticky="e", padx=20, pady=5)
# row 6
checkUntil = ctk.CTkCheckBox(leftFrame, text="Reapeat until stopped")
checkUntil.grid( column=0, row=6, padx=5, pady=5)

labelYet = ctk.CTkLabel(leftFrame, text="0")
labelYet.grid(column=1, row=6, padx=5, pady=5)
# row 7
buttonStart = ctk.CTkButton(leftFrame, text="Start Clicking (F9)", command=start)
buttonStart.grid(columnspan=2, row= 7, padx=5, pady=5, sticky="we")
# row 8
buttonStop = ctk.CTkButton(leftFrame, text="Stop Clicking (F9)")
buttonStop.grid(columnspan=2, row= 8, padx=5, pady=5, sticky="we")
# row 9
buttonOptions = ctk.CTkButton(leftFrame, text="Options")
buttonOptions.grid(column= 0, row= 9, padx=5, pady=5, sticky="we")
buttonDelete = ctk.CTkButton(leftFrame, text="Delete Cord", command=delete)
buttonDelete.grid(column = 1, row= 9, padx=5, pady=5, sticky="we")

#label5 = ctk.CTkLabel(leftFrame, text="Queued Cursor Positions")
#label5.grid(column=3, row=0, padx=5, pady=5)

def set_column_width(tree, col, width):
    tree.column(col, minwidth=width, width=width, anchor="center")

cols = ("x", "y", "l/r", "delay")
tree = ttk.Treeview(page, columns=cols, show='headings', height=17) #IMPORTANT
#tree.column("x", width=100, stretch=False)
tree.heading("x", text="X")

#tree.column("y", width=100, stretch= False)
tree.heading("y", text="Y")

#tree.column("l/r", width=100)
tree.heading("l/r", text="L/R")

#tree.column("delay", width=100)
tree.heading("delay", text="Delay (MS)")

set_column_width(tree, "x", 100)
set_column_width(tree, "y", 100)
set_column_width(tree, "l/r", 100)
set_column_width(tree, "delay", 100)

tree.grid(column=3, row=0, rowspan=9, sticky="nw", padx=5, pady=7)

page.mainloop()