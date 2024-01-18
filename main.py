import menu
import pyfiglet

# Display a welcome message using pyfiglet
print(pyfiglet.figlet_format("Welcome to 7 Clubs\n"))

while True:
    # Display menu options
    print("1.menu\n2.Table Resevation\n3.Feedback\n0.Exit\n")
    
    # Get user input for choice
    choice = input("Enter your choice: ")
    
    # Check user's choice and perform corresponding action
    if choice == "1":
        menu.menu()         # Display the menu
    elif choice == "0":
        print("Thank you for coming")
        break
    elif choice == "2":
        print("Feature Comming Soon...\n")
    elif choice == "3":
        print("Feature Comming Soon...\n")    
    else:
        print("Invalid Choice\n")

         


        




