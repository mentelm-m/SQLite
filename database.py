import sqlite3


# Creates a connection to database in memory - temporary
#conn = sqlite3.connect(':memory:')

#Connects to a database file.
#If it doesnt exist, it will create one in the same folder
conn = sqlite3.connect('customer.db')


#Creating a cursor
#whataver you want to do in the table/database, cursor does it
c = conn.cursor()

# DATATYPES IN SQLite3:
#NULL - kinda like boolean
#INTEGER - whole number
#REAL - float numbers
#TEXT - like string in python
#BLOB - stores something as it is like mp3 file is a mp3 file and so on

#Create a table
# c.execute("""CREATE TABLE customers (
# 		first_name text,
# 		last_name text,
# 		email text
# 	)""")


#first execution: 
#c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

#DELETE/ Drop the table
c.execute("DROP TABLE customers")
conn.commit()


#import many
#we used a list and c.executemany command:
# many_customers = [
# 					('Wes', 'Brown', 'wes@brown.com'), 
# 					('Steph', 'Kuewa', 'steph@kuewa.com'), 
# 					('Dan', 'Pas', 'dan@pas.com')
# 				]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#Update records:
# c.execute("""UPDATE customers SET first_name = 'Bob'
# 			WHERE rowid = '1'
# 	""")
# conn.commit()

#Delete records:
# c.execute("DELETE from customers WHERE rowid = 6")
# conn.commit()


#Query the database:
c.execute("SELECT rowid, * FROM customers")
#print(c.fetchone())
#c.fetchmany(3)

#Query the database - ORDER BY
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
#c.execute("SELECT rowid, * FROM customers ORDER BY last_name")
#DESC means descedning order

#AND/OR 
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3")

items = c.fetchall()
#print(items)

# print("NAME " + "\t\t EMAIL")
# print("----------" + "\t ------")
# for i in items:
# 	print(i[0] + " " + i[1] + " \t " + i[2])

for i in items:
	print(i)






#print("Command executed succesfully...")

#Commit our command/s
conn.commit()

#Close connection - g
conn.close()
