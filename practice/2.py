# 메뉴 출력 입력 받기 -> 메뉴 (반복문)
# 입력 외 값은 오류 메시지 continue
# 각 기능에 추가 입력 요구와 에러 처리

while True:
    print("""
--------Menu--------
1. 구구단 출력
2. 랜덤값 삼각형 출력
3. 종료""")
    choice = int(input("메뉴를 선택하시오: "))
    if choice == 1:
        num = input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5): ")
        start_num, end_num = num.split("~")
        start = int(start_num)
        end = int(end_num)
        for i in range(9):
            print(f"{num} * {i + 1} = {num * (i + 1)}")
    elif choice == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")