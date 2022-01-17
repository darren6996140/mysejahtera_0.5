# *********************************************************
# Program: TL4V_G2.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL4
# Trimester: 2115
# Year: 2021/22 Trimester 1
# Member_1: 1211102809 | LIAU KAI ZE | PHONES
# Member_2: 1211102810 | LAI CHENG YUNG | PHONES
# Member_3: 1211102861 | TAN JING YAN | PHONES
# Member_4: 1211103533 | CHONG ZHI XUAN | PHONES
# *********************************************************
# Task Distribution
# Member_1: Core coding of the program
# Member_2: Documentation/Report
# Member_3: Presentation
# Member_4: Program testing
# *********************************************************

#_______________________ACKNOWLEDGEMENTS___________________________
# https://github.com/darren6996140/mysejahtera_0.5
# https://www.geeksforgeeks.org/sql-using-python/
# https://docs.python.org/3/library/hashlib.html
# https://www.sqlite.org/index.html
# https://dba.stackexchange.com/questions/129023/selecting-data-from-another-table-using-a-foreign-key

#_________________________MODULE IMPORTS_____________________________
#sqlite3 for usage of SQLite tables and database to store data
import sqlite3
#hashlib for hashing of passwords
import hashlib
#math for mathematical operations
import math

#___________________________GLOBAL VARIABLES___________________________
active = ""

#____________________________USER DETAILS_______________________________
# 1. username: 010101010101 password: qwertya postcode:41000
# 2. username: 020202020202 password: qwertyb postcode:41000
# 3. username: 030303030303 password: qwertyc postcode:41000
# 4. username: 040404040404 password: qwertyd postcode:41000
# 5. username: 050505050505 password: qwertye postcode:42000
# 6. username: 060606060606 password: qwertyf postcode:42000
# 7. username: 070707070707 password: qwertyg postcode:42000
# 8. username: 080808080808 password: qwertyh postcode:43000
# 9. username: 090909090909 password: qwertyi postcode:43000
# 10. username: 101010101010 password: qwertyj postcode:43000
# 11. username: 111111111111 password: qwertyk postcode:43000
# 12. username: 121212121212 password: qwertyl postcode:43000
# 13. username: 131313131313 password: qwertym postcode:43000
# 14. username: 141414141414 password: qwertyn postcode:44000
# 15. username: 151515151515 password: qwertyo postcode:44000
# 16. username: 161616161616 password: qwertyp postcode:44000
# 17. username: 171717171717 password: qwertyq postcode:44000
# 18. username: 181818181818 password: qwertyr postcode:44000
# 19. username: 191919191919 password: qwertys postcode:45000
# 20. username: 012345678910 password: qwertyt postcode:45000
# 21. (ADMIN) username:admin password: admin

#_________________________POSTCODES AND PPV____________________________
#ASSUME ALL POSTCODES and PPV ARE FAKE AND START WITH NUMBER 4 AT THE FRONT
#ASSUME 1 POSTCODES ONLY HAS 1 PPV, SO POSTCODE IS PRIMARY KEY
#41000 Shah Alam [Ideal Convention Center (IDCC), Shah Alam] (capacity of 1)
#42000 Sungai Long [Sungai Long Specialist Hospital, Sungai Long] (capacity of 2)
#43000 Kajang [The MINES Convention Center, Seri Kembangan] (capacity of 3)
#44000 Kuala Lumpur [Bukit Jalil Stadium, Bukit Jalil] (capacity of 5)
#45000 Petaling Jaya [Dewan Sivik MBPJ, Petaling Jaya] (capacity of 2)

#_________________________VACCINATIONS____________________________
# if consent = 0, user has not seen the consent page
#if consent = 1, user consented and will not see the consent page again
#if consent = 2, user did not consent and will not see the consent page again
#if notify = 1 and confirmation = 0, user did not see the confirm page
#if notify = 1 and confirmation = 1, user confirmed and will be assumed vaccinated and notify will automatically go back to 0
#if notify = 1 and confirmation = 2, user did not confirm and will be given a new appointment, notify will automatically go back to 0
#if notify = 0 and confirmation = 0, appointment did not arrive
#if notify = 0 and confirmation = 1, user will be assumed confirmed and vaccinated and vaccinationStatus will return 1, meaning fully vaccinated
#if notify = 0 and confirmation = 2, user is waiting for appointment

#___________________________FUNCTIONS_________________________________
#*************************DATABASE FUNCTIONS*************************
#>>>>>>>>>>>>>CREATING TABLES>>>>>>>>>>>>>
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
	"postcode" INTEGER NOT NULL,
	"gender" INTEGER,
	"risk" INTEGER,
	"status" INTEGER,
    "vaccinationStatus" INTEGER,
    "consent" INTEGER NOT NULL,
	"userStatus" INTEGER,
    PRIMARY KEY("ICnum")
    );"""
    
    # execute the statement
    cursor.execute(command)
    #save the data
    connection.commit()
    # close the connection
    connection.close()
    print("Table 'user' with primary key 'ICnum' with attributes 'password', 'name', 'age', 'phone', 'address', 'postcode', 'gender', 'risk', 'status', 'vaccinationStatus', 'consent', 'userStatus' created.")
    userManage()

#function to create a table named  "ppv", since data is preloaded, no need to call this function
def newTablePPV():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
  
    command = """CREATE TABLE ppv (
    "postcode" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "vaccineBrand" TEXT NOT NULL,
    "patientsPerDay" INTEGER NOT NULL,
    PRIMARY KEY("postcode")
    );"""

    cursor.execute(command)
    connection.commit()
    connection.close()
    print ("Table 'ppv' with primary key 'postcode' with attributes 'name', 'location', 'vaccineBrand', 'patientsPerDay' created.")
    PPVManage()

#function to create a table named  "vaccinations", since data is preloaded, no need to call this function (datetime format: YYYYMMDDHHMM)
def newTableVaccinations():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
  
    command = """CREATE TABLE vaccinations(
    "id" INTEGER NOT NULL,
    "datetime" TEXT NOT NULL,
    "ICnum" TEXT NOT NULL,
    "postcodePPV" INTEGER NOT NULL,
    "notify" INTEGER NOT NULL,
    "confirmation" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY(ICnum) REFERENCES user(ICnum)
    FOREIGN KEY(postcodePPV) REFERENCES ppv(postcode)
    );"""

    cursor.execute(command)
    connection.commit()
    connection.close()
    print("Table 'vaccinations' with primary key 'id' autoincrementing with attributes 'datetime', 'icnum' as foreign key to table 'user', 'postcode' as foreign key to table 'ppv', 'notify', 'confirmation'' created.")
    vaccineManage()

#function to create a table named  "covidstats", since data is preloaded, no need to call this function
def newTableCOVIDStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    command = """CREATE TABLE covidstats (
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
    print ("Table 'covidstats' with primary key 'date' with attributes 'cases', 'recoveries', 'deaths', 'active', 'cumulative', 'tests' created.")
    covidStatsManage()

#function to create a table named  "vaccinationstats", since data is preloaded, no need to call this function
def newTableVaccinationStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
  
    command = """CREATE TABLE vaccinationstats(
    "date" TEXT NOT NULL,
    "dose1" INTEGER NOT NULL,
    "dose2" INTEGER NOT NULL,
    "booster" INTEGER NOT NULL,
    "totaldose1" INTEGER NOT NULL,
    "totaldose2" INTEGER NOT NULL,
    "totalbooster" INTEGER NOT NULL,
    "grandtotaate")l" INTEGER NOT NULL,
    PRIMARY KEY("d
    );"""

    cursor.execute(command)
    connection.commit()
    connection.close()
    print ("Table 'vaccinationstats' with primary key date with attributes 'dose1', 'dose2', 'booster', 'totaldose1', 'totaldose2', 'totalbooster', 'grandtotal' created.")
    vaccinationStatsManage()

#>>>>>>>>>>>>>ADDING DATA>>>>>>>>>>>>>
#function to add data into table "ppv"
def addDataPPV():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    postcode = int(input("Postcode: "))
    name = str(input("Name: "))
    location = str(input("Location: "))
    vaccineBrand = str(input("Vaccine Brand: "))
    patientsPerDay = int(input("Patients Per Day: "))
  
    #insert into table from user input
    cursor.execute("""
    INSERT INTO ppv (postcode, name, location, vaccineBrand, patientsPerDay)
    VALUES (?,?,?,?,?)
    """, (postcode, name, location, vaccineBrand, patientsPerDay))

    connection.commit()
    connection.close()
    print("PPVs added, redirecting back to PPV management shortly\n")
    PPVManage()

#function to add data into table "covidstats"
def addDataCOVIDStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    date = str(input("Date: "))
    cases = int(input("Cases: "))
    recoveries = int(input("Recoveries: "))
    deaths = int(input("Deaths: "))
    active = int(input("Active Cases: "))
    cumulative  = int(input("Cumulative Cases: "))
    tests  = int(input("Tests Done: "))

    cursor.execute("""
    INSERT INTO covidstats (date, cases, recoveries, deaths, active, cumulative, tests)
    VALUES (?,?,?,?,?,?,?)
    """, (date, cases, recoveries, deaths, active, cumulative, tests))

    connection.commit()
    connection.close()
    print("COVID-19 statistics added, redirecting back to COVID-19 stats management shortly.")
    covidStatsManage()

#function to add data into table "vaccinationstats"
def addDataVaccinationStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    date = str(input("Date: "))
    dose1 = int(input("Dose 1: "))
    dose2 = int(input("Dose 2: "))
    booster = int(input("Booster doses: "))
    totaldose1  = int(input("Total dose 1: "))
    totaldose2  = int(input("Total dose 2: "))
    totalbooster  = int(input("Total booster doses: "))
    grandtotal  = int(input("Cumulative administered: "))

    cursor.execute("""
    INSERT INTO vaccinationstats (date, dose1, dose2, booster, totaldose1, totaldose2, totalbooster, grandtotal)
    VALUES (?,?,?,?,?,?,?,?)
    """, (date, dose1, dose2, booster, totaldose1, totaldose2, totalbooster, grandtotal))

    connection.commit()
    connection.close()
    print("Vaccination statistics added, redirecting back to vaccination stats management shortly.")
    vaccinationStatsManage()

#>>>>>>>>>>>>>UPDATING DATA>>>>>>>>>>>>>
#function to update data in table "ppv"
def updateDataPPV():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    postcode = int(input("Which postcode do you want to update the PPV?: "))
    name = str(input("New name: "))
    location = str(input("New location: "))
    vaccineBrand = str(input("New Vaccine Brand: "))
    patientsPerDay = int(input("New Patients Per Day: "))
  
    #updates the table of according to postcode
    statement = f"UPDATE ppv SET name='{name}', location='{location}', vaccineBrand='{vaccineBrand}', patientsPerDay='{patientsPerDay}' WHERE postcode = '{postcode}';"
    cursor.execute(statement)

    connection.commit()
    connection.close()
    print("Information updated, redirecting to PPV management shortly.")
    PPVManage()

#function to update data in table "covidstats"
def updateDataCOVIDStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    date = str(input("Which date do you want to update the statistics?: "))
    cases = int(input("New cases: "))
    recoveries = int(input("New recoveries: "))
    deaths = int(input("New deaths: "))
    active = int(input("New active cases: "))
    cumulative  = int(input("New cumulative cases: "))
    tests  = int(input("New tests done: "))
  
    statement = f"UPDATE covidstats SET cases='{cases}', recoveries='{recoveries}', deaths='{deaths}', active='{active}', cumulative='{cumulative}', tests='{tests}' WHERE date = '{date}';"
    cursor.execute(statement)

    connection.commit()
    connection.close()
    print("Information updated, redirecting to COVID-19 stats management shortly.")
    covidStatsManage()

#function to update data in table "vaccinationstats"
def updateDataVaccinationStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    date = str(input("Which date do you want to update the statistics?: "))
    dose1 = int(input("New dose 1: "))
    dose2 = int(input("New dose 2: "))
    booster = int(input("New booster doses: "))
    totaldose1  = int(input("New total dose 1: "))
    totaldose2  = int(input("New total dose 2: "))
    totalbooster  = int(input("New total booster doses: "))
    grandtotal  = int(input("New cumulative administered: "))
  
    statement = f"UPDATE vaccinationstats SET dose1='{dose1}', dose2='{dose2}', booster='{booster}', totaldose1='{totaldose1}', totaldose2='{totaldose2}', totalbooster='{totalbooster}', grandtotal='{grandtotal}' WHERE date = '{date}';"
    cursor.execute(statement)

    connection.commit()
    connection.close()
    print("Information updated, redirecting to vaccination stats management shortly.")
    vaccinationStatsManage()

#>>>>>>>>>>>>>DATA DELETION>>>>>>>>>>>>>
#function to delete data in table "ppv"
def deleteDataPPV():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    postcode = int(input("Please enter the postcode of the PPV to be deleted: "))
  
    #deletes the row according to postcode
    statement = f"DELETE FROM ppv WHERE postcode='{postcode}';"
    cursor.execute(statement)

    connection.commit()
    connection.close()
    print("PPV deleted, redirecting to PPV management shortly.")
    PPVManage()

#function to delete data in table "covidstats"
def deleteDataCOVIDStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    date = str(input("Please enter the date of the statistics to be deleted: "))
  
    statement = f"DELETE FROM covidstats WHERE date='{date}';"
    cursor.execute(statement)

    connection.commit()
    connection.close()
    print("Statistics deleted, redirecting to COVID-19 stats management shortly.")
    covidStatsManage()

#function to delete data in table "vaccinationstats"
def deleteDataVaccinationStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    date = str(input("Please enter the date of the statistics to be deleted: "))
  
    statement = f"DELETE FROM vaccinationstats WHERE date='{date}';"
    cursor.execute(statement)

    connection.commit()
    connection.close()
    print("Statistics deleted, redirecting to vaccination stats management shortly.")
    vaccinationStatsManage()

#>>>>>>>>>>>>>DATA EXPORTS>>>>>>>>>>>>>
#function to choose what should it be sorted by
def dataExportUser():
    print("How should the table be sorted?")
    instruct = str(input("Please enter a command (normal, risk, status, age, postcode): "))
    while True:
        if instruct == "normal":
            dataExportUserNormal()
            break
        elif instruct == "risk":
            dataExportUserRisk()
            break
        elif instruct == "status":
            dataExportUserStatus()
            break
        elif instruct == "age":
            dataExportUserAge()
            break
        elif instruct == "postcode":
            dataExportUserPostcode()
            break
        else:
            print("Unknown command.")

#function to export all data in table "user"
def dataExportUserNormal():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "user"
    cursor.execute(f"SELECT * FROM user")
    output = cursor.fetchall()
    for i in output:
       print(i)
    connection.close()

#function to export table "user" according to risk
def dataExportUserRisk():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "user" and sorts risk by ascending order
    cursor.execute(f"SELECT * FROM user ORDER BY risk;")
    output = cursor.fetchall()
    for i in output:
       print(i)
    print("\n")
    connection.close()

#function to export table "user" according to status
def dataExportUserStatus():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "user" and sorts status by ascending order
    cursor.execute(f"SELECT * FROM user ORDER BY status;")
    output = cursor.fetchall()
    for i in output:
       print(i)
    print("\n")
    connection.close()

#function to export table "user" according to age
def dataExportUserAge():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "user" and sorts age by ascending order
    cursor.execute(f"SELECT * FROM user ORDER BY age;")
    output = cursor.fetchall()
    for i in output:
       print(i)
    print("\n")
    connection.close()

#function to export table "user" according to postcode
def dataExportUserPostcode():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "user" and sorts postcode by ascending order
    cursor.execute(f"SELECT * FROM user ORDER BY postcode;")
    output = cursor.fetchall()
    for i in output:
       print(i)
    print("\n")
    connection.close()

#function to export all data in table "ppv"
def dataExportPPV():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "ppv"
    cursor.execute(f"SELECT * FROM ppv")
    output = cursor.fetchall()
    for i in output:
       print(i)
    print("\n")
    connection.close()

#function to export all data in table "vaccinations" according to datetime
def dataExportVaccinations():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "vaccinations" and sorts datetime by ascending order
    cursor.execute(f"SELECT * FROM vaccinations ORDER BY datetime;")
    output = cursor.fetchall()
    for i in output:
       print(i)
    print("\n")
    connection.close()

#function to export all data in table "covidstats"
def dataExportCOVIDStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "covidstats"
    cursor.execute(f"SELECT * FROM covidstats")
    output = cursor.fetchall()
    print("Date (YYYY,MM,DD), New Cases, Recoveries, Deaths, Active Cases, Cumulative Cases, Tests Done")
    for i in output:
       print(i)
    print("\n")
    connection.close()

#function to export all data in table "vaccinationstats"
def dataExportVaccinationStats():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "vaccinationstats"
    cursor.execute(f"SELECT * FROM vaccinationstats")
    output = cursor.fetchall()
    print("Date (YYYY,MM,DD), Dose 1, Dose 2, Boosters, Total Dose 1, Total Dose 2, Total Booster, Total Doses Given")
    for i in output:
       print(i)
    print("\n")
    connection.close()

#*************************USER INTERACTION FUNCTIONS*************************
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
    postcode = int(input("Postcode: "))
    gender = int(input("Gender (0 for male, 1 for female): "))
  
    #Insert values above entered from user
    cursor.execute("""
    INSERT INTO user (ICnum, name, password, age, phone, address, postcode, gender, consent, userStatus)
    VALUES (?,?,?,?,?,?,?,?,?,?)
    """, (ICnum, name, password, age, phone, address, postcode, gender, 0, 0))

    #To save the changes in the files
    connection.commit()
    connection.close()

    print("\nSignup successful, you will be redirected shortly.\n")
    #Redirect to start menu page
    startMenu()

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
        statement = f"SELECT ICnum FROM user WHERE ICnum='{ICnum}' AND password = '{password}';"
        cursor.execute(statement)
        if not cursor.fetchone():  # An empty result evaluates to False.
            print("Login failed, please try again.\n")
        else:
            print("Welcome!")
            #the line below acts as a cookie to record the active user
            active = ICnum
            connection.close()
            mainMenu()
            return active

#function to logout normal users and admins
def logout():
    global active
    active = ""
    print("You have been logged out.")
    startMenu()
    return active

#function for users to assess risk
def userRisk():
    global active
    risk = 0
    print("----------------------------RISK ASSESSMENT----------------------------\n")
    print("To ensure everyone will receive their COVID-19 vaccine accordingly, you are advised to carry out a risk assesment.")
    print("Your risk will be displayed in a number from 1-5.")
    print("Please answer the following questions truthfully by answering either 'Y' for yes or 'N' for no.\n")

    while True:
        overseas = str(input("Have you been outside of the country in the past 14 days?\n"))
        if overseas == "Y":
            risk = risk + 0.6
            break
        elif overseas == "N":
            break
        else:
            print("Invalid input.\n")
    
    while True:
        CContact = str(input("Have you been in close contact with any COVID-19 patient in the past 14 days?\n"))
        if CContact == "Y":
            risk = risk + 0.6
            break
        elif CContact == "N":
            break
        else:
            print("Invalid input.\n")

    while True:
        age = str(input("Are you above 60 years old?\n"))
        if age == "Y":
            risk = risk + 0.5
            break
        elif age == "N":
            break
        else:
            print("Invalid input.\n")

    while True:
        diabetes = str(input("Are you diabetic?\n"))
        if diabetes == "Y":
            risk = risk + 0.7
            break
        elif diabetes == "N":
            break
        else:
            print("Invalid input.\n")
    
    while True:
        hypertension = str(input("Are you diagnosed with high blood pressure or any heart condition?\n"))
        if hypertension == "Y":
            risk = risk + 0.6
            break
        elif hypertension == "N":
            break
        else:
            print("Invalid input.\n")

    while True:
        immuneCompromised = str(input("Are you Immunocompromised?\n"))
        if immuneCompromised == "Y":
            risk = risk + 0.5
            break
        elif immuneCompromised == "N":
            break
        else:
            print("Invalid input.\n")

    while True:
        obese = str(input("Are you obese? (BMI>35)\n"))
        if obese == "Y":
            risk = risk + 0.6
            break
        elif obese == "N":
            break
        else:
            print("Invalid input.\n")

    while True:
        disease = str(input("Are you diagnosed with any other long term disease such as cancer, high cholesterol, stroke, chronic diseases, etc.?\n"))
        if disease == "Y":
            risk = risk + 0.5
            break
        elif disease == "N":
            break
        else:
            print("Invalid input.\n")

    while True:
        substance = str(input("Do you take unhealthy substances such as drugs, tobacco products, alcohol, etc.?\n"))
        if substance == "Y":
            risk = risk + 0.4
            break
        elif substance == "N":
            break
        else:
            print("Invalid input.\n")

    while True:
        pregnant = str(input("Are you pregnant?\n"))
        if pregnant == "Y":
            risk = risk + 0.4
            break
        elif pregnant == "N":
            break
        else:
            print("Invalid input.\n")

    print("Please state your occupation.\n")
    print("Type 5 if you are a frontline worker, 4 if your job requires face to face meets, 3 if your job requires you to move around, 2 if your job can be done at home and 1 if you are unemployed/staying at home full time.\n")
    
    while True:    
        job = int(input("Enter here: "))
        if job > 0 and job < 6:
            risk = risk + job/10
            break
        else:
            print("Invalid number, please try again.")
            
    #rounds down the risk to an integer
    risk = math.floor(risk)
    print("\nYour updated risk is", risk)
    
    #updates the risk of the user in the database 
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    statement = f"UPDATE user SET risk='{risk}' WHERE ICnum = '{active}';"
    cursor.execute(statement)
    connection.commit()
    connection.close()

    #redirect back to main menu
    print("\nYour risk assessment has been successfully completed, you will be redirected back to the main menu shortly.\n")
    mainMenu()

#function for users to update status
def status():
    global active
    status = 0
    print("----------------------------COVID 19 STATUS----------------------------\n")
    print("Please report your current COVID-19 status here.")
    print("Please type out your current status whether it be 'No symptoms', 'Casual contact', 'Close contact', 'Person Under Surveillance', 'Home Quarantine Order',  'COVID-19 positive, mild symptoms' or 'COVID-19 positive, severe symptoms'\n")
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

#function for users to update and view vaccination status
def vaccine():
    global active
    list=['[','(',']',')',',',"'"]
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT consent FROM user WHERE ICnum='{active}'")
    oldConsent = str(cursor.fetchall())
    consent ="".join(i for i in oldConsent if i not in list)
    if consent == "0":
        print("Welcome to the COVID-19 vaccination programme, to aid our country to defeat this virus, all able bodied citizen must recieve their COVID-19 vaccine.\n")
        print("Do you consent to recieving the COVID-19 vaccination? (Type 1 if you do consent, type 2 if you do not consent.)\n")
        while True:
            cons = int(input("Please type a number: "))
            if cons == 1:
                print("Congratulations, your COVID-19 vaccine appointment will arrive in a few days, please be patient.\n")
                cursor.execute(f"UPDATE user SET consent = 1 WHERE ICnum = '{active}';")
                cursor.execute(f"SELECT postcode FROM user WHERE ICnum = '{active}';")
                oldPostcode = str(cursor.fetchall())
                postcode ="".join(i for i in oldPostcode if i not in list)
                cursor.execute(f"INSERT INTO vaccinations (ICnum, postcodePPV, notify, confirmation) VALUES ('{active}','{postcode}', 0, 0)")
                print("You will be redirected back to main menu shortly.\n")
                connection.commit()
                connection.close()
                mainMenu()
                break
            elif cons == 2:
                print("Irresponsible.\n")
                cursor.execute(f"UPDATE user SET consent = 2 WHERE ICnum='{active}'")
                print("You will be redirected back to main menu shortly.\n")
                connection.commit()
                connection.close()
                mainMenu()
                break
            else:
                print("Invalid input.\n")

    elif consent == "1":
        cursor.execute(f"SELECT notify FROM vaccinations")
        oldNotify = str(cursor.fetchall())
        notify ="".join(i for i in oldNotify if i not in list)
        if notify == "1":
            cursor.execute(f"SELECT postcodePPV FROM vaccinations INNER JOIN ppv WHERE ICnum='{active}'")
            oldPostcode = str(cursor.fetchall())
            postcode ="".join(i for i in oldPostcode if i not in list)
            cursor.execute(f"SELECT name FROM ppv WHERE postcode='{postcode}'")
            oldLocation = str(cursor.fetchall())
            location ="".join(i for i in oldLocation if i not in list)
            cursor.execute(f"SELECT datetime FROM vaccinations WHERE ICnum='{active}'")
            oldDatetime = str(cursor.fetchall())
            datetime ="".join(i for i in oldDatetime if i not in list)
            print("You have been selected to be vaccinated at ",location, "during ",datetime, " (YYYYMMDDHHMM), would you be able to attend? (Type 1 for yes, type 2 for no)")
            while True:
                confirm = int(input("Please enter a number: "))
                if confirm == 1:
                    cursor.execute(f"UPDATE vaccinations SET confirmation = 1, notify = 0 WHERE ICnum='{active}'")
                    cursor.execute(f"UPDATE user SET vaccinationStatus = 1 WHERE ICnum='{active}'")
                    print("Great! See you then.")
                    print("Redirecting you to main menu shortly.")
                    connection.commit()
                    connection.close()
                    mainMenu()
                    break
                elif confirm == 2:
                    cursor.execute(f"UPDATE vaccinations SET confirmation = 2, notify = 0 WHERE ICnum='{active}'")
                    print("Our administrators will give you a new appointment shortly.")
                    print("Redirecting you to main menu shortly.")
                    connection.commit()
                    connection.close()
                    mainMenu()
                    break
                else:
                    print("Invalid input.\n")
        else:
            cursor.execute(f"SELECT vaccinationStatus FROM user WHERE ICnum='{active}'")
            oldStatus = str(cursor.fetchall())
            status ="".join(i for i in oldStatus if i not in list)
            if status == "1":
                print("Congratulations, you are already fully vaccinated, thank you for your kind efforts.\n")
                print("Redirecting you to main menu shortly.\n")
                connection.close()
                mainMenu()
            else:
                print("Please be patient, our administrators are finding open appointments for you.\n")
                print("Redirecting you to main menu shortly.\n")
                connection.close()
                mainMenu()

    elif consent == "2":
        print("Irresponsible.")
        mainMenu()

#function to let users to view or edit personal info
def personalInfo():
    print("-----------------------PERSONAL INFORMATION-----------------------\n")
    print("Type 1 to view your information.")
    print("Type 2 to edit your information.")
    print("Type 3 to return to main menu.")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
        if num == 1:
            viewPersonalInfo()
            break
        elif num == 2:
            editPersonalInfo()
            break
        elif num == 3:
            mainMenu()
            break
        else:
            print("Invalid input.\n")

#function to let users to update personal info
def editPersonalInfo():
    global active
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    print("\nPlease enter the following details: \n")
    name = str(input("Full Name: "))
    age = int(input("Age: "))
    phone = str(input("Phone number (without dash): "))
    address = str(input("Address: "))
    postcode = int(input("Postcode: "))
    gender = int(input("Gender (0 for male, 1 for female): "))
  
    statement = f"UPDATE user SET name='{name}', age='{age}', phone='{phone}', address='{address}', postcode='{postcode}', gender='{gender}' WHERE ICnum = '{active}';"
    cursor.execute(statement)

    connection.commit()
    connection.close()
    print("Information updated, redirecting back to personal information shortly.\n")
    personalInfo()

#function to export all data in table "user" by the active user
def viewPersonalInfo():
    global active
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()

    #Selects everything from table "covidstats"
    cursor.execute(f"SELECT ICnum, name, age, phone, address, postcode FROM user WHERE ICnum='{active}'")
    output = cursor.fetchall()
    print ("IC Number, Name, Age, Phone Number, Address, Postcode")
    for i in output:
       print(i)
    connection.close()
    print("Redirecting back to personal information shortly.\n")
    personalInfo()

#function to login for admin
def loginAdmin():
    print("----------------------------ADMIN LOGIN----------------------------\n")
    ICnum = str(input("Enter ID: "))
    rawPassword = str(input("Password: "))
    hash_object = hashlib.sha512(rawPassword.encode())
    password = hash_object.hexdigest()
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    statement = f"SELECT ICnum FROM user WHERE ICnum='{ICnum}' AND password = '{password}' AND userStatus = 1;"
    cursor.execute(statement)
    if not cursor.fetchone():
        print("Login failed, please try again.\n")
        startMenu()
    else:
        connection.close()
        mainMenuAdmin()

#>>>>>>>>>>>>>>DATABASE MANAGEMENT FUNCTIONS>>>>>>>>>>>>>>
#function to manage user data
def userManage():
    print("----------------------------USER MANAGEMENT----------------------------\n")
    print("What would you like to do?")
    print("Type 1 to create table user.")
    print("Type 2 to view all user data.")
    print("Type 3 to return to main menu.")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
        if num == 1:
            newTableUser()
            break
        elif num == 2:
            dataExportUser()
            userManage()
            break
        elif num == 3:
            mainMenuAdmin()
            break
        else:
            print("Invalid input.\n")

#function to manage PPV data
def PPVManage():
    print("----------------------------PPV MANAGEMENT----------------------------\n")
    print("What would you like to do?")
    print("Type 1 to create table PPV.")
    print("Type 2 to view all PPV data.")
    print("Type 3 to add a PPV.")
    print("Type 4 to update a PPV's details.")
    print("Type 5 to remove a PPV.")
    print("Type 6 to return to main menu.")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
        if num == 1:
            newTablePPV()
            break
        elif num == 2:
            dataExportPPV()
            PPVManage()
            break
        elif num == 3:
            addDataPPV()
            break
        elif num == 4:
            updateDataPPV()
            break
        elif num == 5:
            deleteDataPPV()
            break
        elif num == 6:
            mainMenuAdmin()
            break
        else:
            print("Invalid input.\n")

#function to manage vaccination appointments
def vaccineManageAppoint():
    connection = sqlite3.connect("mysejahtera_0.5.db")
    cursor = connection.cursor()
    list=['[','(',']',')',',',"'"]

    print("This is the list of users that are waiting for an appointment.")
    cursor.execute(f"SELECT * FROM vaccinations WHERE notify = 0 AND confirmation = 0;")
    output = cursor.fetchall()
    for i in output:
       print(i)

    print("This is the list of users that rejected the first appointment are waiting for a 2nd appointment.")
    cursor.execute(f"SELECT * FROM vaccinations WHERE notify = 0 AND confirmation = 2;")
    output = cursor.fetchall()
    for i in output:
       print(i)

    while True:
        ICnum = str(input("Which user would you like to make an appointment to? (Type 0 to return to main menu.): "))
        if ICnum == "0":
            print("You will be redirected shortly.")
            connection.close()
            mainMenuAdmin()
            break
        else:
            statement = f"SELECT ICnum FROM user WHERE ICnum='{ICnum}'"
            cursor.execute(statement)
            if not cursor.fetchone():
                print("No such person exists.")
            else:
                cursor.execute(f"SELECT postcode FROM user WHERE ICnum='{ICnum}'")
                oldPostcode = str(cursor.fetchall())
                postcode ="".join(i for i in oldPostcode if i not in list)
                cursor.execute(f"UPDATE vaccinations SET notify = 1 , confirmation = 0 , postcodePPV='{postcode}' WHERE ICnum='{ICnum}' ")
                connection.commit()
                print("Records updated.")

#function to manage vaccinations
def vaccineManage():
    print("----------------------------VACCINATION MANAGEMENT----------------------------\n")
    print("What would you like to do?")
    print("Type 1 to create table vaccinations.")
    print("Type 2 to manage vaccinations.")
    print("Type 3 to return to main menu.")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
        if num == 1:
            newTableVaccinations()
        elif num == 2:
            vaccineManageAppoint()
            break
        elif num == 3:
            mainMenuAdmin()
            break
        else:
            print("Invalid input.\n")

#function to choose what stats to manage
def statsManage():
    print("----------------------------STATISTICS MANAGEMENT----------------------------\n")
    print("What would you like to do?")
    print("Type 1 for COVID-19 statistics.")
    print("Type 2 for vaccination statistics.")
    print("Type 3 to return to main menu.")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
        if num == 1:
            covidStatsManage()
        elif num == 2:
            vaccinationStatsManage()
            break
        elif num == 3:
            mainMenuAdmin()
            break
        else:
            print("Invalid input.\n")

#function to manage COVID-19 stats
def covidStatsManage():
    print("----------------------------COVID STATS MANAGEMENT----------------------------\n")
    print("What would you like to do?")
    print("Type 1 to create COVID-19 statistics table.")
    print("Type 2 to view COVID-19 statistics.")
    print("Type 3 to add COVID-19 statistics.")
    print("Type 4 to update COVID-19 statistics.")
    print("Type 5 to remove COVID-19 statistics.")
    print("Type 6 to return to main menu.")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
        if num == 1:
            newTableCOVIDStats()
            break
        elif num == 2:
            dataExportCOVIDStats()
            covidStatsManage()
            break
        elif num == 3:
            addDataCOVIDStats()
            break
        elif num == 4:
            updateDataCOVIDStats()
            break
        elif num == 5:
            deleteDataCOVIDStats()
            break
        elif num == 6:
            mainMenuAdmin()
            break
        else:
            print("Invalid input.\n")

#function to manage vaccination stats
def vaccinationStatsManage():
    print("----------------------------VACCINATION STATS MANAGEMENT----------------------------\n")
    print("What would you like to do?")
    print("Type 1 to create vaccination statistics table.")
    print("Type 2 to view vaccination statistics.")
    print("Type 3 to add vaccination statistics.")
    print("Type 4 to update vaccination statistics.")
    print("Type 5 to remove vaccination statistics.")
    print("Type 6 to return to main menu.")
    while True:
        num = int(input("Enter a number: "))
        print("\n-------------------------------------------------------------\n")
        if num == 1:
            newTableVaccinationStats()
            break
        elif num == 2:
            dataExportVaccinationStats()
            vaccinationStatsManage()
            break
        elif num == 3:
            addDataVaccinationStats()
            break
        elif num == 4:
            updateDataVaccinationStats()
            break
        elif num == 5:
            deleteDataVaccinationStats()
            break
        elif num == 6:
            mainMenuAdmin()
            break
        else:
            print("Invalid input.\n")

#*************************MENUS FUNCTIONS*************************
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
            print("Invalid input.\n")

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
    print("Welcome", name, "please type a number.")
    print("Type 1 for vaccination appointments.")
    print("Type 2 for risk assesment.")
    print("Type 3 for updating personal information.")
    print("Type 4 for current COVID-19 updates.")
    print("Type 5 to log out.")
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
            personalInfo()
            break
        elif num == 4:
            print("\nThis is the list of COVID-19 statistics starting from 1st January 2022\n")
            dataExportCOVIDStats()
            print("\nThis is the list of vaccination statistics starting from 1st January 2022\n")
            dataExportVaccinationStats()
            print("\nRedirecting to main menu shortly. \n")
            mainMenu()
            break
        elif num == 5:
            logout()
            break
        else:
            print("Invalid input.\n")
    connection.close()

#function for menu when admin logged in
def mainMenuAdmin():
    print("----------------------------ADMIN MENU----------------------------\n")
    print("Welcome admin.")
    print("Type 1 for user management.")
    print("Type 2 for PPV management.")
    print("Type 3 for vaccination management.")
    print("Type 4 for COVID-19 statistics management.")
    print("Type 5 to logout.")
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
            statsManage()
            break        
        elif num == 5:
            logout()
            break
        else:
            print("Invalid input.\n")

#call this for magic to happen
startMenu()