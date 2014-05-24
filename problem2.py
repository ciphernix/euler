#!/usr/bin/python

fab_nums = []
def fab(a=1,b=2,max=4000000):
     if b >= max:
         return a
     fab_nums.append(a)
     fab_nums.append(fab(a=b,b=a+b))

fab()
total = 0
for number in fab_nums:
    if isinstance(number,int):
        if number % 2 == 0:
            total += number

print total

