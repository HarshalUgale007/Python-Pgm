class calculator:
    def __init__(self):
      pass

    def add(self, a, b):
      self.plus = a + b
      if x == "add":
        print("Addition of your numbers is: ", self.plus)

    def sub(self, a, b):
      self.minus = a - b
      if x == "sub":
        print("Subtraction of your numbers is: ", self.minus)

    def mul(self, a, b):
      self.into = a * b
      if x == "mul":
        print("Multiplication of your numbers is: ", self.into)

    def div(self, a, b):
      self.divide = a / b
      if x == "div":
        print("Division of your numbers is: ", self.divide)

    def mod(self, a, b):
      self.modulus = a % b
      if x == "mod":
        print("Modulus of your numbers is: ", self.modulus)

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
x = input("Enter calculation type: ")

obj = calculator()
obj.add(a,b)
obj.sub(a,b)
obj.mul(a,b)
obj.div(a,b)
obj.mod(a,b)