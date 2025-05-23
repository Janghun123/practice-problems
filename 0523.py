import random

# 사용자 입력
num = int(input("난수 개수를 입력하세요: "))
start = int(input("시작 범위를 입력하세요: "))
end = int(input("끝 범위를 입력하세요: "))

# 난수 생성
read_nums = [random.randint(start, end) for _ in range(num)]

# 빈도 계산
freq = {}
for number in read_nums: # number 에 리스트 값을 부여
    if number in freq: # number랑 수가 겹치면
        freq[number] += 1 # 카운트 
    else:
        freq[number] = 1 # 1

# (숫자, 빈도) 쌍 리스트 생성
freq_list = list(freq.items())

# 상위 3개를 저장할 리스트 (삽입 정렬 방식)
top3 = [] 

for item in freq_list:
    inserted = False
    for i in range(len(top3)):
        if item[1] > top3[i][1]:  # 빈도 기준 비교
            top3.insert(i, item)
            inserted = True
            break
    if not inserted:
        top3.append(item)
    if len(top3) > 3:
        top3 = top3[:3]

# 출력
print("\n가장 많이 등장한 숫자 TOP 3:")
for number, count in top3:
    print(f"숫자 {number} = {count}회 등장")
