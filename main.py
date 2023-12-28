#import tkinter ??
import customtkinter as ctk


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
#***
def PrevPage():
    page.destroy()
    import login

def NextPage():
    page.destroy()
    import main

#***
page = ctk.CTk()
page.geometry("720x360")
page.title("Main Page")

label = ctk.CTkLabel(page, text="Hi, Main Page")
label.pack()

label1 = ctk.CTkLabel(page, text="HELLO WORLD 2!", font=("Segoe UI", 40, "bold"), text_color="red")
label1.pack()

buttonPrev = ctk.CTkButton(page, text="Previous Page", command=PrevPage)
buttonPrev.pack(side="left", padx=10, pady=10)

buttonNext = ctk.CTkButton(page, text="Next Page", command=NextPage, state="disabled")
buttonNext.pack(side="right", padx=10, pady=10)


page.mainloop()