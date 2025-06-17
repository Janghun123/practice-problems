# def get_input_num():
#     msg = "정수를 입력하세요: "
#     input_value = int(input(msg))
    
#     if input_value < 0:
#         print("0과 양의 정수만 입력하세요.")
#         return
    
#     return input_value

# value = get_input_num()

# print(value, type(value))

def bar(a,b):
    sum = a+b
    return sum, "합계", 23.23, 23, "지지"

value = bar(2,4)
print(value, type(value))

for i in value:
    if type(i) == int:
        print("정수")
    elif type(i) == str:
        print("문자열")
    else:
        print("실수") 
        
alpha = [i for i in range(ord('a'), ord('z') + 1)]
chr_list = []
for j in alpha:
    chr_list.append(chr(j))
print(chr_list)

def bar(a,b,c,d,e=100):
    print(a,b,c,d,e)
    
bar(1,2,3,4,5)
bar(1,2,3,4)
bar(1,2,3)