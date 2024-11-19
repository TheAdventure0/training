first = 35
input(35)
second = 46
input(46)
third = 35
input(35)

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
