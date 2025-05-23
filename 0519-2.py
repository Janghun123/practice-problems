items = []
while True:
    print("""
작업을 선택하세요:
1: 추가 (Create)
2: 조회 (Read)
3: 수정 (Update)
4: 삭제 (Delete)
5: 종료 (Exit)""")
    choice = int(input("입력: "))
    if choice == 1:
        add_num = int(input("추가할 값을 입력하세요: "))
        items.append(add_num)
    elif choice == 2:
        print("[현재 리스트 내용]")
        for index, value in enumerate(items):
            print(f"{index}: {value}")
    elif choice == 3:
        options = int(input("수정할 인덱스를 입력하세요: "))
        new_value = int(input("새로운 값을 입력하세요: "))
        items.pop(options)
        items.insert(options, new_value)
        print("수정 완료.")
    elif choice == 4:
        select = int(input("삭제할 인덱스를 입력하세요: "))
        items.pop(select)
        print("삭제 완료")
    elif choice == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다")