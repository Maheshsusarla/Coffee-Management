rent_from_user=int(input("Enter your hostel/room rent= "))

food=int(input("Enter the amount of your food= ")) 

electricity_bill=int(input("Enter your electricity bill= ")) 

charge_per_unit=int(input("Enter your charge per unit= "))

persons=int(input("Enter the no.of persons living in hostel/room= "))

total=electricity_bill* charge_per_unit

output=(food+rent_from_user+total) // persons

print(" Each person will play bill= ",output)