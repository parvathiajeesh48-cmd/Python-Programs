# def greet(name, age):
#     print("Name:", name)
#     print("Age:", age)
# greet("Achu", 25)

# def greet(name, age):
#     print("Name:", name)
#     print("Age:", age)
# greet(age=25, name="Shivaay")

# def greet(name="Guest"):
#     print("Hello", name)
# greet("Rudra")
# greet()

# def total(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     return result

# print(total(10, 20))
# print(total(10, 20, 30))
# print(total(10, 20, 30, 40))

# def student_info(**data):
#     for key, value in data.items():
#         print(key, ":", value)

# student_info(
#     name="Ravi",
#     age=18,
#     marks=85
# )

# def demo(*args, **kwargs):
#     print(args)
#     print(kwargs)
# demo(10, 20, name="Achu", age=25)

# x = 10
# def show():
#     # print(x)
#     x=20
#     print(x)
# show()
# print(x)

# x = 10
# def show():
#    global x
#    x=20
#    print(x)
# show()
# print(x)

# def outer():
#     x = "outer"

#     def inner():
#         # nonlocal x
#         x = "inner"

#     inner()
#     print("x after inner():", x)
# outer()

