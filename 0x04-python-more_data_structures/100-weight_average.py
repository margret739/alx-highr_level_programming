#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    d = 0
    for put in my_list:
        number += put[0] * put[1]
        d += put[1]
    return (number / d)
