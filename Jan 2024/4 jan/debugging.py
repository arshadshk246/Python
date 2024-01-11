# from collections import Counter
# import math
# class Solution:
#     def minOperations(self, nums):
#         ele_count = Counter(nums)
#         count = 0
#         for key, value in ele_count.items():
#             if value == 1:
#                 return -1
#             count += math.ceil(value/3)
#         return count

# nums = [2, 3, 3, 2, 2, 4, 2, 3, 4]
# x = Solution()
# x.minOperations(nums)


# def add(x, y):
#     return x + y
# print(add(3,4))

# class Car:
#     wheels = 4 # Attribute

#     def __init__(self, name, company):
#         self.name = name
#         self.company = company

#     def show(self):
#         print(self.name, self.company, self.wheels)

# car1 = Car("m5", "bmw")
# car2 = Car("lancer", "mistubushi")
# car1.show()
# car2.show()


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

# Example usage:
my_range = MyRange(1, 5)
for num in my_range:
    print(num)