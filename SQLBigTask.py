import sqlite3
import  random
import tkinter as tk

db = sqlite3.connect("./Imazon.db")

db.execute("PRAGMA foreign_keys = ON")



db.commit()
db.close()

class Database:

    databaseRef: str

    def __init__(self, givenDatabaseRef: str):

        self.databaseRef = givenDatabaseRef

    def createTables(self):
        db = sqlite3.connect("./Imazon.db")

        db.execute("PRAGMA foreign_keys = ON")

        db.execute("CREATE TABLE IF NOT EXISTS Products ("
                   "ProductID INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "PName TEXT, "
                   "Description TEXT, "
                   "Price INTEGER )")

        db.execute("CREATE TABLE IF NOT EXISTS Customer("
                   "Customer_Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "Username TEXT, "
                   "Password TEXT, "
                   "Email TEXT, "
                   "Contact_Number INTEGER)")

        db.execute("CREATE TABLE IF NOT EXISTS Basket("
                   "ProductID INTEGER, "
                   "Customer_Id INTEGER, "
                   "Quantity INTEGER, "
                   "FOREIGN KEY(ProductID) REFERENCES Products(ProductID), "
                   "FOREIGN KEY(Customer_Id) REFERENCES Customer(Customer_Id), "
                   "PRIMARY KEY(ProductID, Customer_Id)"
                   ")")

        db.commit()
        db.close()


    def insertIntoTable(self, tableName, values: list):

        tempDb = sqlite3.connect(self.databaseRef)

        if tableName == "Products":
            tempDb.execute("INSERT INTO Products(PName, Description, Price) VALUES(?,?,?)",
                            values)

        elif tableName == "Customer":
            tempDb.execute("INSERT INTO Customer(Username, Password, Email, Contact_Number) VALUES(?,?,?,?)",
                            values)

        elif tableName == "Basket":
            try:
                tempDb.execute("INSERT INTO Basket(ProductID, Customer_Id, Quantity) VALUES(?,?,?)",
                               values)

            except sqlite3.IntegrityError:
                quantity = tempDb.execute("SELECT Quantity FROM Basket "
                                          "WHERE ProductID = ?"
                                          "AND Customer_Id = ?", [values[0], values[1]])
                quantity = quantity.fetchone()[0]
                quantity += 1
                tempDb.execute("UPDATE Basket SET Quantity = ? "
                           "WHERE ProductID = ?"
                           "AND Customer_Id = ?", [quantity, values[0], values[1]])



        tempDb.commit()
        tempDb.close()

    def getUniqueCustomers(self):

        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT DISTINCT Customer_Id FROM Customer")
        cIds = data.fetchall()
        print(cIds)

    def getUniqueProducts(self):

        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT DISTINCT ProductID FROM Products")
        pIds = data.fetchall()
        print(pIds)










