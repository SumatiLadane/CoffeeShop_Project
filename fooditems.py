import random

# Coffee Class
class Coffee():

    def __init__(self, flavor,price):

        self.flavor = flavor
        self.price = price
    
    def getPrice(self):
        return self.price

    def show(self):
        print("Coffee-"+str(self.price))  
    
    @staticmethod
    def randomDish():
        return Coffee("Hot Coffee", 25)
    
    @staticmethod
    def handle():

        price = 0
        
        print("1.flavor Espresso\n2.flavor Cold brew\n3.flavor Hot Coffee\nflavor Latte\n")

        flavor = "Hot Coffee"

        choice = input("Enter your choice: ")

        if choice == 1:
            flavor = "Espresso"
            price+=50
        elif choice == 2:
            flavor = "Cold brew"
            price+=40
        elif choice == 3:
            flavor = "Hot coffee"
            price+=25
        else:
            flavor = "Latte"  
            price+=55   
        
        return Coffee(flavor,price)

# Pizza Class   
class Pizza():

    def __init__(self, size, topping, crust, sauce, price):

        self.size = size
        self.topping = topping
        self.crust = crust
        self.sauce = sauce
        self.price = price
    
    def getPrice(self):
        return self.price
    
    def show(self):
        print("Pizza-"+str(self.price)) 
    
    @staticmethod
    def randomDish():
        return Pizza(10,"Pepperponi","Regular","Tomato", 300)

    @staticmethod
    def handle():
        price = 0
        print("1.size 16\n2.size 14\n3.size 12\nsize 10\n")
        
        choice = input("Enter your choice: ")

        size = 16

        if choice == 1:
            size = 16
            price+=120
        elif choice == 2:
            size = 14
            price+=100
        elif choice == 3:
            size = 12
            price+=80
        else:
            size = 10  
            price+=50   

        print("1.topping Pepperponi\n2.topping Mushrooms\n3.Onions\ntopping Bacon\n")   
        
        choice = input("Enter your choice: ")      

        topping = "Bacon"      

        if choice == 1:
            topping = "Pepperponi"
            price+=120
        elif choice == 2:
            topping = "Mushrooms"
            price+=140
        elif choice == 3:
            topping = "Onions"
            price+=100
        else:
            topping = "Bacon"  
            price+=150 

        print("1.crust Thin\n2.crust Stuffed\n3.crust Thik\ncrust Regular\n") 
       
        choice = input("Enter ypur choice: ")     

        CrustType = "Thin"

        if choice == 1:
            crust = "Thin"
            price+=100
        elif choice == 2:
            crust = "stuffed"
            price+=120
        elif choice == 3:
            crust = "Thik"
            price+=150
        else:
            crust = "Regular" 
            price+=80  

        print("1.suace Tomato\n2.sauce Pesto\n3.sauce Alfredo\nsauce Barbecue\n")
        
        choice = input("Enter your choice: ")

        sauce = "Tomato"

        if choice == 1:
            sauce = "Tomato"
            price+=100
        elif choice == 2:
            sauce = "Pesto"
            price+=150
        elif choice == 3:
            sauce = "Alfredo"
            price+=120
        else:
            sauce = "Barbecue"
            price+=160   

        return Pizza(size,topping,crust,sauce,price)                                         


# Burger Class
class Burger():

    def __init__(self, size, pattytype, toppings,price):
        
        self.size = size
        self.pattytype = pattytype
        self.toppings = toppings
        self.price = price

    def getPrice(self):

        return self.price
    
    def show(self):

        print("Burger-"+str(self.price))    
    
    @staticmethod
    def randomDish():
        return Burger(6,"Veggi","Tomato", 150)    
    
    @staticmethod
    def handle():

        price = 0
        
        print("1.size 6\n2.size 4\n3.size 8\nsize 3\n")

        size = 6

        choice = input("Enter your choice: ")

        if choice == 1:
            size = 6
            price+=60
        elif choice == 2:
            size = 4
            price+=50
        elif choice == 3:
            size = 8
            price+=80
        else:
            size = 3
            price+=30

        print("1.pattytype Mushroom\n2.pattytype Veggi\n3.pattytype Chicken\npattytype Lamb \n") 

        pattytype = "Veggi"

        choice = input("Enter your choice: ")

        if choice == 1:
            pattytype = "Mushroom"
            price+=20
        elif choice == 2:
            pattytype = "Veggi"
            price+=60
        elif choice == 3:
            pattytype = "Chicken"
            price+=50
        else:
            pattytype = "Quinoa" 
            price+=35

        print("1.toppings Tomato\n2.toppings Pickles\n3.toppings Bacon\ntoppings Lettuce\n")

        toppings = "Tomato"

        choice = input("Enter your choice: ")

        if choice == 1:
            toppings = "Tomato" 
            price+=30
        elif choice == 2:
            toppings = "Pickles"
            price+=25
        elif choice == 3:
            toppings = "Bacon"
            price+=50
        else:
            toppings = "Lettuce"
            price+=45

        return Burger(size,pattytype,toppings,price)


# Sandwich Class
class Sandwich():

    def __init__(self, breadtype, filling, price):
        
        self.breadtype = breadtype
        self.filling = filling
        self.price = price

    def getPrice(self):

        return self.price

    def show(self):

        print("Sandwich-"+str(self.price))   
    
    @staticmethod
    def randomDish():
        return Sandwich("Whole Wheat", "BLT", 60)     
    
    @staticmethod
    def handle():  
        price = 0  

        print("1.breadtype White bread\n2breadtype Whole Wheat\n3.breadtype Tortilla\nbreadtype Rye bread\n")

        breadtype = "Whole Wheat"

        choice = input("Enter your choice: ")

        if choice == 1:
            breadtype = "White bread"
            price+=20
        elif choice == 2:
            breadtype = "Whole Wheat"
            price+=25
        elif choice == 3:
            breadtype =  "Tortilla"
            price+=15
        else:
            breadtype =  "Rye bread"
            price+=10

        print("1.filling Turkey\n2.filling Capress\n3.filling BLT\nfilling Tuna salad\n")

        filling = "Turkey"

        choice = input("Enter your choice: ")

        if choice == 1:
            filling = "Turkey"
            price+=30
        elif choice == 2:
            filling = "Capress"
            price+=35
        elif choice == 3:
            filling = "BLT"
            price+=40
        else:
            filling = "Tuna salad"
            price+=20

        return Sandwich(breadtype,filling,price)

# Maggi Class                         
class Maggi():

    def __init__(self, flavor, quantity, topping,price):
         
        self.flavor = flavor
        self.quantity = quantity
        self.topping = topping
        self.price = price

    def getPrice(self):

        return self.price


    def show(self):

        print("Maggi-"+str(self.price))    
    
    @staticmethod
    def randomDish():
        return Maggi("Masala", 1, "Vegetabales",50)
    
    @staticmethod
    def handle():

        price = 0

        print("1.flavor Masala\n2.flavor Vegetable\n3.flavor Chicken\nflavor Cheese\n")

        flavor = "Masala"

        choice = input("Enter your choice: ")

        if choice == 1:
            flavor = "Masala"
            price+=10
        elif choice == 2:
            flavor = "Vegetable" 
            price+=20  
        elif choice == 3:
            flavor = "Chicken"
            price+=30
        else:
            flavor = "Cheese"
            price+=25

        print("1.quantity 1\n2.quantity 2\n3.quantity 3\n 4\n")

        quantity = "1"

        choice = input("Enter your choice: ")

        if choice == 1:
            quantity = 1
            price+=20
        elif choice == 2:
            quantity = 2
            price+=10
        elif choice == 3:
            quantity = 3
            price+=27
        else:
            quantity = 4   
            price+=35

        print("1.topping Egg\n2.topping Vegetables\n3.topping Herbs and grrens\ntopping Sauce\n")

        topping = "Egg"

        choice = input("Enter your choice: ")

        if choice == 1:
            topping = "Egg"
            price+=10
        elif choice == 2:
            topping = "Vegetables"
            price+=20
        elif choice == 3:
            topping = "Herbs and greens"
            price+=30
        else:
            topping = "Sauce"
            price+=25

        return Maggi(flavor,quantity,topping,price)

def randomDish():
    """
    Generates a random dish from a selection of different food items.
    Returns a random food item object.
    """
    randomNum = random.randint(0,5)
    if randomNum == 0:
        return Coffee.randomDish()
    elif randomNum ==1:
        return Pizza.randomDish() 
    elif randomNum == 2:
        return Burger.randomDish()
    elif randomNum == 3:
        return Sandwich.randomDish() 
    elif randomNum == 4:
        return Maggi.randomDish() 
    else:
        pass           

if __name__=="__main__": 
    # Example usage of the Pizza class                                                    
    pizza = Pizza(16, "Bacon", "Thin", "Tomato", 200)  
    pizza.show()

