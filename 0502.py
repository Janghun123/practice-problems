# 사용자로부터 table 개수 T, 각 테이블의 행 수 M, 열 수 N을 입력 받아 *로 구성된 
# m * n table T개 출력
table = int(input("테이블 개수 입력: "))
degree = int(input("행 수 입력: "))
row = int(input("열 수 입력: "))

for t in range(table):
    for d in range(degree):
        print('*' * row)
    print()
        