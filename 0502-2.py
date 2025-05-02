# # 사용자로부터 table 개수 T, 각 테이블의 행 수 M, 열 수 N을 입력 받아 *로 구성된 
# # m * n table T개 출력
# import random

# table = int(input("테이블 개수 입력: "))
# degree = int(input("행 수 입력: "))
# row = int(input("열 수 입력: "))

# print("""출력 옵션을 선택하세요:
# 1. 1부터 시작하여 열 방향으로 증가
# 2 1~100 사이 랜덤 값  출력
#       """)
# choice = int(input("옵션 (1 또는 2): "))
# for t in range(table):
#     num = 1
#     print(f"\n테이블 {t + 1}")
#     for d in range(degree):
#         row_num = []
#         for r in range(row):
#             if choice == 1:
#                 row_num.append(str(num))
#                 num += 1
#             elif choice == 2:
#                 row_num.append(str(random.randint(1, 100)))
#         for r in row_num:
#             print(r, end = " ")
#         print()    
table = int(input("테이블 입력: "))
row = int(input("행 입력: "))
col = int(input("열 입력: "))

print("""
1. 테두리만 *
2. 왼쪽 → 오른쪽 대각선 (\\)
3. 오른쪽 → 왼쪽 대각선 (/)
4. 양방향 대각선 (X)
""")
shape = int(input("옵션 선택 (1~4): "))

for t in range(table):
    print(f"\n[테이블 {t + 1}]")
    for r in range(row):
        for c in range(col):
            if shape == 1:  # 테두리만 *
                if r == 0 or r == row - 1 or c == 0 or c == col - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif shape == 2:  # 왼쪽 → 오른쪽 대각선 (\\)
                if r == c:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif shape == 3:  # 오른쪽 → 왼쪽 대각선 (/)
                if c == col - r - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            elif shape == 4:  # 양방향 대각선 (X)
                if r == c or c == col - r - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()
    print()
