

#Customer class
class Customer:
    #initiate all variables and constructor
    def __init__(self, customerID, name, address, email, phone, member_status):
        self.customerID = customerID
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = member_status
        
    def get_customerID(self):
        return self.customerID
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_member_status(self):
        return self.member_status

#Transaction class
class Transaction:
    #initiate all variables and constructor
    def __init__(self, date, itemName, cost, customerID):
        self.date = date
        self.itemName = itemName
        self.cost = cost
        self.customerID = customerID
        
    def get_date(self):
        return self.date
    
    def get_itemName(self):
        return self.itemName
    
    def get_cost(self):
        return self.cost
    
    def get_customerID(self):
        return self.customerID
