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

#___________________________GLOBAL VARIABLES___________________________
active = ""

#____________________________PASSWORDS_______________________________
# 1. username: 010101010101 password: qwertya
# 2. username: 020202020202 password: qwertyb
# 3. username: 030303030303 password: qwertyc
# 4. username: 040404040404 password: qwertyd
# 5. username: 050505050505 password: qwertye
# 6. username: 060606060606 password: qwertyf
# 7. username: 070707070707 password: qwertyg
# 8. username: 080808080808 password: qwertyh
# 9. username: 090909090909 password: qwertyi
# 10. username: 101010101010 password: qwertyj
# 11. username: 111111111111 password: qwertyk
# 12. username: 121212121212 password: qwertyl
# 13. username: 131313131313 password: qwertym
# 14. username: 141414141414 password: qwertyn
# 15. username: 151515151515 password: qwertyo
# 16. username: 161616161616 password: qwertyp
# 17. username: 171717171717 password: qwertyq
# 18. username: 181818181818 password: qwertyr
# 19. username: 191919191919 password: qwertys
# 20. username: 012345678910 password: qwertyt
# 21. (ADMIN) username:admin password: admin

#___________________________FUNCTIONS_________________________________

#********DATABASE FUNCTIONS********
#function to create a table named  "user", since data is preloaded, no need to call this function
def newTableUser():

    # connecting to the database
    connection = sqlite3.connect("mysejahtera_0.5.db")
    # cursor
    cursor = connection.cursor()
  
    # SQL command to create table "user" in the database
    command = """CREATE TABLE user (
   "ICnum" TEXT NOT NULL,
	"password" TEXT NOT NULL,
	"name" TEXT NOT NULL,
	"age" INTEGER NOT NULL,
	"phone" TEXT NOT NULL,
	"address" TEXT NOT NULL,
	"postcode" TEXT NOT NULL,
	"gender" INTEGER,
	"risk" INTEGER,
	"status" INTEGER,
	"userStatus" INTEGER,
    PRIMARY KEY("ICnum")
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
    "idPPV" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "vaccineBrand" TEXT NOT NULL,
    "patientsPerDay" INTEGER NOT NULL,
    PRIMARY KEY("idPPV")
    );"""

    cursor.execute(command)
    connection.commit()
    connection.close()

#function to create a table named  "covid", since data is preloaded, no need to call this function
def newTableCOVID():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
  
    # SQL command to create table "covid" in the database
    command = """CREATE TABLE covid (
    "date" TEXT NOT NULL,
    "cases" INTEGER NOT NULL,
    "recoveries" INTEGER NOT NULL,
    "deaths" INTEGER NOT NULL,
    "active" INTEGER NOT NULL,
    "cumulative" INTEGER NOT NULL,
    "tests" INTEGER NOT NULL,
    PRIMARY KEY("date")
    );"""

    cursor.execute(command)
    connection.commit()
    connection.close()

#function to create a table named  "vaccinations", since data is preloaded, no need to call this function
def newTableVaccinations():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
  
    # SQL command to create table "vaccinations" in the database
    command = """CREATE TABLE vaccinations(
    "date" TEXT NOT NULL
    "1dose" INTEGER NOT NULL,
    "2dose" INTEGER NOT NULL,
    "booster" INTEGER NOT NULL,
    "total1dose" INTEGER NOT NULL,
    "total2dose" INTEGER NOT NULL,
    "totalbooster" INTEGER NOT NULL,
    "grandtotal" INTEGER NOT NULL,
    PRIMARY KEY("date")
    );"""

    cursor.execute(command)
    connection.commit()
    connection.close()

#function to add data into table "ppv"
def addDataPPV():
    print

#function to add data into table "covid"
def addDataCOVID():
    print

#function to add data into table "vaccinations"
def addDataVaccinations():
    print

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

#function to export all data in table "covid"
def dataExportCOVID():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "covid"
    cursor.execute("SELECT * FROM covid")
    output = cursor.fetchall()
    for i in output:
       print(i)
    connection.close()

#function to export all data in table "vaccinations"
def dataExportVaccinations():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "vaccinations"
    cursor.execute("SELECT * FROM vaccinations")
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

    print("Signup successful, you will be redirected shortly.")
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

#function for users to assess risk
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
    print("Your updated risk is", risk)

    #updates the risk of the user in the database 
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    statement = f"UPDATE user SET risk='{risk}' WHERE ICnum = '{active}';"
    cursor.execute(statement)
    connection.commit()
    connection.close()

    #redirect back to main menu
    print("Your risk assessment has been successfully completed, you will be redirected back to the main menu shortly.")
    mainMenu()

#function for users to update status (UNTESTED)
def status():
    global active
    status = 0
    print("----------------------------COVID 19 STATUS----------------------------\n")
    print("Please report your current COVID-19 status here.")
    print("Please type out your current status whether it be 'No symptoms', 'Casual contact', 'Close contact', 'Person Under Surveillance', 'Home Quarantine Order',  'COVID-19 positive, mild symptoms' or 'COVID-19 positive, severe symptoms'\n")
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    while True:
        enter = str(input("Please enter status: "))
        if enter == "No symptoms":
            status = 1
            break
        elif enter == "Casual contact":
            status = 2
            break
        elif enter == "Close Contact":
            status = 3
            break
        elif enter == "Person Under Surveillance":
            status = 4
            break
        elif enter == "Home Quarantine Order":
            status = 5
            break
        elif enter == "COVID-19 positive, mild symptoms":
            status = 6
            break
        elif enter == "COVID-19 positive, severe symptoms":
            status = 7
            break
        else:
            print("Unknown status.")

    #updates the status of the user in the database 
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    statement = f"UPDATE user SET status='{status}' WHERE ICnum = '{active}';"
    cursor.execute(statement)
    connection.commit()
    connection.close()

    #redirect back to main menu
    print("Your status has been successfully updated, you will be redirected back to the main menu shortly.")
    mainMenu()

def vaccine():
    print("This will be vaccination")

def updates():
    print("This will be COVID-19 updates")

def personalInfo():
    print("This will be user's personal info")
            
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

#function to select which table to export
def exports():
    instruct = str(input("What table would you like to export? (user, ppv, covid, vaccination)"))
    while True:
        if instruct == "user":
            dataExportUser()
            break
        elif instruct == "ppv":
            dataExportPPV()
            break
        elif instruct == "covid":
            dataExportCOVID()
            break
        elif instruct == "vaccination":
            dataExportVaccinations()
            break
        else:
            print("Unknown command.")

#function to add tables
def newTable():
    instruct = str(input("What table would you like to add? (user, ppv, covid, vaccination)"))
    while True:
        if instruct == "user":
            newTableUser()
            print ("Table 'user' with primary key ICnum with attributes ICnum, password, name, age, phone, address, postcode, gender, risk, status, userStatus created.")
            break
        elif instruct == "ppv":
            newTablePPV()
            print ("Table 'ppv' with primary key idPPV with attributes name, location, vaccineBrand, patientsPerDay created.")
            break
        elif instruct == "covid":
            newTableCOVID()
            print ("Table 'covid' with primary key date with attributes cases, recoveries, deaths, active, cumulative, tests created.")
            break
        elif instruct == "vaccination":
            newTableVaccinations()
            print ("Table 'vaccinations' with primary key date with attributes 1dose, 2dose, booster, total1dose, total2dose, totalbooster, grandtotal created.")
            break
        else:
            print("Unknown command.")

#function to select which table to add data to
def addData():
    instruct = str(input("What table would you like to add data to? (ppv, covid, vaccination)"))
    while True:
        if instruct == "ppv":
            addDataPPV()
            break
        elif instruct == "covid":
            addDataCOVID()
            break
        elif instruct == "vaccination":
            addDataVaccinations()
            break
        else:
            print("Unknown command.")

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