from addition import Addition

class Calculator:
    @classmethod
    def add(cls, num1, num2):
        return (Addition.add(num1,num2))

    @classmethod
    def subtract(cls, num1, num2):
        num3 = -num2
        return (cls.add(num1,num3))

    @classmethod
    def multiply(cls, num1, num2):
        num4 = 0
        for x in range (0, num2):
            num4 = cls.add(num1, num4)
        return num4

    @classmethod
    def divide(cls, num1, num2):
        num5 = 0
        while num1 >= num2:
            num1 = cls.subtract(num1, num2)
            num5 = cls.add(num5, 1)
        return num5


print(Calculator.add(6,2))
print(Calculator.subtract(6,2))
print(Calculator.multiply(6,2))
print(Calculator.divide(17,2))















