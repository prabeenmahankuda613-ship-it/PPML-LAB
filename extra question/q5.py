def find_min(lst, i, current_min):
    if i == len(lst):
        return current_min
    elif lst[i] < current_min:
        return find_min(lst, i + 1, lst[i])
    else:
        return find_min(lst, i + 1, current_min)

l = [3, 2, 5, 1, 7]

print("The minimum number in list:", find_min(l, 0, l[0]))