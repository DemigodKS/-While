# while + continue
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index_ = my_list.index(-5)
c = len(my_list) - index_

a = 0
while a < c:
    if my_list[a] < 0:
        continue
    elif my_list[a] > 0:
        print(my_list[a])
        a += 1
    elif my_list[a] == 0:
        a += 1