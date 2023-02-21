"""==========STARTING CODE PROVIDED===================="""
import FoodClass as fc
# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]
dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}
order_total = 0

"""==========NEW CODE ADDEDssssssssssssssss===================="""

#The program said make two customers and run the program twice. However this really wasnt needed.
#To complicate things less here I made a list with both required customers and then added my third 
# test customer with no transactions just for testing purposes (It is commented out for submission)
customerList = [
                fc.Customer(570, "Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dselyarft@gmpg.org", "254-555-9362", False),
                fc.Customer(569, "Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", 'ahimsworthfs@list-manage.com', '254-555-2273', True)#,
                #fc.Customer(500, "Chrissss Code-worth", "2101 south 8th street normandy texas 77401", 'chrischris@baylor.com', '111-222-3333', False)
                ]

#Then make a empty list for the Transaction Objects Im gonna make and append into here
customerTransactions = []

#Now I loop through the dictionary and create a Transaction object and append it to my list for each item
for key, value in dict.items():
        date, item_name, cost, customerID = value
        customerTransaction = fc.Transaction(date, item_name, cost, customerID)
        customerTransactions.append(customerTransaction)

#The next step is to iterate over the list so we do each operation on each customer
for customer in customerList:
    
    #Since I have a list of customers I print their ID and a seperator
    print(f"============[CUSTOMER ID {customer.get_customerID()}]================")

    #Then Print their name and number like requested
    print(f"Customer Name: {customer.get_name()}")       
    print(f"Phone: {customer.get_phone()}")

    #next I make this variable for total cost tracking
    totalCost = 0
    

    #Now we need to iterate through all the transactions and get the ones for our customer
    for customerTransaction in customerTransactions:
        #Here I check if the ID's match, if they dont its not an associated transaction
      if customerTransaction.get_customerID() == customer.get_customerID():
            #Then I add to total cost and print out the transaction details
            totalCost += customerTransaction.get_cost()
            print(f"Order Item: {customerTransaction.get_itemName()} Price: ${customerTransaction.get_cost():.2f}")
    #No matter what I print the total (could be 0 if no transactions)
    print(f"Total Cost: ${(totalCost):.2f}")

    #Then I check for membership and if true print that info + calculation
    if customer.get_member_status() == True:
        print(f"Member Discount: ${(totalCost*0.20):.2f}")
        print(f"Total Cost After Discount: ${(totalCost-(totalCost*0.20)):.2f}")
