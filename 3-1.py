items = []
while True:
    print(f"[현재 리스트 내용]")
    for index, item in enumerate(items):
        print(f"{index}: {item}")
    print("""작업을 선택하세요:
1: 요소 추가 (Create)
2. 요소 조회 (Read)
3. 요소 수정 (Update)
4. 요소 삭제 (Delete)
5. 종료      
""")
    option = int(input("입력: "))
    if option == 1:
        add = int(input("추가할 값을 입력하세요: "))
        items.append(add)
    
    elif option == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 번호를 입력하세요")