from customer import customer
from quote import quotation
from datetime import datetime
import sys

customer_list = []
quotation_list = []

# main menu
def main_menu():
    print("Welcome to John's Decorating")
    print("You have the following options:\n")
    print("1)    Add a new customer")
    print("2)    List all customer")
    print("3)    Add a new quote")
    print("4)    List all Quotation")
    print("5)    Save customer details")
    print("6)    Save Quotation to file\n")
    print("0)    Exit")
    
    
    choice = int(input("Select one --> "))
    if choice == 1:
        add_customer()
    if choice ==2:
        list_all_customer()
    if choice ==3:
        add_a_quote()
    if choice ==4:
        list_all_quotations()
    if choice ==5:
        save_customer_details()
    if choice ==6:
        save_quotation()
        
    if choice ==0:
        print("Good bye ...............")
        sys.exit()

def save_quotation():
    print("Saving Quotations ...")
    file_name=input("Enter the file name to save in : ")
    file_name = file_name+"_quotations.txt"
    quote_file = open(file_name,'w')
    for quote in quotation_list:
        quote_file.write(quote.customer.get_firstname()+"\n")
        quote_file.write(str(quote.get_quotation_date())+ "\n")
        quote_file.write(str(quote.get_length())+ "\n")
        quote_file.write(str(quote.get_width())+ "\n")
        quote_file.write(quote.get_underlay_name()+ "\n")
        quote_file.write(str(quote.get_gripper())+ "\n")
        quote_file.write(str(quote.get_underlay_price())+ "\n")
        quote_file.write(str(quote.get_total_price())+ "\n")
    quote_file.close()
    
    print("File saved")
    main_menu()

#function used to save customers details
def save_customer_details():
    print("Saving Customers' Details ...")
    file_name=input("Enter the file name to save in : ")
    file_name = file_name+"_customers.txt"
    cust_file = open(file_name,'w')
    for cust in customer_list:
        cust_file.write(cust.get_firstname()+"\n")
        cust_file.write(cust.get_surname()+ "\n")
        cust_file.write(cust.get_town()+ "\n")
        cust_file.write(cust.get_telephone()+ "\n")
    cust_file.close()
    
    print("File saved")
    main_menu()
    
#function used to add a new customer, once confirmed save the customer in a 
#customer list
def add_customer():
    print("Add customer")
    firstname = input("Enter the customer's first name: ")
    surname = input("Enter the customer's surname:  ")
    town=input("Enter the customer's town: ")
    telephone = input("Please enter the customer's telephone number: ")
    customer1 = customer(firstname, surname,town, telephone)
    customer1.print_customer()
    customer_list.append(customer1)
    print("Customer added successfully ...")
    another = input("Would you like to add another? yes [y]  or no [n] --> ")
    if another=='y':
        add_customer()
    else:
        main_menu()

    
#list all the quotation in the system
def list_all_quotations():
    number =1
    for quote in quotation_list:
        print("Quotation " , str(number))
        quote.print_quotation()
        number = number +1
        print("\n")
    
    print("[A] Add new    [D] Delete      [B] Back")
    choice=input("-->")
    if choice=='a' or choice=='A':
        add_a_quote()
    else:
        if choice=='d' or choice=='D':
            print("Enter the quotation number to delete")
            quote_num = int(input("--> "))
            quote = quotation_list[quote_num-1]
            print("Are you sure you want to delete: ")
            quote.print_quotation()
            choice = input("[Y] Yes    [N] No") 
            if choice =='y' or choice =='Y':
                quotation_list.remove(quote)
                print("Quotation removed ")
                main_menu()
            else:
                list_all_quotations()
        else:
            main_menu()
     
def list_all_customer():
    number =1
    for cust in customer_list:
        print("Customer" , str(number))
        cust.print_customer()
        number = number +1
        print("\n")
    
    print("[A] Add new    [D] Delete   [V] View Quote for customer     [B] Back")
        
    choice = input("What would you like to do --> ")
    if choice == 'a' or choice=='A':
        add_customer()
    else:
        if choice =='d' or choice =='D':
            delete_customer()
        else:
            if choice == 'v' or choice =="V":
                view_quote()
            else:
                main_menu()

def add_a_quote():
    print("Add new Quote")
    print("[N] New customer     [E] Exiting customer")
    choice=input("-->")
    if choice == 'n' or choice == 'N':
        customer1 = add_customer_for_quote()
    else:
        customer1 = search_for_existing_customer()  
    
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    print("Underlay Choice")
    print("[F] First Step (5.99)   [M] Monarch (7.99)     [R] Royal (60)")
    choice=input("-->")
    if choice == 'f' or choice =='F':
        uname = "First Step"
    else:
        if choice =='m' or choice =='M':
            uname="Monarch"
        else:
            uname="Royal"
    gripper = 2*length + 2*width
    quotation1 = quotation(customer1, datetime.now(), length, width, uname, gripper)
    quotation1.print_quotation()
    print("[A] Add    [D] Delete")
    choice=input("-->")
    if choice=='a' or choice =='A':
        quotation_list.append(quotation1)
        print("Quote added successfully")
        main_menu()
    else:
        main_menu()
    
def add_customer_for_quote():
    print("Add customer For new Quote")
    firstname = input("Enter the customer's first name: ")
    surname = input("Enter the customer's surname:  ")
    town=input("Enter the customer's town: ")
    telephone = input("Please enter the customer's telephone number: ")
    customer1 = customer(firstname, surname,town, telephone)
    #customer1.print_customer()
    customer_list.append(customer1)
    return customer1
    
def search_for_existing_customer():
    number =1
    print("Here is a list of all customers ")
    for cust in customer_list:
        print("Customer" , str(number))
        cust.print_customer()
        number = number +1
        print("\n")
    print("enter the customer number to add a quote for ")
    cust_number=int(input("-->"))
    customer1=customer_list[cust_number-1]
    return customer1    
    
def delete_customer():
    print("Delete Customer")
    cust_number=int(input("Enter the customer number to delete --> "))
    customer1 = customer_list[cust_number-1]
    print("Customer")
    customer1.print_customer()
    print("Are you sure you want to delete [Y] Yes    [N] No")
    choice = input("--> ")
    if choice =='y' or choice=='Y':
        customer_list.remove(customer1)
        print("Customer information Deleted  ...")
    main_menu()

def view_quote():
    print("View Quote") 
    print("Enter the customer's number to view quote")
    choice = int(input("-->"))
    customer1=customer_list[choice-1]
    
    #Create a dummy quote, just in case the customer do not have a quote saved
    target_quote = quotation(customer1, datetime.now(), 0, 0, "dummy", 0 )
    #Now search for the quotation with the customer
    for quote in quotation_list:
        if quote.customer == customer1:
            target_quote = quote  
    if target_quote.get_underlay_name() == "dummy":
        print("Sorry", customer1.get_firstname(), "does not have a quote ")
        print("Here is a list of all your customers")
        list_all_customer()
    else:
        target_quote.print_quotation()
        choice=input("continue --> ")
        main_menu()
    
main_menu()