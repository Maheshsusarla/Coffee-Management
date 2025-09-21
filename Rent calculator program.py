Our_Menu={
    'Cold Coffe' : 120,
    'Green Tea':60,
    'Masala Chai':50,
    'Cold Coffe with Ice Cream':150,
    'Veg Sandwich':100
}


print("---Welcome to Mr.chai---")

print("1.Cold Coffe : 120\nGreen Tea: 60\nMasala Chai: 50\nCold Coffe with Ice Cream: 150\nVeg Sandwich: 100")

Order_total=0

Item1=input("Enter the your first  item = ")

if Item1 in Our_Menu:
    Order_total+=Our_Menu[Item1]
    print(f"Your item{Item1} has been added")
else:
    print(f"Order item {Item1}is not avaialble ")

Another_order_Item=input("Do you want to add another item?(Yes/No)")

if Another_order_Item=="Yes":
    Item2=input("Enter your second item=")
    if Item2 in Our_Menu:
        Order_total+=Our_Menu[Item2]
        print(f"Your item as been added")
    else:
        print(f"Order item{Item2} is not avaliable")
print(f"The total amount is {Order_total}")
