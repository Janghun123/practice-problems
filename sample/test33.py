def max_of_three(*args):
    large = 0
    for i in args:
        if i > large:  # 순차적으로 불러오고 max에 저장된 값과 비교
            large = i
        else:
            pass
    return large


print(max_of_three(10, 20, 15))