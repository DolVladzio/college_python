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

    def CalculateDiscriminant(self):
        try:
            self.a = int(self.a)
            self.b = int(self.b)
            self.c = int(self.c)
            self.d = int(self.d)

            DiscriminantResult = (self.b ** 2) - 4 * (self.a) * (self.c)

            # Line()
            # print(f"- Example: {self.a}x^2 {self.b}x {self.c} = {self.d}")

            if DiscriminantResult < 0:
                print("- Discriminant can't be lesser than 0")
                return "- No result"
            elif DiscriminantResult == 0:
                Line
                DiscriminantResult = (- (self.b) / 2 * (self.a))

                print("- Formula: - (b / 2a)")
                return f"- Result of x: {DiscriminantResult}"
            else:
                Line()
                print("- Formula: b^2 - 4ac")
            
                print(f"- D = ({self.b})^2 - 4 * {self.a} * {self.c}")

                print(f"- D = √{DiscriminantResult}")
                Line()

                x1 = round(((self.b) - sqrt(DiscriminantResult)) / 2 * (self.a), 2)
                x2 = round(((self.b) + sqrt(DiscriminantResult)) / 2 * (self.a), 2)

                print(f"- Formula(x1) = ({self.b} - √{DiscriminantResult}) / (2 * {self.a})")
                print(f"- Formula(x2) = ({self.b} + √{DiscriminantResult}) / (2 * {self.a})")
                Line()

                print( f"- x1 = {x1}\n- x2 = {x2}")
                
                return "--------------------------------"
        except:
            return "- Incorrect input"
#_Objects_===============================
first_object = Discriminant(-12, -5.5, 4, 0)
#_Result_================================
print(first_object.CalculateDiscriminant())
#========================================
