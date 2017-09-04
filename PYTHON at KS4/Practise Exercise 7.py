"""
f = open("UKPrimeMinisters.txt", "r")
print(f.read())
f.close()

file_name = "my_quote.txt"
new_file = open(file_name, "w+")
new_file.close

def update_file(file_name,quote):
    new_file = open(file_name, "a")
    new_file.write("This is an update\n")
    new_file.write(quote)
    new_file.write("\n\n")
    new_file.close()
for index in range(0,3):
    quote = input("Enter favourite quote: ")
    update_file(file_name,quote)
print(new_file.read())
new_file.close()


import sqlite3
new_db = sqlite3.connect("C:\\Users\\User\\Desktop\\PYTHON at KS4\\library.db")
c = new_db.cursor()
c.execute('''CREATE TABLE Books
(book_isbn text,
book_title text,
book_type text,
book_author text,
publisher text)
''')

c.execute('''INSERT INTO Books
          VALUES ('978-0-340-88851-3', 'A2 Pure Mathematics', 'Non fictional', 'Catherine Berry', 'Hodder Education')''')
c.execute('''INSERT INTO Books
          VALUES ('978-1-118-10227-5', 'Android 4 Application Development', 'Non fictional', 'Reto Meier', 'Wiley')''')
c.execute('''INSERT INTO Books
          VALUES ('0-596-00699-3', 'Programming C#', 'Non fictional', 'Jesse Liberty', 'O Reilly')''')
new_db.commit()
new_db.close()

new_db = sqlite3.connect("C:\\Users\\User\\Desktop\\PYTHON at KS4\\library.db")
c = new_db.cursor()
c.execute('''SELECT * FROM Books
''')

book_library = c.fetchone()
for book in (book_library):
    print (book)
print ("\n")

book_library = c.fetchone()
for book in (book_library):
    print (book)
print ("\n")

book_library = c.fetchone()
for book in (book_library):
    print (book)
print ("\n")

new_db.close()

"""