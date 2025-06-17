sentence = input("문자와 숫자가 섞인 문자열을 입력하세요: ")

# 숫자만 추출하여 int로 저장
num_list = [int(val) for val in sentence if val.isdigit()]
print(f"숫자 추출: {num_list}")

# 짝수 → 1, 홀수 → -1
turns_list = [1 if val % 2 == 0 else -1 for val in num_list]
print(f"변환된 리스트: {turns_list}")

# 합이 0인 모든 연속 부분 수열 찾기
for index in range(len(turns_list)):
    total = 0
    for j in range(index, len(turns_list)):
        total += turns_list[j]
        if total == 0:
            print(f"부분 수열 [{index}:{j + 1}] → {turns_list[index:j + 1]}")
