from tkinter import ttk
import customtkinter as ctk
import time as t


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
#***
'''
def PrevPage():
    page.destroy()
    import login

def NextPage():
    page.destroy()
    import main
'''
#***
page = ctk.CTk()
page.geometry("800x1000")
page.title("Main Page")
page.resizable(False, False)

lol = ""
def dialog():
    lol = ctk.CTkInputDialog(title=" XDD", text="text 4fun") #how this works?
def dialog2():
    print(lol)


label = ctk.CTkLabel(page, text="OKE! Lets's Go!", font=("Segoe UI", 40, "bold"), text_color="red")
label.pack()

x = ctk.CTkCheckBox(page, text="Do You like it?").pack(pady=10)
#y = ctk.CTkLabel(page, width=100, height= 100, bg_color="white", ).pack()
z = ctk.CTkButton(page, text="press it!", command=dialog).pack(pady=10)
z2 = ctk.CTkButton(page, text="press it!", command=dialog2, hover_color="yellow").pack(pady=10)

y = ctk.CTkScrollableFrame(page)
y.pack(pady=10)
label1 = ctk.CTkLabel(y,text="test1").pack(pady=5)
label2 = ctk.CTkLabel(y,text="test2").pack(pady=5)
label3 = ctk.CTkLabel(y,text="test3").pack(pady=5)
label4 = ctk.CTkLabel(y,text="test4").pack(pady=5)

v = ctk.CTkSegmentedButton(page).pack() #this?
v2 = ctk.CTkTextbox(page).pack()
v3 = ctk.CTkSwitch(page).pack()
v4 = ctk.CTkSlider(page).pack()
v5 = ctk.CTkComboBox(page).pack()
v6 = ctk.CTkRadioButton(page).pack()
#v7 = ctk.CTkTabview(page).pack()


cols = ('first_name', 'last_name', 'email')
v8 = ttk.Treeview(page, columns=cols, show='headings', height=13) #IMPORTANT
v8.heading("first_name", text="its works!")


v8.pack()
#buttonPrev = ctk.CTkButton(page, text="Previous Page", command=PrevPage)
#buttonPrev.pack(side="left", padx=10, pady=10)

#buttonNext = ctk.CTkButton(page, text="Next Page", command=NextPage, state="disabled")
#buttonNext.pack(side="right", padx=10, pady=10)
page.mainloop()