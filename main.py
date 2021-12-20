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

import sqlite3

#function to create a table named  "user", since data is preloaded, no need to call this function
def newUserTable():

    # connecting to the database
    connection = sqlite3.connect("mysejahtera0.5.db")
    # cursor
    cursor = connection.cursor()
  
    # SQL command to create a table in the database
    command = """CREATE TABLE user (
    ICnum VARCHAR (13) PRIMARY KEY NOT NULL,
    name VARCHAR (100) NOT NULL,
    age TINYINT(3) NOT NULL,
    phone VARCHAR (12) NOT NULL, 
    address VARCHAR (200) NOT NULL,
    postcode VARCHAR (6) NOT NULL,
    gender TINYTINT(1),
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

#function to imput new user's data into table "user"
def newUser():
    connection = sqlite3.connect("mysejahtera0.5.db")
    cursor = connection.cursor()

    #Inputs from the user
    print("Please enter the following details: ")
    ICnum = str(input("IC number: "))
    name = str(input("Full Name: "))
    age = int(input("Age: "))
    phone = str(input("Phone number: "))
    address = str(input("Address: "))
    postcode = str(input("Postcode: "))
    gender = int(input("Gender (0 for male, 1 for female): "))
  
    # SQL command to insert data in table "user"
   # command = 
  
    cursor.execute("""
    INSERT INTO user (ICnum, name, age, phone, address, postcode, gender)
    VALUES (?,?,?,?,?,?,?)
    """, (ICnum, name, age, phone, address, postcode, gender))

    #To save the changes in the files.
    connection.commit()

    connection.close()

def dataExport():
    connection = sqlite3.connect("mysejahtera0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "user"
    cursor.execute("SELECT * FROM user")
    output = cursor.fetchall()
    for i in output:
       print(i)
    connection.close()