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
        
        while True:
            print("1.flavor Espresso\n2.flavor Cold brew\n3.flavor Hot Coffee\n4flavor Latte\n")

            flavor = "Hot Coffee"

            choice = input("Enter your choice: ")

            if choice == "1":
                flavor = "Espresso"
                price+=50
                break
            elif choice == "2":
                flavor = "Cold brew"
                price+=40
                break
            elif choice == "3":
                flavor = "Hot coffee"
                price+=25
                break
            elif choice == "4":
                flavor = "Latte"  
                price+=55 
                break  
            else:
                print("Invalid Choice")    
        
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
        while True:
            print("1.size 16\n2.size 14\n3.size 12\n4size 10\n")
            
            choice = input("Enter your choice: ")

            size = 16
            
            if choice == "1":
                size = 16
                price+=120
                break
            elif choice == "2":
                size = 14
                price+=100
                break
            elif choice == "3":
                size = 12
                price+=80
                break
            elif choice == "4":
                size = 10  
                price+=50 
                break
            else:
                print("Invalid Choice")      
        while True:

            print("1.topping Pepperponi\n2.topping Mushrooms\n3.Onions\ntopping Bacon\n")   
            
            choice = input("Enter your choice: ")      

            topping = "Bacon"      

            if choice == "1":
                topping = "Pepperponi"
                price+=120
                break
            elif choice == "2":
                topping = "Mushrooms"
                price+=140
                break
            elif choice == "3":
                topping = "Onions"
                price+=100
                break
            elif choice == "4":
                topping = "Bacon"  
                price+=150 
                break
            else:
                print("Invalid Choice")    
        while True:

            print("1.crust Thin\n2.crust Stuffed\n3.crust Thik\ncrust Regular\n") 
        
            choice = input("Enter ypur choice: ")     

            CrustType = "Thin"

            if choice == "1":
                crust = "Thin"
                price+=100
                break
            elif choice == "2":
                crust = "stuffed"
                price+=120
                break
            elif choice == "3":
                crust = "Thik"
                price+=150
                break
            elif choice == "4":
                crust = "Regular" 
                price+=80 
                break 
            else:
                print("Invalid Choice")    
        
        while True:

            print("1.suace Tomato\n2.sauce Pesto\n3.sauce Alfredo\nsauce Barbecue\n")
            
            choice = input("Enter your choice: ")

            sauce = "Tomato"

            if choice == "1":
                sauce = "Tomato"
                price+=100
                break
            elif choice == "2":
                sauce = "Pesto"
                price+=150
                break
            elif choice == "3":
                sauce = "Alfredo"
                price+=120
                break
            elif choice == "4":
                sauce = "Barbecue"
                price+=160 
                break  
            else:
                print("Invalid Choice")    

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
        
        while True:

            print("1.size 6\n2.size 4\n3.size 8\nsize 3\n")

            size = 6

            choice = input("Enter your choice: ")

            if choice == "1":
                size = 6
                price+=60
                break
            elif choice == "2":
                size = 4
                price+=50
                break
            elif choice == "3":
                size = 8
                price+=80
                break
            elif choice == "4":
                size = 3
                price+=30
                break
            else:
                print("Invalid Choice")    

        while True:

            print("1.pattytype Mushroom\n2.pattytype Veggi\n3.pattytype Chicken\npattytype Lamb \n") 

            pattytype = "Veggi"

            choice = input("Enter your choice: ")

            if choice == "1":
                pattytype = "Mushroom"
                price+=20
                break
            elif choice == "2":
                pattytype = "Veggi"
                price+=60
                break
            elif choice == "3":
                pattytype = "Chicken"
                price+=50
                break
            elif choice == "4":
                pattytype = "Quinoa" 
                price+=35
                break
            else:
                print("Invalid Choice")    

        while True:

            print("1.toppings Tomato\n2.toppings Pickles\n3.toppings Bacon\ntoppings Lettuce\n")

            toppings = "Tomato"

            choice = input("Enter your choice: ")

            if choice == "1":
                toppings = "Tomato" 
                price+=30
                break
            elif choice == "2":
                toppings = "Pickles"
                price+=25
                break
            elif choice == "3":
                toppings = "Bacon"
                price+=50
                break
            elif choice == "4":
                toppings = "Lettuce"
                price+=45
                break
            else:
                print("Invalid Choice")    

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
        
        while True:

            print("1.breadtype White bread\n2breadtype Whole Wheat\n3.breadtype Tortilla\nbreadtype Rye bread\n")

            breadtype = "Whole Wheat"

            choice = input("Enter your choice: ")

            if choice == "1":
                breadtype = "White bread"
                price+=20
                break
            elif choice == "2":
                breadtype = "Whole Wheat"
                price+=25
                break
            elif choice == "3":
                breadtype =  "Tortilla"
                price+=15
                break
            elif choice == "4":
                breadtype =  "Rye bread"
                price+=10
                break
            else:
                print("Invalid Choice")    

        while True:

            print("1.filling Turkey\n2.filling Capress\n3.filling BLT\nfilling Tuna salad\n")

            filling = "Turkey"

            choice = input("Enter your choice: ")

            if choice == "1":
                filling = "Turkey"
                price+=30
                break
            elif choice == "2":
                filling = "Capress"
                price+=35
                break
            elif choice == "3":
                filling = "BLT"
                price+=40
                break
            elif choice == "4":
                filling = "Tuna salad"
                price+=20
                break
            else:
                print("Invalid Choice")    

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
        
        while True:

            print("1.flavor Masala\n2.flavor Vegetable\n3.flavor Chicken\nflavor Cheese\n")

            flavor = "Masala"

            choice = input("Enter your choice: ")

            if choice == "1":
                flavor = "Masala"
                price+=10
                break
            elif choice == "2":
                flavor = "Vegetable" 
                price+=20 
                break 
            elif choice == "3":
                flavor = "Chicken"
                price+=30
                break
            elif choice == "4":
                flavor = "Cheese"
                price+=25
                break
            else:
                print("Invalid Choice")    
        
        while True:

            print("1.quantity 1\n2.quantity 2\n3.quantity 3\n 4\n")

            quantity = "1"

            choice = input("Enter your choice: ")

            if choice == "1":
                quantity = 1
                price+=20
                break
            elif choice == "2":
                quantity = 2
                price+=10
                break
            elif choice == "3":
                quantity = 3
                price+=27
                break
            elif choice == "4":
                quantity = 4   
                price+=35
                break
            else:
                print("Invalid Choice")    

        while True:

            print("1.topping Egg\n2.topping Vegetables\n3.topping Herbs and grrens\ntopping Sauce\n")

            topping = "Egg"

            choice = input("Enter your choice: ")

            if choice == "1":
                topping = "Egg"
                price+=10
                break
            elif choice == "2":
                topping = "Vegetables"
                price+=20
                break
            elif choice == "3":
                topping = "Herbs and greens"
                price+=30
                break
            elif choice == "4":
                topping = "Sauce"
                price+=25
                break
            else:
                print("Invalid Choice")    

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

