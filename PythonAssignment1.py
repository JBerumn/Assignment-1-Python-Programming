

menuChoice=""
itemChoice=""
price=0

myInventory=[0,0,0]

def Menu():
    print("What would you like to do?")
    print("A: Make a Purchase")
    print("B: Make a Return")
    print("C: Check Inventory")
    print("D: Checkout")
    menuChoice=input()
    
    if(menuChoice=="A"):
        Purchase()
   
    if(menuChoice=="B"):
        Return()
        
    if(menuChoice=="C"):
        Inventory()
        
    if(menuChoice=="D"):
        Checkout()
        

def Purchase():
    print("What would you like to purchase")
    print("A.Shirt ($2.50)")
    print("B.Pineapple ($1.50)")
    print("C.Kale ($3.00)")
    itemChoice=input()
    
    if(itemChoice=="A"):
        myInventory[0] += 1
        print("Thank you for purchasing shirt(s)!")
        print("Would you like to make another purchase? (Y/N)")
        repeatChoice=input()
        if(repeatChoice=="Y"):
            Purchase()
        if(repeatChoice=="N"):
            Menu()
    if(itemChoice=="B"):
        myInventory[1] += 1
        print("Thank you for purchasing pineapple!")
        print("Would you like to make another return? (Y/N)")
        repeatChoice=input()
        if(repeatChoice=="Y"):
            Purchase()
        if(repeatChoice=="N"):
            Menu()
    if(itemChoice=="C"):
        myInventory[2] += 1
        print("Thank you for purchasing kale!")
        print("Would you like to make another return? (Y/N)")
        repeatChoice=input()
        if(repeatChoice=="Y"):
            Purchase()
        if(repeatChoice=="N"):
            Menu()

def Return():
    print("What would you like to return")
    print("A.Shirt ($2.50)")
    print("B.Pineapple ($1.50)")
    print("C.Kale ($3.00)")
    itemChoice=input()
    
    if(itemChoice=="A"):
        myInventory[0] -= 1
        print("Shirt(s) were removed from your inventory")
        print("Would you like to make another return? (Y/N)")
        repeatChoice=input()
        if(repeatChoice=="Y"):
            Purchase()
        if(repeatChoice=="N"):
            Menu()
    if(itemChoice=="B"):
        myInventory[1] -= 1
        print("Pineapple was removed from your inventory")
        print("Would you like to make another return? (Y/N)")
        repeatChoice=input()
        if(repeatChoice=="Y"):
            Purchase()
        if(repeatChoice=="N"):
            Menu()
    if(itemChoice=="C"):
        myInventory[2] -= 1
        print("Kale was removed from your inventory")
        print("Would you like to make another return? (Y/N)")
        repeatChoice=input()
        if(repeatChoice=="Y"):
            Purchase()
        if(repeatChoice=="N"):
            Menu()

def Inventory():
    print("Here is what you currently have in your inventory")
    print("Shirts:",myInventory[0])
    print("Pineapples:",myInventory[1])
    print("Kale:",myInventory[2])
    print("Press ENTER to proceed")
    menuChoice=input()
    if(menuChoice==""):
        Menu()
        
def Checkout():
    print("Here is what you currently have in your inventory")
    print("Shirts($2.50):",myInventory[0])
    print("Pineapples($1.50):",myInventory[1])
    print("Kale($3.00):",myInventory[2])
    
    total=(myInventory[0]*2.5)+(myInventory[1]*1.5)+(myInventory[2]*3.0)
    print("Your total is:",total)

    print("Press ENTER to proceed")
    menuChoice=input()
    if(menuChoice==""):
        Menu()


    
    

print("Welcome to my friggin EPIC store(for bottoms)")
Menu()
