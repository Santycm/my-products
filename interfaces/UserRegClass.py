from tkinter import messagebox
import tkinter as tk
from src import userclass as u

from interfaces import LoginClass as lg

class UserRegister:
    def __init__(self, window_reg):
        self.window_reg = window_reg
        self.window_reg.title("Register new user")
        self.window_reg.geometry("300x420")

        self.lblLog = tk.Label(self.window_reg, text="Register new user")
        self.lblLog.grid(row=0, pady=(60,15), columnspan=2, sticky='ew')

        self.lblName = tk.Label(self.window_reg, text="Name", padx=15, pady=10)
        self.lblName.grid(row=1, column=0, padx=10) 
        self.entName = tk.Entry(self.window_reg, width=20)
        self.entName.grid(row=1, column=1) 

        self.lblLast = tk.Label(self.window_reg, text="Last Name", padx=15, pady=10)
        self.lblLast.grid(row=2, column=0, padx=10)
        self.entLast = tk.Entry(self.window_reg, width=20)
        self.entLast.grid(row=2, column=1)

        self.lblTel = tk.Label(self.window_reg, text="Telephone", padx=15, pady=10)
        self.lblTel.grid(row=3, column=0, padx=10) 
        self.entTel = tk.Entry(self.window_reg, width=20)
        self.entTel.grid(row=3, column=1)
        self.lblTelC = tk.Label(self.window_reg, text="MAX: 10 Caracters", font=("Arial", 8, "bold"))
        self.lblTelC.grid(row=4, column=1)

        self.lblEmail = tk.Label(self.window_reg, text="Email", padx=15, pady=10)
        self.lblEmail.grid(row=5, column=0, padx=10) 
        self.entEmail = tk.Entry(self.window_reg, width=20)
        self.entEmail.grid(row=5, column=1)
        self.lblEmailC = tk.Label(self.window_reg, text="Must have @example.com", font=("Arial", 8, "bold"))
        self.lblEmailC.grid(row=6, column=1)

        self.lblPass = tk.Label(self.window_reg, text="Password", padx=15, pady=10)
        self.lblPass.grid(row=7, column=0, padx=10) 
        self.entPass = tk.Entry(self.window_reg, width=20, show="*")
        self.entPass.grid(row=7, column=1)
        self.lblPassC = tk.Label(self.window_reg, text="Must have '@ or *'", font=("Arial", 8, "bold"))
        self.lblPassC.grid(row=8, column=1)

        self.btnSubmit = tk.Button(window_reg, text="Submit", background='green', foreground='white', command= lambda: self.userRegister(self.entName.get(), self.entLast.get(), self.entTel.get(), self.entEmail.get(), self.entPass.get(), self.window_reg, self.entTel, self.entEmail, self.entPass))
        self.btnSubmit.grid(row=9, column=0, pady=(10,0))

        self.btnReturn = tk.Button(window_reg, text="Return Login", background='black', foreground='white', command= lambda: self.returnLogin(self.window_reg))
        self.btnReturn.grid(row=9, column=1, pady=(10,0))

    def userRegister(self, name, lastname, telephone, email, password, window_reg, entTel, entEmail, entPass):
        if self.correctForm(telephone, email, password, window_reg, entTel, entEmail, entPass):
            NewUser = u.user(name, lastname, telephone, email, password)
            if NewUser.regUser():
                messagebox.showinfo(title="REGISTRADO", message=f"Se ha registrado correctamente {NewUser.AssignUser()}")
                window_reg.destroy()
                
                root = tk.Tk()
                NewWindow = lg.Login(root)
                root.mainloop()
            else:
                messagebox.showerror(title="ERROR", message="Already username exists")

    def correctForm(self, telephone, email, password, window_reg, entTel, entEmail, entPass):
        checkTelephone = False
        checkEmail1 = False
        checkEmail2 = False
        checkPassword = False
        
        if 0 < len(telephone) < 11:
            checkTelephone = True
        else:
            entTel.config(background='red')
            entTel.grid(row=3, column=1)

        for i in range(len(email)):
            if email[i] == '@':
                checkEmail1 = True
                break
        for i in range(len(email)):
            if email[i] == '.':
                checkEmail2 = True
                break

        if checkEmail1 == False:
            entEmail.config(background='red')
            entEmail.grid(row=5, column=1)

        if checkEmail2 == False:
            entEmail.config(background='red')
            entEmail.grid(row=5, column=1)

        for i in range(len(password)):
            if password[i] == '@' or password[i] == '*':
                checkPassword = True
        
        if checkPassword == False:
            entPass.config(background='red')
            entPass.grid(row=7, column=1)

        

        if checkTelephone and checkEmail1 and checkEmail2 and checkPassword:
            return True
        else:
            window_reg.mainloop()
            return False

        
    def returnLogin(self, window_reg):
        window_reg.destroy()

        root = tk.Tk()
        NewWindow = lg.Login(root)
        root.mainloop()





    

