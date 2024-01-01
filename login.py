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

#next
loginFrame = tk.LabelFrame(page, text="Login", bd=5)
loginFrame.pack(page, row=0, column=0, padx=20, pady=20)

label2 = ctk.CTkEntry(loginFrame, placeholder_text="PUT IT HERE")
#label3 = ctk.CTkEntry(page, placeholder_text="PUT IT HERE").pack()



#passwordsFrame = ctk.CTkFrame(page, text="Password", background=5)


buttonPrev = ctk.CTkButton(page, text="Previous Page", command=PrevPage, state="disabled")
buttonPrev.pack(side="left", padx=10, pady=10)

buttonNext = ctk.CTkButton(page, text="Next Page", command=NextPage)
buttonNext.pack(side="right", padx=10, pady=10)


page.mainloop()