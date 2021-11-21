import sqlite3

#Query the database and return all records
def show_all():
	#Connect to db and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	#Query the db
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()

	#Prints all records
	for i in items:
		print(i)

	#Commit our command
	conn.commit()
	#Close our connection
	conn.close()


#Add new record to the table:
def add_one(first, last, email):
	#Connect to db and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last,email))

	#Commit our command
	conn.commit()
	#Close our connection
	conn.close()


#Delete record from table
def delete_one(id):
	#Connect to db and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	c.execute("DELETE from customers WHERE rowid = (?)", id)

	#Commit our command
	conn.commit()
	#Close our connection
	conn.close()


def add_many(list):
	#Connect to db and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	c.executemany("INSERT INTO customers VALUES (?,?,?)", list)

	#Commit our command
	conn.commit()
	#Close our connection
	conn.close()


#Lookup with WHERE
def email_lookup(email):
	#Connect to db and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	c.execute("SELECT * FROM customers WHERE email = (?)", (email,))
	items = c.fetchall()

	#Prints all records
	for i in items:
		print(i)

	#Commit our command
	conn.commit()
	#Close our connection
	conn.close()







