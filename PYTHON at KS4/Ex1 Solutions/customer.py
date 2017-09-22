class customer():
    '''
    The customer class, storing the information for each customer:
    firstname, surname, town, address
    '''

    def __init__(self, firstname="First name", surname="surname", town="Town", telephone="070 000 0000"):
        self.firstname=firstname
        self.surname = surname
        self.town = town
        self.telephone = telephone
    
    def get_firstname(self):
        return self.firstname
    
    def get_surname(self):
        return self.surname
    
    def get_town(self):
        return self.town
    
    def get_telephone(self):
        return self.telephone
    
    def print_customer(self):
        print("Name is  : ", self.firstname, self.surname)
        print("Town is  : ", self.town)
        print("Telephone: ", self.telephone)
    
    def set_firstname(self, new_name):
        self.firstname = new_name
    
    def set_surname(self, new_surname):
        self.surname = new_surname
    
    def set_town(self, new_town):
        self.town = new_town
    
    def set_telephone(self, new_telephone):
        self.telephone = new_telephone
        