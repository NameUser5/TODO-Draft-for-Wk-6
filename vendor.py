class Vendor():
    def __init__(self, name, sales_contact, city, account_number, street_adress="", state="", zip="", payment_terms="", bank_number="", routing_number=""):
        
      self.name = name
      self.sales_contact = sales_contact
      self.city = city
      self.account_number = account_number
      self.street_adress = street_adress
      self.state = state
      self.zip = zip
      self.payment_terms = payment_terms
      self.bank_number = bank_number
      self.routing_number = routing_number
      self.vskus = []

#TODO add an attribute that is a list to hold inventory.This will be the vendor's specific inventory and price. Create a function that will allow the vendor's inventory list (including prices) to be printed.  --DANIEL

#???