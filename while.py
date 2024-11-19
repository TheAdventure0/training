my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
while number < len(my_list):
    num_ = my_list[number]
    number += 1
    if num_ == 0:
        continue
    elif num_ < 0:
        break
    print(num_)
