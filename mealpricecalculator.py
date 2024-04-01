answer=""
while  answer!="salir":
    print("       menu")
    name = input("what is your name: ")
    id = input("what's your id number: ")
    print(f"welcome {name} your id number is {id}")
    subtotal=0
    taxrate=16
    nueva=""
    while  nueva !="N":     
    
        compra=input(" what do you wish to purchase:  ")
        precio=float(input("what's the price:  "))
        subtotal+=precio

        nueva=input("anything else: Y/N ").upper()
    print(f"the subtotal is {subtotal}")
    print(f"the tax is {subtotal*taxrate/100}")
    print(f"the total is: {subtotal+subtotal*taxrate/100} ")