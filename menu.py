# Import necessary modules and functions
import fooditems  
from playsound import playsound
from audionumbers import audionumbers
         
# Initialize global variables
cart = []       # List to store selected food items
totalprice = 0  # Variable to keep track of the total price


def coffee():
    cart.append(fooditems.Coffee.handle())
def pizza():
    cart.append(fooditems.Pizza.handle())
def burger():
    cart.append(fooditems.Burger.handle())
def sandwich():
    cart.append(fooditems.Sandwich.handle())
def maggi():
    cart.append(fooditems.Maggi.handle())
def random():
    cart.append(fooditems.randomDish())

# Function to calculate and display the billing details
def billing():
    tprice = 0
    # Function to calculate and display the billing details
    for i in cart:
        tprice+=i.getPrice()
    print("Grand total is :"+str(tprice) +"\n")
    
    
    # Apply and display discount if total price is above a certain threshold
    disc = 0
    if tprice >= 500:
        disc = (10/100) *tprice
        tprice-=disc
        print("Grand total is :"+str(tprice)+"\n") 
    
    # Convert the total price to voice using audionumbers module
    path = "audio/totalA.wav"
    playsound(path)
    audionumbers.numberToVoice(tprice)  
   
     

 # Function to display the main menu and handle user choices   
def menu():

    global totalprice, cart             # Access global variables

    while True:
        
        print("1.coffee\n2.burger\n3.pizza\n4.sandwich\n5.maggi\n6.random\n7.billing\n")
        
        choice = input("Enter your choice: ")
        
        # Check user's choice and perform corresponding action
        if choice == "1":
            coffee()
        elif choice == "2":
            burger()
        elif choice == "3":
            pizza()
        elif choice == "4":
            sandwich()
        elif choice == "5":
            maggi()
        elif choice == "6":
            random()
        elif choice == "7":
            billing()
            cart = []
            break
        else:
            print("Invalid Choice")
        
         # Display selected items and update the total price
        totalprice = 0
        for i in cart:
            i.show()
            totalprice+=i.getPrice()
       

   
