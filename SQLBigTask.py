import sqlite3
import  random
import tkinter as tk


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


    def populateProductsTable(self, db2):
        products = [
            ("Smartphone", "Latest model with 128GB storage", 699.99),
            ("Microsoft Surface Laptop 13.8-inch", "Snapdragon X Plus/Elite, 13.8-inch touchscreen, up to 32GB RAM, 1TB SSD", 999.99),
            ("Microsoft Surface Laptop 15-inch", "Snapdragon X Elite, 15 touchscreen, up to 64GB RAM, 1TB SSD", 999.99),
            ("Tablet", "10-inch screen, 64GB storage", 329.99),
            ("Smartwatch", "Fitness tracking and notifications", 199.99),
            ("Wireless Earbuds", "Noise-cancelling, Bluetooth 5.0", 149.99),
            ("Gaming Console", "Next-gen console with 1TB storage", 499.99),
            ("4K TV", "55-inch Ultra HD Smart TV", 799.99),
            ("Bluetooth Speaker", "Portable with 12-hour battery life", 89.99),
            ("External Hard Drive", "2TB USB 3.0", 79.99),
            ("Gaming Mouse", "RGB lighting, 16000 DPI", 59.99),
            ("Mechanical Keyboard", "RGB backlit, tactile switches", 129.99),
            ("Drone", "4K camera, 30-minute flight time", 599.99),
            ("Digital Camera", "24MP, 4K video recording", 449.99),
            ("Smart Home Hub", "Voice control for smart devices", 99.99),
            ("VR Headset", "Immersive virtual reality experience", 399.99),
            ("Wireless Charger", "Fast charging for smartphones", 29.99),
            ("Action Camera", "Waterproof, 4K video", 199.99),
            ("E-Reader", "6-inch display, adjustable lighting", 129.99),
            ("Portable Projector", "1080p resolution, compact design", 299.99),
            ("Noise-Cancelling Headphones", "Over-ear, wireless", 249.99),
            ("Smart Thermostat", "Energy-saving, remote control", 149.99),
            ("Electric Scooter", "15-mile range, foldable design", 499.99),
            ("Fitness Tracker", "Heart rate monitor, step counter", 99.99),
            ("Webcam", "1080p HD, built-in microphone", 49.99),
            ("USB-C Hub", "6-in-1 adapter with HDMI and USB ports", 39.99),
        ]

        for product in products:
            db2.insertIntoTable("Products", product)









