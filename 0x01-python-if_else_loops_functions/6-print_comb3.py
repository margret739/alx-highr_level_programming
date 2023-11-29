#!/usr/bin/python3
for i in range(9):
    for l in range(i + 1, 10):
        if i * 10 + l < 89:
            print("{:d}{:d}".format(i,l), end=",")
print("{:d}".format(89))
