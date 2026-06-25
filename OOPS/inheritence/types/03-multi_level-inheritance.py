

class Base_Cost:
    def __init__(self,baseCost):
        self.baseCost = baseCost
        
class Build_Cost(Base_Cost):
    def __init__(self,baseCost,buildCost):
        super().__init__(baseCost)
        self.buildCost = buildCost
        
class Tax_Cost(Build_Cost):
    def __init__(self,baseCost,buildCost,taxCost):
        super().__init__(baseCost,buildCost)
        self.taxCost = taxCost
    
    def print_cost(self):
        print(self.baseCost,self.buildCost,self.taxCost)

car = Tax_Cost(45000,345000,55000)

car.print_cost()















