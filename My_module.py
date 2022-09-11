class MyOperandFinder:
    def __init__(self, number):
        self.number = number
        self.operand = 0
       
        
    def __iter__(self):
        return self
    
    def __next__(self):
        _sum = self.number - self.operand
        if _sum < self.operand:
            raise StopIteration
        self.operand += 1
        
        return self.operand
    
    @classmethod
    def findOperand(cls, number):
        operand = list(cls(number)).pop()
        
        return operand