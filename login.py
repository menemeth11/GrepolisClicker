import time
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
page.geometry("470x360")
page.title("Login/Register Page")
page.resizable(False, False)

label = ctk.CTkLabel(page, text="HELLO WORLD!", font=("Segoe UI", 50, "bold"), text_color="red", bg_color="yellow").grid(column=0, row=0,columnspan= 2, sticky="we")

menuFrame = ctk.CTkFrame(page, width=450, height=80, border_width=3, border_color="green").grid(column=0, row=1,columnspan= 2,rowspan=2, padx=10, pady=10)

textLogin = ""
labelLogin = ctk.CTkLabel(menuFrame, text="LOGIN:", text_color="green", font=("Segoe UI", 15, "bold"), bg_color="#2b2b2b").grid(column=0, row=1,sticky="s")
inputLogin = ctk.CTkEntry(menuFrame, placeholder_text="Put Your login here", width=180, textvariable=textLogin).grid(column=0, row=2, sticky="n")

textPassword = ""
labelPassword = ctk.CTkLabel(menuFrame, text="PASSWORD:", text_color="green", font=("Segoe UI", 15, "bold"), bg_color="#2b2b2b").grid(column=1, row=1,sticky="s")
inputPassword = ctk.CTkEntry(menuFrame, placeholder_text="Put Your password here", width=180, show="*", textvariable=textPassword).grid(column=1, row=2, sticky="n")




def login():
    print(f"Login: {textLogin}, Password: {textPassword}")
    x = inputPassword.__str__
    print(x)

buttonLogin = ctk.CTkButton(page, text="Login!", command="login").grid(column=0, columnspan=2)




### MAKE IT AGAIN 
'''
frameMenu = ctk.CTkFrame(page, height=200, width=600)
frameMenu.pack()
#next
loginFrame = tk.LabelFrame(frameMenu, text="Login", bd=5, relief="ridge")
loginFrame.grid(row=0, column=0, sticky="W", padx=20, pady=20)

label2 = ctk.CTkEntry(loginFrame, placeholder_text="PUT LOGIN HERE").pack(pady=10)

passwordsFrame = tk.LabelFrame(frameMenu, text="Password", bd=5, relief="ridge")
passwordsFrame.grid(row=1, column=0, sticky="W", padx=20, pady=20)

label3 = ctk.CTkEntry(passwordsFrame, placeholder_text="PUT PASSWORD HERE").pack(pady=10)'''


#buttonPrev = ctk.CTkButton(page, text="Previous Page", command=PrevPage, state="disabled")
#buttonPrev.pack(side="left", padx=10, pady=10)
'''
def Quit():
    answer = messageBox.askyesno(title="Quit Confirm", message="Are you sure you want to quit"
    if answer:
        page.destroy()
'''
#buttonQuit = ctk.CTkButton(page, text="QUIT", state="disabled").pack(side="left")

#buttonNext = ctk.CTkButton(page, text="Next Page", command=NextPage)
#buttonNext.pack(side="right", padx=10, pady=10)


page.mainloop()