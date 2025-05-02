print("""
도형을 선택하세요:
1. 원의 면적 계산
2. 삼각형의 면적 계산
3. 사각형의 면적 계산
""")
choice = int(input(""))
if choice == 1:
    radius = int(input("반지름을 입력하세요: "))
    print(f"원의 면적은 {3.14 * (radius ** 2)}입니다.")
elif choice == 2:
    distance = int(input("밑변을 입력하세요: "))
    height = int(input("높이를 입력하세요: "))
    print(f"삼각형의 면적은 {(distance * height) / 2}입니다.")
elif choice == 3:
    width = int(input("가로를 입력하세요: "))
    length = int(input("세로를 입력하세요: "))
    print(f"사각형의 면적은 {width * length}입니다.")
else:
    print("잘못된 입력입니다.")