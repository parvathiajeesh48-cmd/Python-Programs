# # # 1. Write a script to perform the following three operations on given list
# # # Access the third element of a list
# # # List Length: Print the total number of items
# # # Check if the list is empty

# # # num_list = [10,20,30,40,50]
# # # print(num_list[2])
# # # print("Total number of items in the list are :",len(num_list))

# # # if num_list:
# # #     print("The list have items")

# # # num_list2 = []
# # # print("Is the second list empty ? :", not num_list2)

# # # 2. Take a given list and modify it through five specific actions:

# # # Change Element: Change the second element of a list to 200 and print the updated list.
# # # Append Element: Add 600 o the end of a list and print the new list.
# # # Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# # # Remove Element (by value): Remove 600 from the list and print the list.
# # # Remove Element (by index): Remove the element at index 0 from the list print the list.

# # num_list = [10,20,30,40,50]
# # num_list[1] = 200
# # print(num_list)

# # num_list.append(600)
# # print(num_list)

# # num_list.insert(2,300)
# # print(num_list)

# # num_list.remove(600)
# # print(num_list)

# # num_list.remove(num_list[0])
# # print(num_list)

# # #OR
# # # num_list.pop(0)
# # # print(num_list)

# #3. Calculate the total sum of all integers in a list and find the arithmetic mean (average).
# # monthly_profit = [10,20,30,45,60,75]
# # total_profit = 0

# # for profit in monthly_profit:
# #     print(profit)
# #     total_profit = total_profit + profit
# # print("The total profit of 6 months is ",total_profit)    

# # average_profit = total_profit/len(monthly_profit)
# # print("The average profit for 6 months is ",average_profit)

# # 4. Find Maximum and Minimum from List
# # Practice Problem: Identify the largest and smallest numerical values within a provided list.

# min_Max_List = [45,12,89,2,67]

# largest = min_Max_List[0]
# smallest = min_Max_List[0]

# for num in min_Max_List:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print("The largest number is ",largest)
# print("The smallest number is ",smallest)

# 5. Multiply every number in a list together to find the total product.

# num_list = [1,2,3,4,5,6,7,8,9,10]
# num_prod = 1

# for num in num_list:
#     num_prod = num_prod * num
# print("The product of the numbers are ",num_prod)

# 6. Given a list of integers, iterate through the items and count how many are even and how many are odd.

# odd_Even_List = [45,12,89,2,67]
# odd_count = 0
# even_count = 0

# for num in odd_Even_List:
#     if num % 2 == 0:
#         even_count+=1
#     else:
#         odd_count+=1
# print("The count of odd numbers in the list is ",odd_count)
# print("The count of even numbers in the list is ",even_count)

# 7.  Take a list and reverse the order of its elements.

# ordered_List = [100,200,300,400,500]
# reversed_List = ordered_List[::-1]

# print("The List is ",ordered_List)
# print("The reversed List is ",reversed_List)

# 8. Sort a list of numbers in ascending order (lowest to highest).

# unordered_List = [23, 4, 57, 13, 43, 90]

# n = len(unordered_List)
# for i in range(n):
#   for j in range(0, n - i - 1):
#     if unordered_List[j] > unordered_List[j + 1]:
#       unordered_List[j], unordered_List[j + 1] = (
#           unordered_List[j + 1],
#           unordered_List[j],
#       )

# print(unordered_List)

# 9. Create a copy of an existing list so that modifying the copy does not change the original.

# fruits = ["Apple","Orange","Mango"]

# copy_Fruits = fruits.copy()

# copy_Fruits[2] = "Cherry"

# print(fruits)
# print(copy_Fruits)

# 10. Merge two separate lists into a single, unified list.

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

l3 = l1+l2
print(l3)


