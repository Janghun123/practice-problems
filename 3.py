numlist = []
for val in range(1, 11):
    num = int(input("정수를 입력하세요: "))
    numlist.append(num)

    
    
print(f"[원본 리스트]\n{numlist}")

print(f"1. 처음 5개 원소: \n{numlist[0:5]}")

print(f"2. 뒤에서 3개 원소: \n{numlist[-1:-4:-1]}")

print(f"3. 짝수 인덱스 원소: \n{numlist[1:10:2]}")

print(f"4. 거꾸로 뒤집은 리스트: \n{numlist[::-1]}")

