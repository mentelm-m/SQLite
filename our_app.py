import database2

#Add a record to the database
#database2.add_one("Laura", "Smith", "laura@smith.com")

#Delete record from database
# database2.delete_one('6')
# database2.delete_one('7')

stuff = [
		('John', 'Krasinsky', 'john@krasinsky.com'),
		('Brenda', 'Smitherton', 'brenda@smitherton.com')
		]

#Lookup EMAIL ADDRESS
database2.email_lookup("john@krasinsky.com")

#database2.add_many(stuff)

#Show all records
#database2.show_all()