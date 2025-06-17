import random

n = int(input("난수 개수를 입력하세요: "))
a = int(input("시작 범위를 입력하세요: "))
b = int(input("끝 범위를 입력하세요: "))

num_list = [random.randint(a, b) for _ in range(n)]
unique_numbers = []
freq_list = []

for num in num_list:
    if num not in unique_numbers:
        unique_numbers.append(num)

        count = 0
        for j in range(len(num_list)):
            if num_list[j] == num:
                count += 1
        freq_list.append(count)

print(f"고유 숫자 리스트: {unique_numbers}")
print(f"빈도 수 리스트: {freq_list}")
