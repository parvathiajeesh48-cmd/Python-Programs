# 1. Write a program to create a new string made of an input string’s first, middle, and last characters.
# Given Input: str1 = "James"
# Expected Output: Jms
#--------------------------------------------------------------------------------------------------------------------

# user_string=input("Enter a string :")
# user_string_len = len(user_string)
# f= user_string[0]
# l = user_string[-1]
# m= user_string[user_string_len//2]
# print(f,m,l) 

# 2. Write a program to create a new string made of the middle three characters of an input string of odd length.

# Given Input: str1 = "JhonDipPeta"
# Expected Output: Dip

# user_String = input("Enter the input string: ")
# string_length = len(user_String)

# rem = string_length % 2 

# if rem == 0:
#     print("Please enter an odd length string")
# else:
#     mid_str = user_String[(string_length//2)-1] , user_String[string_length//2] ,  user_String[(string_length//2)+1]
#     print(mid_str)

# 3. Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1.
# Given Input: s1 = "Ault" s2 = "Kelly"
# Expected Output: AuKellylt

# s1 = input("Print the first string:")
# s2 = input("Print the second string:")

# s1_mid = len(s1) //2

# s3 = s1[0:s1_mid]+s2+s1[s1_mid:]
# print(s3)


# # 4. Given two strings, s1 and s2, create a new string from the first, middle, and last characters of each input string.
# # Given Input: s1 = "America" s2 = "Japan"
# # Expected Output: AJrpan

# s1 = input("Enter the first string: ")
# s2 = input("Enter the second string:")

# s1_mid = len(s1)//2
# s2_mid = len(s2)//2

# s3 = s1[0]+s2[0]+s1[s1_mid]+s2[s2_mid]+s1[-1]+s2[-1]

# print(s3)

# 5. Write a program to reverse a given string.

# Given Input: str1 = "PYnative"

# Expected Output: evitanYP

normal_string = input("Enter the string: ")

reversed_string = normal_string[::-1]

print(reversed_string)