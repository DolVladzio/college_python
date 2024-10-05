#_Task_2
#=========================================================
import random

def endLine():
    print()
#=========================================================
class MenuItem:
    def __init__(self, foodName, foodDescription, foodPrice, isVegeterian):
        self.foodName = foodName
        self.foodDescription = foodDescription
        self.foodPrice = foodPrice
        self.isVegeterian = isVegeterian
#=========================================================
class Order(MenuItem):
    def __init__(self, 
                foodName, foodDescription, foodPrice, isVegeterian, 
                orderNumber, customerName, countFood):
        super().__init__(foodName, foodDescription, foodPrice, isVegeterian)
        self.orderNumber = orderNumber
        self.customerName = customerName
        self.countFood = countFood
    #=========================================================
    def addItem(self): 
        return f"- Order: {self.orderNumber} has just created"
    #=========================================================
    def removeItem(self): 
        return f"- Order: {self.orderNumber} has just deleted"
    #=========================================================
    def orderInfo(self): 
        #_Checking if food is vegeterian or not
        if (self.isVegeterian) == True:
            typeOfFood = "Vegeterian"
        else:
            typeOfFood = "Not vegeterian"

        try:
            sumOfOrder = (int(self.foodPrice) * int(self.countFood))
        except:
            return "- Error!"

        return f"""==========================================
- Customer: {self.customerName}
- Food: {self.foodName}
- Description: {self.foodDescription}
- Type: {typeOfFood}
- Price(per piece): {self.foodPrice}UAH
- Count: {self.countFood}
- Sum(without a discount): {sumOfOrder}UAH
=========================================="""
#=========================================================
class DiscountedMenuItem(MenuItem):
    def __init__(self, discountPercentage): 
        self.discountPercentage = discountPercentage
    #=========================================================
    def applyDiscount(self): 
        return f"- Your have discount - {self.discountPercentage}%"
    #=========================================================
    def sumOrderWithDiscountable(self, sumWithoutDiscount): 
        sumWithDiscount = sumWithoutDiscount - ((sumWithoutDiscount * self.discountPercentage) / 100)
        return f"""==========================================

- Sum(with a discount): {sumWithDiscount}UAH

=========================================="""
#_Objects=================================================
order_object = Order("Борщ", "Смачна українська страва", 150, True, 75, "Vladzio", 2)
#=========================================================
discountedMenuItem_object = DiscountedMenuItem(7)
#_Result==================================================
print(order_object.addItem())

print(order_object.orderInfo())
endLine()
#=========================================================
print(discountedMenuItem_object.applyDiscount())
endLine()

print(discountedMenuItem_object.sumOrderWithDiscountable(300))
endLine()
#=========================================================
print(order_object.removeItem())
#=========================================================
