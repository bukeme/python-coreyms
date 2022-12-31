# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result


def square_numbers(nums):
    for i in nums:
        yield i*i

my_nums = square_numbers([1, 2, 3, 4, 5])
# nums = [i*i for i in [1, 2, 3, 4, 5]] # list comprehension
nums = (i*i for i in [1, 2, 3, 4, 5]) # generators

# print(nums)
# print(list(nums))

# print(my_nums)
# for num in my_nums:
#     print(num)
for num in nums:
    print(num)