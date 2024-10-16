#========================================
from math import sqrt

def Line():
    print ("--------------------------------")
#========================================
class Discriminant:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
#========================================
    def CalculateDiscriminant(self):
        try:
            self.a = float(self.a)
            self.b = float(self.b)
            self.c = float(self.c)
            self.d = float(self.d)

            Line()
            self.discriminant_value = (self.b ** 2) - 4 * (self.a) * (self.c)
            print("- Formula: b^2 - 4ac")
            
            print(f"- D = ({self.b})^2 - 4 * ({self.a}) * ({self.c})")
            return f"- D = √{self.discriminant_value}"

        except:
            return "- Incorrect input"
#========================================
    def DiscriminantResult(self):
        if self.discriminant_value < 0:
            Line()

            print("- No result\n- Discriminant can't be lesser than 0")

            return "--------------------------------"
        elif self.discriminant_value == 0:
            Line()
            result = -self.b / (2 * self.a)
            
            print("- Formula: -b / 2a")

            print(f"- ({-self.b}) / (2 * {self.a})")
            
            print(f"- One root: x = {result}")

            return "--------------------------------"
        else:            
            Line()

            x1 = round((-self.b - sqrt(self.discriminant_value)) / (2 * self.a), 2)
            x2 = round((-self.b + sqrt(self.discriminant_value)) / (2 * self.a), 2)

            print(f"- Formula(x1) = ({self.b} - √{self.discriminant_value}) / (2 * {self.a})")
            print(f"- Formula(x2) = ({self.b} + √{self.discriminant_value}) / (2 * {self.a})")
            Line()

            print(f"- x1 = {x1}\n- x2 = {x2}")
            
            return "--------------------------------"
#_Objects_===============================
first_object = Discriminant(12, 1, 4, 0)
#_Result_================================
print(first_object.CalculateDiscriminant())
print(first_object.DiscriminantResult())
#========================================