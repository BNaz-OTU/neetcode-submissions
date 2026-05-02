import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args):
        if len(args) == 1:
            value = math.pi * (args[0] ** 2)
            return round(value, 2)
        
        return args[0] * args[1]
        

    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
