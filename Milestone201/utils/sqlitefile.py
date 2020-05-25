import _sqlite3

connection = _sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('SQL Query')
connection.commit()

connection.close()
