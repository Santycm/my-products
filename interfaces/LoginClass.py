import tkinter as tk
from tkinter import messagebox
import src.userclass as u

from interfaces import DashClass as dsh
from interfaces import UserRegClass as ur

class Login:
    def __init__(self, window_log):
        self.window_log = window_log
        self.window_log.title("Login")
        self.window_log.geometry("250x300")

        self.lblLog = tk.Label(window_log, text="Login")
        self.lblLog.grid(row=0, pady=(60,20), columnspan=2, sticky='ew')

        self.lblUser = tk.Label(window_log, text="User")
        self.lblUser.grid(row=1, column=0, padx=20)
        self.entUser = tk.Entry(window_log, width=20)
        self.entUser.grid(row=1, column=1, padx=20)

        self.lblPass = tk.Label(window_log, text="Password", pady=20)
        self.lblPass.grid(row=2, column=0, padx=10, pady=(0,30))
        self.entPass = tk.Entry(window_log, width=20, show="*")
        self.entPass.grid(row=2, column=1, pady=(0, 30))

        self.btnLogin = tk.Button(window_log, text='Log In', background='green', foreground='white', command= lambda: userAuth(self.entUser.get(), self.entPass.get(), window_log))
        self.btnLogin.grid(row=3, column=0)

        self.btnCreate = tk.Button(window_log, text='Register new user', background='blue', foreground='white', command=lambda: self.showRegister(window_log))
        self.btnCreate.grid(row=3, column=1)

    def showRegister(self, window_log):
        window_log.destroy()
        root = tk.Tk()
        NewWindow = ur.UserRegister(root)
        root.mainloop

def userAuth(user, password, window_log):
    if u.authUser(user, password):
        root = tk.Tk()
        window_log.destroy()
        NewWindow = dsh.dashboard(root, user)
        root.mainloop()
    else:
        messagebox.showerror(title="ERROR", message="Incorrect user")  

    