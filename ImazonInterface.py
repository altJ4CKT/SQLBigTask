from SQLBigTask import Database
import tkinter as tk
import sqlite3


db1: Database = Database("./Imazon.db")


class ShoppingMenuFrame(tk.Frame):
    searchEntry: tk.Entry

    def __init__(self, windowRef:tk.Tk, oldFrame:tk.Frame):

        if oldFrame is not None:
            oldFrame.destroy()

        super().__init__(windowRef)
        self.SetupLayout()
        self.pack(fill="both", expand=True)

    def SetupLayout(self):
        self.configure(bg="black")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        self.columnconfigure(7, weight=1)

        self.searchEntry = tk.Entry(self, font=["Century Gothic", 20], width=20)
        self.searchEntry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        tk.Button(self, text="Search", command=lambda: self.searchButtonClicked(), 
                  font=["Century Gothic", 20], 
                  width=10).grid(row=0, column=2, padx=5, pady=5)
        
        self.resultsBox = tk.Listbox(self, font=["Century Gothic", 20], width=40, height=20)
        self.resultsBox.grid(row=1, column=0, columnspan=3, rowspan=5, padx=5, pady=5)
        
    def searchButtonClicked(self):
        searchTerm = self.searchEntry.get()

        self.resultsBox.delete(0, tk.END)

        tempDb = sqlite3.connect("./Imazon.db")

        matchingProducts = tempDb.execute("SELECT PName FROM Products "
                                          "WHERE PName LIKE ?",
                                          ['%' + searchTerm + '%'])
        matchingProducts = matchingProducts.fetchall()
        tempDb.commit()
        tempDb.close()

        for product in matchingProducts:
            self.resultsBox.insert(tk.END, product[0])


class RegisterFrame(tk.Frame):
    usernameEntry: tk.Entry
    passwordEntry: tk.Entry
    emailEntry: tk.Entry
    phoneEntry: tk.Entry

    def __init__(self, windowRef: tk.Tk, oldFrame: tk.Frame):

        if oldFrame is not None:
            oldFrame.destroy()

        super().__init__(windowRef)
        self.SetupLayout()
        self.pack(fill="both", expand=True)

    def SetupLayout(self):
        self.configure(bg="#000000")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        tk.Button(self, text="Cancel", command=lambda: LoginRegisterFrame(self.master, self),
                  font=["Century Gothic", 20],
                  width=10).grid(row=5, column=0)
        tk.Button(self, text="Submit", command=lambda: self.submitButtonClicked(),
                  font=["Century Gothic", 20],
                  width=10).grid(row=5, column=4)

        tk.Label(self, text="Username", font=("Century Gothic", 20), width=10).grid(row=0, column=1)
        self.usernameEntry = tk.Entry(self, font=("Century Gothic", 20), width=30)
        self.usernameEntry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self, text="Password", font=("Century Gothic", 20), width=10).grid(row=1, column=1)
        self.passwordEntry = tk.Entry(self, font=("Century Gothic", 20), width=30)
        self.passwordEntry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(self, text="Email", font=("Century Gothic", 20), width=10).grid(row=2, column=1)
        self.emailEntry = tk.Entry(self, font=("Century Gothic", 20), width=30)
        self.emailEntry.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(self, text="Phone", font=("Century Gothic", 20), width=10).grid(row=3, column=1)
        self.phoneEntry = tk.Entry(self, font=("Century Gothic", 20), width=30)
        self.phoneEntry.grid(row=3, column=3, padx=5, pady=5)

    def submitButtonClicked(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()

        db1.insertIntoTable("Customer", [username, password, email, phone])

        tempDb = sqlite3.connect("./Imazon.db")

        cId = tempDb.execute("SELECT Customer_Id FROM Customer "
                              "WHERE Username = ?"
                              "AND Password = ?",
                              [username, password])

        cId = cId.fetchone()[0]

        print(f"Your Customer ID is {cId}")

        tempDb.commit()
        tempDb.close()

        LoginRegisterFrame(self.master, self)


class LoginFrame(tk.Frame):
    usernameEntry: tk.Entry
    passwordEntry: tk.Entry
    cIdEntry: tk.Entry

    def __init__(self, windowRef: tk.Tk, oldFrame: tk.Frame):

        if oldFrame is not None:
            oldFrame.destroy()

        super().__init__(windowRef)
        self.SetupLayout()
        self.pack(fill="both", expand=True)

    def SetupLayout(self):
        self.configure(bg="#000000")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        tk.Button(self, text="Cancel", command=lambda: LoginRegisterFrame(self.master, self),
                 font=["Century Gothic", 20],
                 width=10).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(self, text="Submit", command=lambda: self.submitButtonClicked(),
                  font=["Century Gothic", 20],
                  width=10).grid(row=3, column=4, padx=5, pady=5)

        tk.Label(self, text="Username", font=("Century Gothic", 20), width=40).grid(row=0, column=1)
        self.usernameEntry = tk.Entry(self, font=("Century Gothic", 20), width=30)
        self.usernameEntry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self, text="Password", font=("Century Gothic", 20), width=40).grid(row=1, column=1)
        self.passwordEntry = tk.Entry(self, font=("Century Gothic", 20), width=30)
        self.passwordEntry.grid(row=1, column=3, padx=5, pady=5)

    def submitButtonClicked(self):

        username_ = self.usernameEntry.get()
        password_ = self.passwordEntry.get()

        tempDb = sqlite3.connect("./Imazon.db")

        password = tempDb.execute("SELECT Password FROM Customer "
                                  "WHERE Username = ? ",
                                  [username_])

        password = password.fetchone()[0]

        tempDb.commit()
        tempDb.close()

        if password == password_:
            ShoppingMenuFrame(self.master, self)


class LoginRegisterFrame(tk.Frame):
    def __init__(self, windowRef: tk.Tk, oldFrame: tk.Frame):

        if oldFrame is not None:
            oldFrame.destroy()

        super().__init__(windowRef)
        self.SetupLayout()
        self.pack(fill="both", expand=True)

    def SetupLayout(self):
        self.configure(bg="#FF00FF")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        tk.Button(self, text="Login", command=lambda: LoginFrame(self.master, self), font=["Century Gothic", 20],
                  width=10).grid(row=0, column=0, padx=(10, 5), pady=10)
        tk.Button(self, text="Register", command=lambda: RegisterFrame(self.master, self), font=["Century Gothic", 20],
                  width=10).grid(
            row=0, column=1, padx=(5, 10), pady=10)

class MainProgram(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Main Window")

        self.configure(bg="#ff8000")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        LoginRegisterFrame(self, None)
        self.mainloop()

db1.createTables()
db1.populateProductsTable(db1)

x: MainProgram = MainProgram()

