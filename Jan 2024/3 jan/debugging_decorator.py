def greet(func):
    def wrapper():
        func()
        print("Hello, Good Morning")

    return wrapper


@greet
def func():
    print("in func")


# Calling the decorated function
func()


# def sub_decorator(func):
#     def wrapper(x, y):
#         result = func(x, y)
#         print(f"Substraction of {x} and {y} is: {result}")
#         return result

#     return wrapper


# @sub_decorator
# def sub(a, b):
#     return abs(a - b)


# sub(5, 3)
