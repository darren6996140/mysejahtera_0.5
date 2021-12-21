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
# username: 012345678910 password: qwertyabcd
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
    command = """CREATE TABLE ppv (
    idPPV INT (10) PRIMARY KEY NOT NULL,
    name VARCHAR (255) NOT NULL,
    location VARCHAR (6) NOT NULL,
    vaccineBrand VARCHAR (10) NOT NULL,
    patientsPerDay INT (3) NOT NULL,
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
#~~~~~~~~NORMAL USER~~~~~~~~
#function to input new user's data into table "user"
def signup():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Inputs from the user
    print("Please enter the following details: \n")
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
    print("\n----------------------------LOGIN----------------------------\n")
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

def userRisk():
    global active
    risk = 0
    print("----------------------------RISK ASSESSMENT----------------------------\n")
    print("To ensure everyone will receive their COVID-19 vaccine accordingly, you are advised to carry out a risk assesment.")
    print("Your risk will be displayed in a number from 1-5.")
    print("Please answer the following questions truthfully by answering either 'Y' for yes or 'N' for no.\n")

    overseas = str(input("Have you been outside of the country in the past 14 days?\n"))
    if overseas == "Y":
        risk = risk + 0.6
    
    CContact = str(input("Have you been in close contact with any COVID-19 patient in the past 14 days?\n"))
    if CContact == "Y":
        risk = risk + 0.6

    age = str(input("Are you above 60 years old?\n"))
    if age == "Y":
        risk = risk + 0.5

    diabetes = str(input("Are you diabetic?\n"))
    if diabetes == "Y":
        risk = risk + 0.7
    
    hypertension = str(input("Are you diagnosed with high blood pressure or any heart condition?\n"))
    if hypertension == "Y":
        risk = risk + 0.6

    immuneCompromised = str(input("Are you Immunocompromised?\n"))
    if immuneCompromised == "Y":
        risk = risk + 0.5

    obese = str(input("Are you obese? (BMI>35)\n"))
    if obese == "Y":
        risk = risk + 0.6
    
    disease = str(input("Are you diagnosed with any other long term disease such as cancer, high cholesterol, stroke, chronic diseases, etc.?\n"))
    if disease == "Y":
        risk = risk + 0.5

    substance = str(input("Do you take unhealthy substances such as drugs, tobacco products, alcohol, etc.?\n"))
    if substance == "Y":
        risk = risk + 0.4

    pregnant = str(input("Are you pregnant?\n"))
    if pregnant == "Y":
        risk = risk + 0.4

    print("Please state your occupation.")
    print("Type 5 if you are a frontline worker, 4 if your job requires face to face meets, 3 if your job requires you to move around, 2 if your job can be done at home and 1 if you are unemployed/staying at home full time.")
    
    while True:    
        job = int(input("Enter here: "))
        if job > 0 and job < 6:
            risk = risk + job/10
            print(risk)
            break
        else:
            print("Invalid number, please try again.")
            
    #rounds down the risk to an integer
    risk = math.floor(risk)
    print("Your current risk is", risk)

    #updates the risk of the user in the database 
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    statement = f"UPDATE user SET risk='{risk}' WHERE ICnum = '{active}';"
    cursor.execute(statement)
    connection.commit()
    connection.close()

    return risk

def status():
    print("This will be user status")

def vaccine():
    print("This will be vaccination")

def updates():
    print("This will be COVID-19 updates")

def personalInfo():
    print("This will be user's personal info")

def userManage():
    print("This will be user management")

def PPVManage():
    print("This will be PPV management")

def vaccineManage():
    print("This will be vaccination management")

def riskManage():
    print("This will be user risk analysis")

def updatesManage():
    print("This will manage COVID-19 updates")

def exports():
    print("This will export data")
            
#~~~~~~~~ADMINS~~~~~~~~
#function to login for admin
def loginAdmin():
    print("----------------------------ADMIN LOGIN----------------------------\n")
    ICnum = str(input("Enter ID: "))
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
        connection.close()
        mainMenuAdmin()

#********MENUS FUNCTIONS********
#function for menu when first running the program
def startMenu():
    print("\n-------------------------------------------------------------\n")
    print("Welcome to MySejahtera 0.5!\n")
    print("Enter 1 for login.")
    print("Enter 2 for sign up.")
    print("Enter 3 for admin login.\n")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
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

#function for menu when user successfully login
def mainMenu():
    global active
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT name FROM user WHERE ICnum='{active}'")
    oldName = str(cursor.fetchall())
    #for removing unnecessary characters
    list=['[','(',']',')','.',"'"] 
    name ="".join(i for i in oldName if i not in list) 

    print("----------------------------MAIN MENU----------------------------\n")
    print("Welcome", name, "please type a number.\n")
    print("Type 1 for vaccination appointments.")
    print("Type 2 for risk assesment.")
    print("Type 3 for current COVID-19 updates.")
    print("Type 4 for updating personal information.\n")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
        if num == 1:
            vaccine()
            break
        elif num == 2:
            userRisk()
            break
        elif num == 3:
            updates()
            break
        elif num == 4:
            personalInfo()
            break
        else:
            print("invalid")
    connection.close()

#function for menu when admin logged in
def mainMenuAdmin():
    print("----------------------------ADMIN MENU----------------------------\n")
    print("Welcome admin.")
    print("Type 1 for user management.")
    print("Type 2 for PPV management.")
    print("Type 3 for vaccination management.")
    print("Type 4 for user risk management.")
    print("Type 5 for COVID-19 updates management.")
    print("Type 6 for data exports.")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
        if num == 1:
            userManage()
            break
        elif num == 2:
            PPVManage()
            break
        elif num == 3:
            vaccineManage()
            break
        elif num == 4:
            riskManage()
            break
        elif num == 5:
            updatesManage()
            break
        elif num == 6:
            exports()
            break
        else:
            print("invalid")

#*****MAIN FUNCTION******
def main():
    startMenu()
    login()
    log = login()
    loginUser = login()
    loginUser = login()
    if log ==True:
        mainMenu()

startMenu()