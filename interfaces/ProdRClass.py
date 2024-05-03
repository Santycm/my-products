import tkinter as tk
from interfaces import DashClass as dsh
from src import productclass as p
from src import userclass as u

class ProductRegister:
    def __init__(self, window_pr, user):
        self.window_pr = window_pr
        self.user = user
        self.window_pr.title("Register new product")
        self.window_pr.geometry("300x300")

        self.lblAdd = tk.Label(window_pr, text="Add product")
        self.lblAdd.grid(row=0, pady=(60,15), columnspan=2, sticky='ew')

        self.lblDes = tk.Label(window_pr, text="Description", padx=15, pady=10)
        self.lblDes.grid(row=1, column=0, padx=10) 
        self.entDes = tk.Entry(window_pr, width=20)
        self.entDes.grid(row=1, column=1) 

        self.lblPrice = tk.Label(window_pr, text="Price", padx=15, pady=10)
        self.lblPrice.grid(row=2, column=0, padx=10)
        self.entPrice = tk.Entry(window_pr, width=20)
        self.entPrice.grid(row=2, column=1)

        self.lblStock = tk.Label(window_pr, text="Stock", padx=15, pady=10)
        self.lblStock.grid(row=3, column=0, padx=10) 
        self.entStock = tk.Entry(window_pr, width=20)
        self.entStock.grid(row=3, column=1)

        self.btnSubmit = tk.Button(window_pr, text="Submit", background='green', foreground='white', command= lambda: self.productRegister(self.entDes.get(), float(self.entPrice.get()), int(self.entStock.get()), self.user, self.window_pr))
        self.btnSubmit.grid(row=6, column=0, pady=(10,0))

        self.btnReturn = tk.Button(window_pr, text="Return", background='black', foreground='white', command= lambda: self.returnPage(self.window_pr, self.user))
        self.btnReturn.grid(row=6, column=1, pady=(10,0))
    def returnPage(self, window_pr, user):
        window_pr.destroy()

        root = tk.Tk()
        NewWindow = dsh.dashboard(root, user)
        root.mainloop()

    def productRegister(self, description, price, stock, user, window_pr):
        NewProduct = p.product(description, price, stock)
        NewProduct.addToDB(u.getIDUser(user))

        window_pr.destroy()
        root = tk.Tk()

        NewWindow = dsh.dashboard(root, user)
        root.mainloop()

