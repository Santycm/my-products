import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from interfaces import LoginClass as lg
from src import userclass as u
from src import productclass as p
from interfaces import ProdRClass as pr

class dashboard:
    def __init__(self, window_dsh, user):
        self.window_dsh = window_dsh
        self.user = user
        self.window_dsh.title("Dashboard")
        self.window_dsh.geometry("900x470")

        self.lblUser = tk.Label(window_dsh, text=f"¡WELCOME {u.getNameUser(user)}!", font=("Arial", 20, "bold"))
        self.lblUser.grid(row=0, pady=(60,15), columnspan=4, sticky='ew')

        self.button = tk.Button(window_dsh, text="LOG OUT", background='red', foreground='white', command= lambda: self.returnLogin(self.window_dsh))
        self.button.grid(row=1, column=0, padx=(400,400), pady=(0,15), columnspan=4, sticky='ew')

        self.columnTitles = {"1": "ID", "2": "Description", "3": "Price", "4": "Stock"}

        self.table = ttk.Treeview(window_dsh, columns=("ID", "Description", "Price", "Stock"), show="headings")
        self.table.heading("ID", text=self.columnTitles.get("1"))
        self.table.heading("Description", text=self.columnTitles.get("2"))
        self.table.heading("Price", text=self.columnTitles.get("3"))
        self.table.heading("Stock", text=self.columnTitles.get("4"))
        
        self.loadProducts(u.getIDUser(user), self.table)

        self.btnInsert = tk.Button(window_dsh, text="INSERT", background='green', foreground='white', command=lambda: self.showForm(self.window_dsh, self.user))
        self.btnInsert.grid(row=3, column=0, pady=(15,0))

        self.btnRemove = tk.Button(window_dsh, text="REMOVE", background='red', foreground='white', command=lambda: self.removeProduct(self.table, self.user))
        self.btnRemove.grid(row=3, column=1, pady=(15,0))

        self.btnExport = tk.Button(window_dsh, text="EXPORT", background='orange', foreground='white', command=lambda: self.exportProducts(self.user))
        self.btnExport.grid(row=3, column=2, pady=(15,0))

    def loadProducts(self, iduser, table):
        products = p.getProducts(iduser)
        for product in products:
            table.insert("", tk.END, values=product)
        
        table.grid(row=2, column=0, padx=(15,15), pady=(15,0), columnspan=4, sticky='ew')
        

    def returnLogin(self, window_dsh):
        window_dsh.destroy()
        root = tk.Tk()
        NewWindow = lg.Login(root)

        root.mainloop()

    def showForm(self, window_dsh, user):
        window_dsh.destroy()
        root = tk.Tk()
        NewWindow = pr.ProductRegister(root, user)
        root.mainloop()

    def removeProduct(self, table, user):
        if table.selection():
            selected = table.selection()[0]
            values_row = table.item(selected)['values']
            table.delete(selected)
            p.removeProduct(values_row[0], u.getIDUser(user))
        else:
            messagebox.showwarning("ALERT", "You must select a row")

    def exportProducts(self, user):
        with open("INVENTORY.txt", "w") as f:
            products = p.getProducts(u.getIDUser(user))
            plist = list(products)

            productslist=[]

            for product in plist:
                productslist.append(list(product))

            f.write("________________________________________________\n")
            f.write("|ID |DESCRIPTION              |PRICE     |STOCK|\n")
            f.write("________________________________________________\n")
            for product in productslist:
                formatr = ""
                for value, width in zip(product, [4, 25, 10, 5]):
                    formatp = f"{value:<{width}}"
                    formatr = formatp +"|"
                    f.write(formatr)
                f.write("\n") 

            f.write("________________________________________________\n")
        messagebox.showinfo("EXPORT", "Successfully")


