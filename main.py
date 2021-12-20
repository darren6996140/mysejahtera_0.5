import sqlite3
  
# connecting to the database
connection = sqlite3.connect("mysejahtera0.5.db")
  
# cursor
cursor = connection.cursor()
  
# print statement will execute if there
# are no errors
print("Connected to the database")
  
# close the connection
connection.close()

#function to create a table named '', since data is preloaded, no need to call this function
def newUserTable():
    connection = sqlite3.connect("mysejahtera0.5.db")
  
    cursor = connection.cursor()
  
    # SQL command to create a table in the database
    command = """
    """
  
    # execute the statement
    cursor.execute(command)

    connection.close()

#function to imput new user's data into table ""
def newUser():
    connection = sqlite3.connect("mysejahtera0.5.db")
  
    cursor = connection.cursor()
  
    # SQL command to create a table in the database
    command = """
    """
  
    # execute the statement
    cursor.execute(command)

    connection.close()