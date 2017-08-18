import sqlite3

#def carpet(length, width):
    #carpet_size = length * width
    #carpet_cost = carpet_size * 22.50
    #underlay_First_Step = carpet_size * 5.99
    #underlay_Monarch = carpet_size * 7.99
    #underlay_Royal = carpet_size * 60
    #gripper = (length + width) * 2


customer_db = sqlite3.connect("C:\\Users\\User\\Desktop\\projecttask\\Customer.db")
c = customer_db.cursor()

try:
    c.execute('''CREATE TABLE CustomerDetails 
    (Customer_FIRSTNAME text,
    Customer_SURNAME text,
    Customer_RESIDENCE text,
    Customer_PHONE int,
    Customer_LENGTH int,
    Customer_WIDTH int,
    Customer_UNDERLAY_TYPE text,
    Customer_GRIPPER_LENGTH int,
    Customer_TOTALCOST int)
    ''')

    customer_db.commit()

except:
    print("Table already created")

def labour(Customer_LENGTH, Customer_WIDTH,Customer_AREA):
    if Customer_AREA > 16:
        global labour_cost
        labour_cost = round((Customer_LENGTH * Customer_WIDTH) / 16) * 65
    else:
        labour_cost = 65

def new_customer():
    Customer_FIRSTNAME = input("Enter Firstname: ")
    Customer_SURNAME = input("Enter Surname: ")
    Customer_RESIDENCE = input("Enter Residence: ")
    Customer_PHONE = int(input("Enter phone number: "))
    Customer_LENGTH = int(input("Enter length: "))
    Customer_WIDTH = int(input("Enter width: "))
    Customer_AREA = Customer_WIDTH * Customer_LENGTH
    Customer_UNDERLAY_TYPE = input("Enter Underlay type(fs,m or r): ")
    Customer_GRIPPER_LENGTH = (Customer_LENGTH + Customer_WIDTH) * 2
    labour(Customer_LENGTH=Customer_LENGTH, Customer_WIDTH=Customer_WIDTH, Customer_AREA=Customer_AREA)

    if Customer_UNDERLAY_TYPE == "fs":
        firststep = 5.99
        Customer_TOTALCOST = firststep * Customer_AREA
    elif Customer_UNDERLAY_TYPE == "m":
        monarch = 7.99
        Customer_TOTALCOST = monarch * Customer_AREA
    else:
        royal = 60
        Customer_TOTALCOST = royal * Customer_AREA
    Customer_TOTALCOST += labour_cost + Customer_GRIPPER_LENGTH * 1.1

    c.execute("INSERT INTO CustomerDetails VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
              (Customer_FIRSTNAME,
               Customer_SURNAME,
               Customer_RESIDENCE,
               Customer_PHONE,
               Customer_LENGTH,
               Customer_WIDTH,
               Customer_UNDERLAY_TYPE,
               Customer_GRIPPER_LENGTH,
               Customer_TOTALCOST))

    customer_db.commit()
    print ("Enter another Customer [Y/n/d] ")
    resp = input()
    return resp

def delete_customer():
    global query_FIRSTNAME
    global query_SURNAME
    global query_PHONE
    query_FIRSTNAME = input("Enter Firstname for deletion: ")
    query_SURNAME = input("Enter Surname for deletion: ")
    query_PHONE = input("Enter Phone number for deletion: ")
    c.execute("DELETE FROM CustomerDetails WHERE Customer_FIRSTNAME=? AND Customer_SURNAME=? AND Customer_PHONE=?",(query_FIRSTNAME, query_SURNAME, query_PHONE))
    customer_db.commit()

resp = 'y'
while resp != 'n':
    if resp == 'd':
        delete_customer()
        c.execute('SELECT * FROM CustomerDetails')
        dblst = c.fetchall()
        if query_FIRSTNAME and query_SURNAME and query_PHONE in dblst:
            print(" - Unsuccessfully removed - ")
            for row in c.execute('SELECT * FROM CustomerDetails'):
                print(row)
            delete_customer()
        else:
            print(" - Successfully removed - ")
            for row in c.execute('SELECT * FROM CustomerDetails'):
                print(row)
            new_customer()

    resp = new_customer()


for row in c.execute('SELECT * FROM CustomerDetails'):
    print(row)

customer_db.close()


