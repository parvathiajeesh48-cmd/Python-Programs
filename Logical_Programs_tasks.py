#1. Write a program to check whether a number is positive, negative, or zero.
num = int(input("Enter the number:"))

if num == 0:
    print("The number is Zero")
elif num>0:
    print("The number is Positive")
else:
    print("The number is negative")
#-----------------------------------------------------------------------------------------------

#2. Write a program to check whether a number is even or odd.
num = int(input("Enter the number:"))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
#-----------------------------------------------------------------------------------------------

#3.Write a program to check whether a person is eligible to vote based on age.
age = int(input("Enter your age:"))

if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

#-----------------------------------------------------------------------------------------------

#4. Write a program to find the largest of two numbers
num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))

if num_1 == num_2:
    print("Both numbers are equal")
elif num_1>num_2:
    print("First number is greater than second number")
else: 
    print("Second number is greater than first number")

#-----------------------------------------------------------------------------------------------

#5 Write a program to find the smallest of two numbers.
num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))

if num_1 == num_2:
    print("Both numbers are equal")
elif num_1<num_2:
    print("First number is smaller than second number")
else: 
    print("Second number is smaller than first number")

#-----------------------------------------------------------------------------------------------

#6 Write a program to find the largest of three numbers.
num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
num_3 = int(input("Enter the third number:"))


if num_1 > num_2 and num_1 > num_3:
    print("First number is largest")
elif num_2 > num_1 and num_2 > num_3:
    print("second number is largest")
else: 
    print("third number is largest")

#-----------------------------------------------------------------------------------------------

#7 Write a program to find the smallest of three numbers.
num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
num_3 = int(input("Enter the third number:"))


if num_1 < num_2 and num_1 < num_3:
    print("First number is smallest")
elif num_2 < num_1 and num_2 < num_3:
    print("second number is smallest")
else: 
    print("third number is smallest")

#-----------------------------------------------------------------------------------------------


#8 Write a program to check whether a given year is a leap year.
year = int(input("Enter the year:"))

if year % 4 == 0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")

#-----------------------------------------------------------------------------------------------

#9 Write a program to check whether a student has passed or failed based on marks..
marks = int(input("Enter the marks:"))

if marks >=35:
    print("You have passed the exam")
else:
    print("You are failed")


#-----------------------------------------------------------------------------------------------

#10 Write a program to calculate a student's grade based on marks.

marks = int(input("Enter the marks:"))

if marks >=90:
    print("Grade: A+")
elif marks >=85:
    print("Grade: A")
elif marks >=75:
    print("Grade: B+")
elif marks >=70:
    print("Grade: B")
elif marks >=65:
    print("Grade: C+")
elif marks >=60:
    print("Grade: C")
else:
    print("Grade: D (Failed)")

#-----------------------------------------------------------------------------------------------

#11 Write a program to check whether a person is eligible for a driving licence based on age.

age = int(input("Enter the age:"))

if age > 18:
   print("You are eligible for driving licence")
else:
   print("You are ineligible for driving licence")

#-----------------------------------------------------------------------------------------------


#12 Write a program to check whether a number is divisible by both 5 and 10

number = int(input("Enter the number: "))

if number % 10 == 0:
    print("The number is divisible by both 10 and 5")
elif number % 5 == 0:
    print("The number is divisible by 5 but not by 10")
else:
    print("The number is not divisible by 5 or 10")

#-----------------------------------------------------------------------------------------------


#13 Check if a number is divisible by 3 or 7

number = int(input("Enter a number: "))

if number % 3 == 0 or number % 7 == 0:
    print("The number is divisible by 3 or 7")
else:
    print("The number is not divisible by 3 or 7")


#-----------------------------------------------------------------------------------------------

#14 Check if a character is a vowel or consonant

char = input("Enter a character: ")

if char in 'aeiou' or char in 'AEIOU':
        print("It is a vowel")
else:
        print("It is a consonant")

#-----------------------------------------------------------------------------------------------


#15 Write a program to check whether a number is a two-digit number.

number = int(input("Enter a number: "))

if 10 <= number <= 99:
    print("It is a two-digit number")
else:
    print("It is not a two-digit number")


# -----------------------------------------------------------------------------------------------

#16 Write a program to check whether a student is eligible for admission if:
# Marks ≥ 50
# Attendance ≥ 75%

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

if marks >= 50 and attendance >= 75:
    print("Eligible for admission")
else:
    print("Not eligible for admission")

# -----------------------------------------------------------------------------------------------

#17 Write a program to check whether a person is eligible for a loan if:
# Age ≥ 21
# Salary ≥ ₹25,000

age = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))

if age >= 21 and salary >= 25000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# -----------------------------------------------------------------------------------------------

#18 Write a program to check whether a number is positive and even.

number = int(input("Enter a number: "))

if number > 0 and number % 2 == 0:
    print("The number is positive and even")
else:
    print("The number is not positive and even")

# -----------------------------------------------------------------------------------------------

#19 Write a program to check whether a number is positive and divisible by 5.

number = int(input("Enter a number: "))

if number > 0 and number % 5 == 0:
    print("The number is positive and divisible by 5")
else:
    print("The number is not positive and not divisible by 5")


# -----------------------------------------------------------------------------------------------

#20 Write a program to check whether a number lies between 10 and 50.

number = float(input("Enter a number: "))

if number >= 1 and number<=50:
    print("The number lies between 10 and 50")
else:
    print("The number does not lie between 10 and 50")


# -----------------------------------------------------------------------------------------------

#21 Write a program to check whether a number is outside the range 10–50.

number = float(input("Enter a number: "))

if number < 10 or number > 50:
    print("The number is outside the range 10–50")
else:
    print("The number is within the range 10–50")

# -----------------------------------------------------------------------------------------------

#22 Write a program to accept username and password and display "Login successful" only when both are correct.

USER = "admin"
PASS = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == USER and password == PASS:
    print("Login successful")
else:
    print("Invalid username or password")

# -----------------------------------------------------------------------------------------------

#23 Write a program to check whether a person gets a discount if:
# Age is above 60 OR
# Purchase amount is above ₹5000.

age = int(input("Enter age: "))
purchase_amount = int(input("Enter purchase amount: "))

if age > 60 or purchase_amount > 5000:
    print("Eligible for discount")
else:
    print("Not eligible for discount")

# -----------------------------------------------------------------------------------------------

#24 Write a program to check whether a student is eligible for an exam using:
# Attendance ≥ 75 AND
# Fees paid = True.

attendance = int(input("Enter attendance percentage: "))
fees_input = input("Are fees paid? (yes/no): ")

fees_paid = fees_input in ['yes', 'y', 'true']

if attendance >= 75 and fees_paid:
    print("Eligible for exam")
else:
    print("Not eligible for exam")

# -----------------------------------------------------------------------------------------------

#25 Write a program to check whether a number is divisible by both 3 and 5, only 3, only 5, or neither.

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
elif number % 3 == 0:
    print("Divisible by only 3")
elif number % 5 == 0:
    print("Divisible by only 5")
else:
    print("Divisible by neither 3 nor 5")
















