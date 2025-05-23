#  10개 입력

num_list = []

for i in range(10):
    print("정수를 입력하세요(10개)")
    num = int(input(f"{i + 1}번째 정수: "))
    num_list.append(num)
    
print("[원본 리스트]")
print(f"{num_list}")

print("1. 처음 5개")
print(f"{num_list[0:5]}")
    
print("2. 뒤에서 3개 원소: ")
print(f"{num_list[-3:]}")

print("3. 짝수 인덱스 원소:")
print(f"{num_list[1::2]}")

print("4. 거꾸로 뒤집은 리스트:")
print(f"{num_list[::-1]}")

