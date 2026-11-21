# # # word = "Python"
# # # print(word[0])
# # # print(word[-1])

# # # text="abcdefghi"
# # # print(text[:])
# # # print(text[:3])
# # # print(text[::-1])
# # # print(text[::-2])
# # # print(text[3:])

# # # t="Hello"
# # # t[0] = "j"

# # # name="Veena"
# # # age=30
# # # print(f"{name} is {age} years old")

# # # print("{name} is {age} years old")
 
# # age=25
# # # print("Age: "+age)
# # # Output-> TypeError

# # # print("Age: "+str(age))
# # # print(f"Age: {age}")

# # # fruits = ["Apple", "Banana", "Mango"]
# # # fruits[0]
# # # fruits[1]="Orange"
# # # print(fruits)
# # # fruits[2]="Orange"
# # # print(fruits)

# # # mixed=[10,"Python",3.5,True]
# # # print(mixed)

# # # fruits.append(True)
# # # print(fruits)

# # # numbers=[10,20,30,40]
# # # print(numbers[0])
# # # print(numbers[-1])

# # # list[start:stop:step]
# # # numbers=[10,20,30,40]
# # # print(numbers[1:3])
# # # # output -> 20,30
# # # print(numbers[:3])
# # # print(numbers[::-1])

# # nums=[1,2]
# # nums.append(3)
# # # output-> [1,2,3]
# # # nums.append(4,5)//error
# # # append() accepts only one argument

# # nums.append([4,5])
# # print(nums)

# # nums=[1,3]
# # nums.insert(1,2)
# # print(nums)

# # nums=[1,2]
# # nums.extend([3,4,5])
# # print(nums)

# # nums=[1,2,3,2]
# # nums.remove(2)
# # print(nums)

# nums=[1,2,3,2]
# nums.pop(1)
# print(nums)
# # nums.pop() // removes the last element
# print(nums)

# # pop() returns the removed element
# nums=[1,2,3]
# x=nums.pop()
# print(x)

# nums=[1,2,3]
# nums.clear()
# nums=[1,2,3]
# g=nums.index(2)
# print(g)

# nums=[3,1,4,2]
# nums.sort()

# print(nums)
# nums.sort(reverse=True)


# # Difference between sort() and sorted()

# # nums.sort()-> changes the original list

# # sorted(nums) -> returns a new sorted list. Original list remains unchanged

# nums=[3,1,4,2]
# new_list=sorted(nums)
# print(nums)  
# print(new_list)  

# fruits = ["Apple", "Banana", "Mango"]
# # for fruit in fruits:
# #     print(fruit)

# for i in range(len(fruits)):
#    print(fruits[i])

# a=[1,2]
# b=[3,4]
# print(a+b)

# a=[1,2]
# print(a*2)

matrix = [[1, 2], [3, 4]]

for row in matrix:
  print(*row) #-->* operator for unpacking individual items

# Output:
# [1, 2]
# [3, 4]