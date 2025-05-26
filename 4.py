# bar = [val for val in range(1, 6)]
# # assignment operator
# sol = 8

# # multiple assignment operator 좌항과 우항의 개수는 동일 해야한다.
# foo , pos, kin = 2, 3, 4
# print(foo, pos, kin)

# # bar = [1, 2, 3, 4, 5] 1 = a , 2 = b ··· (Unpacking)
# a, b, c, d, e = bar
# # * -> collection -> list
# foo = [1, 2, 3]
# pos = [4, 5, 6]

# a, *b, c = bar
# print(a, b, c)
# for x, y in zip(foo, pos):
#     print(f"{x}, {y}")
    
# bar = [1, 2, 3]
# foo = [40, 50, 60]
# pos = [bar, foo]
# # matrix
# print(pos)
# # vactor
# sol = [*bar, *foo]
# print(sol)

# # 함수 정의 def test(a, b, c)

# def test(a, b, c, d, e, f, g):
#     print(a, b, c, d, e, f, g)
    
# arg_1 = [1, 2, 3, 4, 5, 6, 7]    
# arg_2 = [10, 20, 30, 40, 50, 60, 70]    

# # packing and unpacking for a list
# test(*arg_1)
# test(*arg_2)

# def test(*args):
#     for val in args:
#         print(val, end='')
        
        
# bar = [1, 2, 3]
# foo = (4, 5, 6)
# print(bar, type(bar), bar[1])
# print(foo, type(foo), foo[1])
# bar.append(100)

# def due(*args):
#     print(args[0])
#     print(args)

# arg_1 = [val for val in range(2, 11, 2)]
# arg_2 = [val for val in range(1, 11, 2)]

# due(*arg_1)
# due(*arg_2)

# # 변수의 동작 모드

# bar = 2     # set
# print(bar)  # get

bar = [ 5, 6, 7]
foo = bar
sol, *pos = bar

print(foo)

print(sol, pos)