class Channel():
    def __init__(self, name, account_manager, type, marketplace_fee_percentage=0, transaction_fees=0, refund_policy="", warranty_policy="", content_manager=""):
        
      self.name = name
      self.account_manager = account_manager
      self.type = type
      self.marketplace_fee_percentage =        marketplace_fee_percentage
      self.transaction_fees = transaction_fees
      self.refund_policy = refund_policy
      self.warranty_policy = warranty_policy
      self.content_manager = content_manager
      
#TODO add a class atribute that will hold all SKUs sold on a channel. --DANIEL
      
      