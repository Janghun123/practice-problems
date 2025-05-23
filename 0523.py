import random

# 사용자 입력
num = int(input("난수 개수를 입력하세요: "))
start = int(input("시작 범위를 입력하세요: "))
end = int(input("끝 범위를 입력하세요: "))

# 난수 생성
read_nums = [random.randint(start, end) for _ in range(num)]

# 고유 숫자 + 빈도 구하기
count_num_list = []
freq_list = []  # (숫자, 빈도)

for i in range(len(read_nums)):
    n = read_nums[i]
    if n in count_num_list:
        continue

    count = 0
    for j in range(len(read_nums)):
        if read_nums[j] == n:
            count += 1

    freq_list.append((n, count))
    count_num_list.append(n)

# 출력 (디버깅용)
print(f"\n고유 숫자 리스트: {count_num_list}")
print(f"빈도 수 리스트: {freq_list}")

# 상위 3개의 빈도값 찾기
top_freqs = []

for i in range(len(freq_list)):
    freq = freq_list[i][1]  # 두 번째 값만 비교 (정수)
    if freq not in top_freqs:
        if len(top_freqs) < 3: # 상위3개 이내의 값
            top_freqs.append(freq)
        else:
            min_val = top_freqs[0]
            min_idx = 0
            for k in range(1, len(top_freqs)):
                if top_freqs[k] < min_val:
                    min_val = top_freqs[k]
                    min_idx = k
            if freq > min_val:
                top_freqs[min_idx] = freq

# 최종 출력
print(f"\n📊 가장 많이 등장한 숫자 Top 3 (동점 포함):")
for pair in freq_list:
    if pair[1] in top_freqs:
        print(f"숫자 {pair[0]} → {pair[1]}회")
