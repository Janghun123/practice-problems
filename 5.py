# shopping_list = []

# shopping_list = ['milk', 'bread', 'eggs', 'apple']

# print(f"현재 쇼핑 리스트: {shopping_list}")

# shopping_list.insert(0, 'toilet paper')

# shopping_list.insert(1, 'orange juice')

# shopping_list += 'chicken', 'rice'

# print(f"최종 쇼핑 리스트: {shopping_list}")

# import random

# num = int(input("랜덤 지수의 개수(1 ~ 100): "))
# if 100 < num or num < 1:
#     print("에러: N은 1 이상 100 이하의 정수여야 합니다.")
# else: 
#     num_list = []

#     num_list = [random.randint(1, 101) for _ in range(num)]

#     print(f"생성된 리스트: {num_list}")
#     value = list(range(num))
#     index = int(input(f"원하는 원소의 인덱스를 입력하세요(0 ~ {num}): "))
#     if index not in value:
#         print("유효한 인덱스를 입력하세요.")
#     else:
#         print(f"선택한 인덱스의 원소: {num_list[index]}")

# 각 학기별 최고 점수
# import random
# score = []

# score = [random.randint(1,101) for _ in range(10)]
# mid_index = len(score) // 2
# print(score)

# first_score = score[:mid_index]

# second_score = score[mid_index:]

# print(f"1학기 최고 점수: {max(first_score)}")
# print(f"2학기 최고 점수: {max(second_score)}")


bar = [val for val in range(10,51,10)]

print(bar)
idx = 0
for idx in bar:
    print(idx)
    
for idx, val in enumerate(bar):
    print(f"{idx} index: {val}")
    
pos, kin, sol = [2, 3, 4]
print(pos, kin, sol)