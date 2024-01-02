import tkinter as tk
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
#idk = tk.Tk()
page = ctk.CTk()
page.geometry("720x360")
page.title("Login/Register Page")

label = ctk.CTkLabel(page, text="Hi, Login Page")
label.pack()


label1 = ctk.CTkLabel(page, text="HELLO WORLD!", font=("Segoe UI", 50, "bold"), text_color="red")
label1.pack()

frameMenu = ctk.CTkFrame(page, height=200, width=600)
frameMenu.pack()
#next
loginFrame = tk.LabelFrame(frameMenu, text="Login", bd=5, relief="ridge")
loginFrame.grid(row=0, column=0, sticky="W", padx=20, pady=20)

label2 = ctk.CTkEntry(loginFrame, placeholder_text="PUT LOGIN HERE").pack(pady=10)

passwordsFrame = tk.LabelFrame(frameMenu, text="Password", bd=5, relief="ridge")
passwordsFrame.grid(row=1, column=0, sticky="W", padx=20, pady=20)

label3 = ctk.CTkEntry(passwordsFrame, placeholder_text="PUT PASSWORD HERE").pack(pady=10)


buttonPrev = ctk.CTkButton(page, text="Previous Page", command=PrevPage, state="disabled")
buttonPrev.pack(side="left", padx=10, pady=10)
'''
def Quit():
    answer = messageBox.askyesno(title="Quit Confirm", message="Are you sure you want to quit"
    if answer:
        page.destroy()
'''
buttonQuit = ctk.CTkButton(page, text="QUIT", state="disabled").pack(side="left")

buttonNext = ctk.CTkButton(page, text="Next Page", command=NextPage)
buttonNext.pack(side="right", padx=10, pady=10)


page.mainloop()