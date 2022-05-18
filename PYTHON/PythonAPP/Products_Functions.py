import pickle
import Basic_Metods
import Products

def menuproducts():
    menuproductOption = -1
    print("For the management system of the products what file do you want to use?")
    fileName = Basic_Metods.BasicMethods.askForFile()
    while (menuproductOption != 0):
        print("\n------------------------MENU PRODUCTS------------------------")
        print("1) Update a product")
        print("2) Delete a product")
        print("3) Create a new product and save on a file")
        print("4) See all the products")
        print("5) Make a purchase")
        print("0) Exit")
        print("--------------------------------------------------------------\n")
        menuproductOption = Basic_Metods.BasicMethods.askAnInt("Enter an option: ")
        if menuproductOption == 1: #Update a product
            updateAproduct(fileName)
        elif menuproductOption == 2: #Delete a product
            deleteAproduct(fileName)
        elif menuproductOption == 3: #Inproductt new product  #Save the products on a file 
            saveAndCreateTheproducts(fileName)
        elif menuproductOption == 4: #See all the products
            seeAllTheproducts(fileName)
        elif menuproductOption == 5: #Make a purchase
            seeAllTheproducts(fileName)

def createANewproduct():
    print("\n---------------------------------------------------------------------")
    print("---------------- You are going to CREATE a product.--------------------")
    print("---------------------------------------------------------------------\n")
    id = Basic_Metods.BasicMethods.askAString("Enter the id: \n")
    group = Basic_Metods.BasicMethods.askAString("Enter the group: \n")
    name = Basic_Metods.BasicMethods.askAString("Enter the name: \n")
    description = Basic_Metods.BasicMethods.askAString("Enter the description: \n")
    price = Basic_Metods.BasicMethods.askAnDouble("Enter the price: \n")
    amount = Basic_Metods.BasicMethods.askAnInt("Enter the amount: \n")
    available = Basic_Metods.BasicMethods.askAString("Enter the available: \n")
    supplier = Basic_Metods.BasicMethods.askAString("Enter the supplier: \n")

    
    product = Products.Products(id, group, name, description, price, amount, available, supplier)
    return product

def seeAllTheproducts(fileName):
    print("\n---------------------------------------------------------------------")
    print("--------------- You are going to SEE all the products.-------------------")
    print("---------------------------------------------------------------------\n")
    Basic_Metods.BasicMethods.readFile(fileName)
        
    
def saveAndCreateTheproducts(fileName):
    ans = 1
    while ans == 1:
        c1 = createANewproduct()
        print("\n---------------------------------------------------------------------")
        print("---------------------- SAVING the product... ----------------------------")
        print("---------------------------------------------------------------------\n")
        Basic_Metods.BasicMethods.save_objectOn_File(c1,fileName)
        ans = Basic_Metods.BasicMethods.askAnInt("Do you want to add a new product? (1/0)")
    del c1

def deleteAproduct(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- DELETING the product --------------------------")
    print("---------------------------------------------------------------------\n")
    products = []
    seeAllTheproducts(fileName)
    print("Which product you want to delete?")
    id = Basic_Metods.BasicMethods.askAString("Enter the id of the product:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, id)
    if pos != -1:
        products = Basic_Metods.BasicMethods.readFileToList(fileName)
        products.pop(pos)
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, products)
    else:
        print("The product does not exist.")
   

def updateAproduct(fileName):
    print("\n---------------------------------------------------------------------")
    print("---------------------- UPDATING the product --------------------------")
    print("---------------------------------------------------------------------\n")
    products = []
    seeAllTheproducts(fileName)
    print("Which product you want to update?")
    id = Basic_Metods.BasicMethods.askAString("Enter the id of the product:\n")
    pos = Basic_Metods.BasicMethods.searchByID(fileName, id)
    if pos != -1:
        products = Basic_Metods.BasicMethods.readFileToList(fileName)
        print("\n-----------------Enter the new information of the product-----------------\n")
        
        print("Do you want to change the id? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            products[pos].setid()
        
        print("Do you want to change the group? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            products[pos].setgroup()
        
        print("Do you want to change the name? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            products[pos].setname()
        
        print("Do you want to change the description? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            products[pos].setdescription()
        
        print("Do you want to change the price? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            products[pos].setprice()
        
        print("Do you want to change the amount? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            products[pos].setamount()
        
        print("Do you want to change the available? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            products[pos].setavailable()
        
        print("Do you want to change the supplier? (1/0)")
        answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if answer == 1:
            products[pos].setsupplier()
            
        Basic_Metods.BasicMethods.reWriteTheObjects(fileName, products)
    else:
        print("The product does not exist.")

def makeAPurchase(fileName):
    print("\n---------------------------------------------------------------------")
    print("-------------------------- MAKE a PURCHASE ----------------------------")
    print("---------------------------------------------------------------------\n")
    products = []
    purchase = []
    ans = -1
    i = 0
    seeAllTheproducts(fileName)
    while ans != 0:
        print("Do you want to add a product to the purchase? (1/0)")
        ans = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
        if ans == 1:
            print("Which product you want to buy?")
            id = Basic_Metods.BasicMethods.askAString("Enter the id of the product:\n")
            pos = Basic_Metods.BasicMethods.searchByID(fileName, id)
            if pos != -1:
                products = Basic_Metods.BasicMethods.readFileToList(fileName)
                purchase[i] = products[pos]
                
                print("Do you want to change the amount? (1/0)")
                answer = Basic_Metods.BasicMethods.askAnInt("Enter an option: \n")
                if answer == 1:
                    products[pos].setamount()
                
                Basic_Metods.BasicMethods.reWriteTheObjects(fileName, products)
            else:
                print("The product does not exist.")
            
            i = i + 1
        else:
            print("\n---------------------------------------------------------------------")
            print("-------------------------- Your purchase ------------------------------")
            print("---------------------------------------------------------------------\n")
            for st in purchase:
                print(st.toString())
            
            print("Enter the file name to save the purchase:\n")
            Basic_Metods.BasicMethods.save_objectOn_File(purchase, Basic_Metods.BasicMethods.askForFile())
