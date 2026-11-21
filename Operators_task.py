# -----------------------SCENARIO 1: Shopping Bill — Addition + -----------------------
print("SCENARIO 1: Shopping Bill — Addition +")
shirt = 800
shoes = 1200
total = shirt + shoes
print("Total bill =", total)

#----------------------- SCENARIO 2: Bank Balance — Subtraction (-) -----------------------
print("SCENARIO 2: Bank Balance — Subtraction (-)")
balance = 10000
withdraw = 2500
remaining = balance - withdraw
print("Remaining balance =", remaining)

#----------------------- SCENARIO 3: Movie Tickets — Multiplication (*)-----------------------
print("SCENARIO 3: Movie Tickets — Multiplication (*)")
ticket_rate = 250
num_of_tickets = 4
total = ticket_rate * num_of_tickets
print("Total amount =", total)

#----------------------- SCENARIO 4: Restaurant Bill — Division (/)-----------------------
print("SCENARIO 4: Restaurant Bill — Division (/)")
bill = 1500
friends = 4
each_person = bill / friends
print("Each person pays =", each_person)

#----------------------- SCENARIO 5: Packing Chocolates — // and -----------------------
print("SCENARIO 5: Packing Chocolates — // and")
chocolates = 53
box_capacity = 10
boxes = chocolates // box_capacity
remaining = chocolates % box_capacity
print("Complete boxes =", boxes)
print("Chocolates left =", remaining)

#----------------------- SCENARIO 6: Convert Minutes into Hours and Minute-----------------------
print("SCENARIO 6: Convert Minutes into Hours and Minute")
minutes = 145
hours = minutes // 60
remaining_minutes = minutes % 60
print("Hours =", hours)
print("Minutes =", remaining_minutes)

# -----------------------SCENARIO 7: Even or Odd — Modulus (%)-----------------------
print("SCENARIO 7: Even or Odd — Modulus (%)")
roll_no = 25

if roll_no % 2 == 0:
    print("Even")
else:
    print("Odd")

#----------------------- SCENARIO 8: Area of a Square — Exponent (**)-----------------------
print("SCENARIO 8: Area of a Square — Exponent (**)")
side = 5
area = side ** 2
print("Area =", area, "square metres")

#----------------------- SCENARIO 9: Adding Money to a Wallet — +-----------------------
print("SCENARIO 9: Adding Money to a Wallet — +")
balance = 500
balance += 200
print("Updated balance =", balance)

#------------------------SCENARIO 10: Game Score — += and ------------------------
print("SCENARIO 10: Game Score — += and")
score = 100
score += 50
score -= 20
print("Final score =", score)

#----------------------- SCENARIO 11: Exam Pass Check — >=-----------------------
print("SCENARIO 11: Exam Pass Check — >=")
mark = 65
passing_mark = 40
print(mark >= passing_mark)

# -----------------------SCENARIO 12: Password Matching — ==-----------------------
print("SCENARIO 12: Password Matching — ==")

stored_password = "python123"
entered_password = "python123"

if entered_password == stored_password:
    print("Password matched")
else:
    print("Incorrect password")

#----------------------- SCENARIO 13: Stock Availability — !=-----------------------
print("SCENARIO 13: Stock Availability — !=")
stock = 10

if stock != 0:
    print("Product is available")
else:
    print("Product is out of stock")

#----------------------- SCENARIO 14: Driving Licence Eligibility — and-----------------------
print(" SCENARIO 14: Driving Licence Eligibility — and")
age = 20
passed_test = True

if age >= 18 and passed_test:
    print("Eligible for driving licence")
else:
    print("Not eligible")

#----------------------- SCENARIO 15: Weekend Check — or-----------------------
print("SCENARIO 15: Weekend Check — or")
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

#----------------------- SCENARIO 16: Online Shopping Free Delivery — or-----------------------
print("SCENARIO 16: Online Shopping Free Delivery — or")
order_amount = 800
premium_member = True

if order_amount >= 1000 or premium_member:
    print("Free delivery")
else:
    print("Delivery charge applies")

#----------------------- SCENARIO 17: Account Access — not-----------------------
print("SCENARIO 17: Account Access — not")
account_blocked = False

if not account_blocked:
    print("Account access allowed")
else:
    print("Account is blocked")

#----------------------- SCENARIO 18: Job Eligibility-----------------------
print(" SCENARIO 18: Job Eligibility")
age = 24
graduated = True
banned = False

if age >= 21 and graduated and not banned:
    print("Eligible for job")
else:
    print("Not eligible")

#----------------------- SCENARIO 19: Check Product Availability — in -----------------------
print("SCENARIO 19: Check Product Availability — in")
products = ["Laptop", "Mobile", "Tablet", "Headphones"]
print("Laptop" in products)

#----------------------- SCENARIO 20: Restricted Username — not in-----------------------
print("SCENARIO 20: Restricted Username — not in")
blocked_names = ["admin", "root", "system"]
username = "student"

if username not in blocked_names:
    print("Username allowed")
else:
    print("Username blocked")

#----------------------- SCENARIO 21: Membership with Strings — in-----------------------
print(" SCENARIO 21: Membership with Strings — in")
email = "student@gmail.com"
print("@" in email)

#----------------------- SCENARIO 22: == vs is-----------------------
print("SCENARIO 22: == vs is")
list1 = [10, 20, 30]
list2 = [10, 20, 30]

print(list1 == list2)
print(list1 is list2)

#----------------------- SCENARIO 23: Same Object Reference — is-----------------------
print(" SCENARIO 23: Same Object Reference — is")
cart1 = ["Laptop", "Mouse"]
cart2 = cart1

print(cart1 == cart2)
print(cart1 is cart2)

#----------------------- SCENARIO 24: User Permissions — Bitwise &-----------------------



#----------------------- SCENARIO 25: Online Shopping Checkout-----------------------
print("SCENARIO 25: Online Shopping Checkout")
price = 1200
quantity = 3
discount = 500

products = ["Laptop", "Mobile", "Tablet", "Headphones"]

total = price * quantity
final_amount = total - discount

print("Total price =", total)
print("Final amount =", final_amount)

if final_amount >= 2000:
    print("Free delivery")
else:
    print("Delivery charge applies")

if "Laptop" in products:
    print("Laptop is available")
else:
    print("Laptop is not available")