# --------------------------------------------------
print("---------------------------------------------------")
print("SMART SHOPPING CART SYSTEM")
print("---------------------------------------------------")
# --------------------------------------------------


# --------------------------------------------------
# INPUT DETAILS
# --------------------------------------------------

customer_name = input("Enter Customer Name: ")
product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price Per Product: "))
membership = input("Enter Membership Type (Gold/Silver/Regular): ")
wallet = float(input("Enter Available Wallet Balance: "))

# Available products
products = ["Rice", "Sugar", "Oil", "Milk", "Bread"]


# --------------------------------------------------
# ARITHMETIC OPERATORS
# --------------------------------------------------
    
# Total product cost
total_cost = quantity * price

# Discount based on membership
if membership == "Gold":
    discount_rate = 20
elif membership == "Silver":
    discount_rate = 10
else:
    discount_rate = 5

discount_amount = total_cost * discount_rate / 100

# Cost after discount
amount_after_discount = total_cost - discount_amount

# GST calculation
gst_rate = 5
gst_amount = amount_after_discount * gst_rate / 100

# Final bill
final_bill = amount_after_discount + gst_amount

# Modulus operator
remainder = quantity % 2

# --------------------------------------------------
# ASSIGNMENT OPERATORS
# --------------------------------------------------

# Add delivery charge using +=
bill_with_delivery = final_bill
delivery_charge = 50
bill_with_delivery += delivery_charge

# Apply discount using -=
discount_test = total_cost
discount_test -= discount_amount


print("\n" + "=" * 50)
print("             FINAL BILL")
print("=" * 50)

print("Total Cost          : ₹", round(total_cost, 2))
print("Discount Rate       :", discount_rate, "%")
print("Discount Amount     : ₹", round(discount_amount, 2))
print("Amount After Discount: ₹", round(amount_after_discount, 2))
print("GST Amount          : ₹", round(gst_amount, 2))
print("Final Bill          : ₹", round(final_bill, 2))
print("Delivery Charge     : ₹", delivery_charge)
print("Bill With Delivery  : ₹", round(bill_with_delivery, 2))


# --------------------------------------------------
# BITWISE OPERATORS
# --------------------------------------------------

a = 10
b = 6

bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
left_shift = a << 1
right_shift = a >> 1

print("\n" + "=" * 50)
print("             BITWISE OPERATORS")
print("=" * 50)

print("a =", a, "and b =", b)
print("a & b               :", bitwise_and)
print("a | b               :", bitwise_or)
print("a ^ b               :", bitwise_xor)
print("a << 1              :", left_shift)
print("a >> 1              :", right_shift)

# --------------------------------------------------
# IDENTITY OPERATORS
# --------------------------------------------------

x = 100
y = x
z = 100

list1 = ["Rice", "Sugar"]
list2 = ["Rice", "Sugar"]
list3 = list1

same_value_identity = x is z
different_identity = x is not z

same_list_identity = list1 is list3
different_list_identity = list1 is not list2

print("\n" + "=" * 50)
print("            IDENTITY OPERATORS")
print("=" * 50)

print("x is z              :", same_value_identity)
print("x is not z          :", different_identity)
print("list1 is list3      :", same_list_identity)
print("list1 is not list2  :", different_list_identity)