number_of_items=int(input("Enter the number: "))
total_price=0
while number_of_items<0 :
    print("Invalid number of items.\n Enter number of items: ")
if number_of_items==0 :
    print("No items mentioned.")
else :
    for i in range(1, number_of_items+1):
        price = float(input("Enter price of item: "))
        total_price = total_price + price
discounted_price=total_price-(total_price*0.1)
print("Total Price for "+str(number_of_items)+" items is "+"{:.2f}".format(discounted_price))

