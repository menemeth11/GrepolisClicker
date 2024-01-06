from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
#***
test1, test2 = "12", "1234" #temp for4 before DB 
def login():
    login = textLogin.get()
    passw = textPassword.get()
    #print(f'Login: {login}, Password: {passw}')
    if(login == test1 and passw == test2):
        page.destroy()
        import main
    elif login != test1 and passw != "":
        messagebox.showerror("Error","User does not exist!")
    elif login != "" and passw != test2:
        messagebox.showerror("Error","Wrong password!")
    else : #login == "" or passw == "":
        messagebox.showerror("Error","Complete all data!")
    

#***    
page = ctk.CTk()
page.geometry("470x260")
page.title("Clicker by Menemeth11")
page.resizable(False, False)

label = ctk.CTkLabel(page, text="Grepo Clicker", font=("Segoe UI", 50, "bold"), text_color="Green").grid(column=0, row=0,columnspan= 2, sticky="we")
label1 = ctk.CTkLabel(page, text="by Menemeth11", font=("Segoe UI", 10, "bold"), text_color="Green").grid(column=0, row=1,columnspan= 2, sticky="n")

menuFrame = ctk.CTkFrame(page, width=450, height=80, border_width=3, border_color="green").grid(column=0, row=2,columnspan= 2,rowspan=2, padx=10, pady=10)

textLogin = ctk.StringVar()
labelLogin = ctk.CTkLabel(menuFrame, text="LOGIN:", text_color="green", font=("Segoe UI", 15, "bold"), bg_color="#2b2b2b").grid(column=0, row=2,sticky="s")
inputLogin = ctk.CTkEntry(menuFrame, placeholder_text="Put Your login here", width=180, textvariable=textLogin).grid(column=0, row=3, sticky="n")

textPassword = ctk.StringVar()
labelPassword = ctk.CTkLabel(menuFrame, text="PASSWORD:", text_color="green", font=("Segoe UI", 15, "bold"), bg_color="#2b2b2b").grid(column=1, row=2,sticky="s")
inputPassword = ctk.CTkEntry(menuFrame, placeholder_text="Put Your password here", width=180, show="*", textvariable=textPassword).grid(column=1, row=3, sticky="n")

buttonLogin = ctk.CTkButton(page, text="Login!", command=login, width=300, height=50).grid(column=0, columnspan=2)

page.mainloop()



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


