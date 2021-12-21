# *********************************************************
# Program: TL4V_G2.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL1
# Trimester: 2115
# Year: 2021/22 Trimester 1
# Member_1: ID | NAME | PHONES
# Member_2: ID | NAME | PHONES
# Member_3: ID | NAME | PHONES
# Member_4: ID | NAME | PHONES
# *********************************************************
# Task Distribution
# Member_1:
# Member_2:
# Member_3:
# Member_4:
# *********************************************************

#_________________________MODULE IMPORTS_____________________________
#sqlite3 for usage of SQLite tables and database to store data
import sqlite3
#hashlib for hashing of passwords
import hashlib
#math for mathematical operations
import math

#_________________________GLOBAL VARIABLES____________________________
active = ""

#_________________________PASSWORDS____________________________
# (ADMIN) username:admin password: admin
# username: 030725101499 password:abc123
#
#
#
#
#
#

#__________________________FUNCTIONS________________________________

#********DATABASE FUNCTIONS********
#function to create a table named  "user", since data is preloaded, no need to call this function
def newTableUser():

    # connecting to the database
    connection = sqlite3.connect("mysejahtera_0.5.db")
    # cursor
    cursor = connection.cursor()
  
    # SQL command to create table "user" in the database
    command = """CREATE TABLE user (
    ICnum VARCHAR (13) PRIMARY KEY NOT NULL,
    password VARCHAR (128) NOT NULL,
    name VARCHAR (100) NOT NULL,
    age TINYINT(3) NOT NULL,
    phone VARCHAR (12) NOT NULL, 
    address VARCHAR (200) NOT NULL,
    postcode VARCHAR (6) NOT NULL,
    gender TINYINT(1),
    risk TINYINT(2),
    status TINYINT(2),
    userStatus TINYINT(1)
    );"""
    
    # execute the statement
    cursor.execute(command)
    #save the data
    connection.commit()
    # close the connection
    connection.close()

#function to create a table named  "ppv", since data is preloaded, no need to call this function
def newTablePPV():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
  
    # SQL command to create table "ppv" in the database
    command = """CREATE TABLE user (
    ICnum VARCHAR (13) PRIMARY KEY NOT NULL,
    password VARCHAR (128) NOT NULL,
    name VARCHAR (100) NOT NULL,
    age TINYINT(3) NOT NULL,
    phone VARCHAR (12) NOT NULL, 
    address VARCHAR (200) NOT NULL,
    postcode VARCHAR (6) NOT NULL,
    gender TINYINT(1),
    risk TINYINT(2),
    status TINYINT(2),
    userStatus TINYINT(1)
    );"""

    cursor.execute(command)
    connection.commit()
    connection.close()

#function to export all data in table "user"
def dataExportUser():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "user"
    cursor.execute("SELECT * FROM user")
    output = cursor.fetchall()
    for i in output:
       print(i)
    connection.close()

#function to export all data in table "ppv"
def dataExportPPV():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "user"
    cursor.execute("SELECT * FROM ppv")
    output = cursor.fetchall()
    for i in output:
       print(i)
    connection.close()

#********USER INTERACTION FUNCTIONS********
#function to input new user's data into table "user"
def signup():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Inputs from the user
    print("Please enter the following details: ")
    ICnum = str(input("IC number (without dash): "))
    rawPassword = str(input("Password: "))
    #SHA-512 hashing of password
    hash_object = hashlib.sha512(rawPassword.encode())
    password = hash_object.hexdigest()
    name = str(input("Full Name: "))
    age = int(input("Age: "))
    phone = str(input("Phone number (without dash): "))
    address = str(input("Address: "))
    postcode = str(input("Postcode: "))
    gender = int(input("Gender (0 for male, 1 for female): "))
  
    #Insert values above entered from user
    cursor.execute("""
    INSERT INTO user (ICnum, name, password, age, phone, address, postcode, gender, userStatus)
    VALUES (?,?,?,?,?,?,?,?,?)
    """, (ICnum, name, password, age, phone, address, postcode, gender, 0))

    #To save the changes in the files
    connection.commit()
    connection.close()

    print("Signup Successful")
    #Redirect to login page
    login()

#function to login for normal users
def login():
    global active
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    while True:
        ICnum = str(input("Enter IC number: "))
        rawPassword = str(input("Password: "))
        hash_object = hashlib.sha512(rawPassword.encode())
        password = hash_object.hexdigest()
        statement = f"SELECT ICnum from user WHERE ICnum='{ICnum}' AND password = '{password}';"
        cursor.execute(statement)
        if not cursor.fetchone():  # An empty result evaluates to False.
            print("Login failed, please try again.")
        else:
            print("Welcome!")
            active = ICnum
            connection.close()
            mainMenu()
            return active

#function to login for admin
def loginAdmin():
    ICnum = str(input("Enter IC number: "))
    rawPassword = str(input("Password: "))
    hash_object = hashlib.sha512(rawPassword.encode())
    password = hash_object.hexdigest()
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    statement = f"SELECT ICnum from user WHERE ICnum='{ICnum}' AND password = '{password}' AND userStatus = 1;"
    cursor.execute(statement)
    if not cursor.fetchone():
        print("Login failed, please try again.")
    else:
        print("Welcome!")
        mainMenuAdmin()
    connection.close()

def risk():
    print("abc")

def status():
    print

#********MENUS FUNCTIONS********
def mainMenu():
    global active
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT name FROM user WHERE ICnum='{active}'")
    oldName = str(cursor.fetchall())
    #for removing unnecessary characters
    list=['[','(',']',')','.',"'"] 
    name ="".join(i for i in oldName if i not in list) 

    print("Welcome", name, "please type a number.")
    print("Type 1 for vaccination appointments.")
    print("Type 2 for risk assesment.")
    print("Type 3 for current COVID-19 updates.")
    print("Type 4 for updating personal information.")

    connection.close()

def mainMenuAdmin():
    print("Welcome admin.")
    print("Type 1 for user management.")
    print("Type 2 for PPV management.")
    print("Type 3 for vaccination management.")
    print("Type 4 for user risk management.")
    print("Type 5 for data exports.")

def startMenu():
    print("-------------------------------------------------------------")
    print("Welcome to MySejahtera 0.5!")
    print("Enter 1 for login.")
    print("Enter 2 for sign up.")
    print("Enter 3 for admin login.")
    while True:
        num = int(input("Enter a number: "))
        print("-------------------------------------------------------------")
        if num == 1:
            login()
            break
        elif num == 2:
            signup()
            break
        elif num == 3:
            loginAdmin()
            break
        else:
            print("invalid")

#*****MAIN FUNCTION******
def main():
    startMenu()
    login()
    log = login()
    #loginUser = login()
    #loginUser = login()
    #if log == True:
    #    mainMenu()

main()