# def name_of_function():
#     num1 = 10
#     num2 = 30
#     return num1 + num2
# ans = name_of_function()
# print(ans)

# def value_of_function(num1, num2):
#     return num1 + num2
# ans = value_of_function(10, 20)
# print(ans)

# def sum_of_values(num1=10, num2=20): # default arguments
#     print(num1, num2)
#     return num1 + num2

# ans = sum_of_values(100, 200)
# print(ans)

# def sum_of_values(*args, **kwargs):
#     print(args, kwargs) # args=arguments, kwargs=keywordarguments
#     return sum(args), sum(kwargs.values())
# agrs will be stored in a tuple, kwargs will be stored in a dictionary
# If you don't define a return function it will return none

# ans = sum_of_values(10, 20, 30, 40, 50, 60, 70, num1=10, num2=20)
# print(ans)

# ans = sum_of_values(10, 20, 30, 40, num1=10)
# print(ans)

# ans = sum_of_values(10, 20)
# print(ans)

# def square(num):
#     return num ** 2
# ans = square(10)
# print(ans)

# square = lambda num: num ** 2 # lambda is a inline function in python
# ans = square(10)
# print(ans)

# sample_list = range(1, 11) # 1...10
# square = lambda num: num ** 2
# ans = map(square, sample_list)
# print(ans)

# for ele in ans:
#     print (ele)

# sample_list = range(1, 11) # 1...10
# even = lambda x: x % 2 == 0
# ans = filter(even, sample_list)
# ans = list(filter(even, sample_list)) # filter only returns true values and gives actual result
# ans = list(map(even, sample_list)) # map returns true, false values
# print(ans)

# for ele in ans:
#     print(ele)

# List comprehension = single line code
sample_list = range(1, 11) # 1...10
# for ele in sample_list:
#     if ele % 2 == 0:
#         print(ele)
# ans = [ele for ele in sample_list if ele % 2 == 0]
ans = [ele if ele % 2 == 0 else False for ele in sample_list]
print(ans)

