def contains(arg_list, num):
    for i in arg_list:
        if i == num:
            return True
        
    return False
        # 반복문 하고 if를     
print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))