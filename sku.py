class Sku():
    def __init__(self, part_number, manufacturer, model, weight, dimension, quantity, condition, warehouse_location = [], color="", vendor="", cost=0, selling_price=0):
        
      self.part_number = part_number
      self.manufacturer = manufacturer
      self.model = model
      self.weight = weight
      self.dimension = dimension
      self.quantity = quantity
      self.condition = condition
      self.warehouse_location = warehouse_location
      self.color = color
      self.vendor = vendor
      self.cost = cost
      self.selling_price = selling_price

      def add_stock(self,warehouse_loc,qty):
        self.warehouse_location.append((warehouse_loc,qty))

        
      # skus = []

      # warehouses = []
      
      # def print_inventory(skus):
      #   for _ in skus:
      #     warehouses.append(_.warehouse_location)
        
#TODO Modify you code so that warehosue_location now stores a quantity and location. For example, [(MIA1, 10), (MIA2, 50), (DEF, 9)]. Create a class function/method that will allow the invetory location list to be printed. --SARAH

