print("Welcome to the Python Coffee Shop!")

customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")
 
price_coffee = 3.50
price_latte = 4.00
price_mocha=6.00
 
print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))
print("Latte: $" + str(price_mocha))
 
choice = input("What would you like to order? (coffee/latte): "). lower()
 
if choice == "coffee":
    cost = price_coffee
elif choice == "latte":
    cost = price_latte
elif choice == "mocha":
    cost = price_mocha

else:
    print("Sorry, we do not have that.")
    cost = 0
 
quantity = int(input("How many cups would you like? "))
student_discount = input("Are you a student? (yes/no)").lower()
if student_discount == "yes" :
 cost= cost*0.9
 
total_cost = cost * quantity
 
if quantity > 1:
     print("You get a discount of $1.00!")
     total_cost -= 1.00
 
print("Your total is: $" + str(total_cost))
print("Thank you, " + customer_name + "! Please come again.")
