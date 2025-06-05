# def square(x: int) -> int:
#     return x ** 2
#
# num = int(input("Enter a number: "))
#
# # print(square(num))
# from numbers import Number
# from typing import Any
#
#
# # def multiply(a, b):
# #     return a * b
# #
# # def multiply(a: str, b: str) -> str:
# #     return a * b
# #
#
# def calc_circle(radius: int  = 1) -> list[float | Any]:
#     area = 3.14 * radius ** 2
#     circum = 2 * 3.14 * radius
#
#     return [area, circum]
#
#
# print(calc_circle(2))
# print(calc_circle(3))

cube = lambda x : x ** 3

print(cube(4))