# ONLINE FOOD ORDERING SYSTEM

# Taking input from the user

customer_name = input("Enter Customer Name: ")
food_item = input("Enter Food Item: ")
quantity = int(input("Enter Quantity: "))
price_per_item = float(input("Enter Price Per Item: "))
delivery_distance = float(input("Enter Delivery Distance: "))

total_food_cost = quantity * price_per_item      #Total Food Cost

delivery_charge = delivery_distance * 6  #Delivery Charge

final_bill = total_food_cost + delivery_charge

#Order Details

print("\n------ ORDER DETAILS ------")

print("Customer Name:", customer_name)
print("Type:", type(customer_name))
print("Memory Address:", id(customer_name))

print("\nFood Item:", food_item)
print("Type:", type(food_item))
print("Memory Address:", id(food_item))

print("\nQuantity:", quantity)
print("Type:", type(quantity))
print("Memory Address:", id(quantity))

print("\nPrice Per Item:", price_per_item)
print("Type:", type(price_per_item))
print("Memory Address:", id(price_per_item))

print("\nDelivery Distance:", delivery_distance)
print("Type:", type(delivery_distance))
print("Memory Address:", id(delivery_distance))

print("\nTotal Food Cost:", total_food_cost)
print("Delivery Charge:", delivery_charge)

print("\nFinal Bill Amount:", final_bill)
print("Type:", type(final_bill))


print("\n------ CHECKING DATA TYPES ------")

print("Quantity is integer:", isinstance(quantity, int))
print("Price is float:", isinstance(price_per_item, float))
print("Final bill is float:", isinstance(final_bill, float))

print("\n------ FINAL BILL ------")
print("Final Bill Amount: ₹",final_bill)
