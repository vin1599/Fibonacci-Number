"""
 fibonacci series is start from 0,1,1,2,3,5,.......
 where 0 is 1st position, 1 is 2nd and so on
 formula for fibonacci series is "F(n) = F(n-1) + F(n-2)"
"""


def fibonacci(number):
    first_num = 0
    second_num = 1
    if number < 0:
        print("incorrect number")
    elif number == 0:
        return first_num
    elif number == 1:
        return second_num
    else:
        for num in range(2, number):
            n_num = first_num + second_num
            first_num = second_num
            second_num = n_num
        return second_num


position = int(input("enter position: "))
print(fibonacci(position))
