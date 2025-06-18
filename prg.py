def input_student(students_list):
    student_number = int(input("학번 입력: "))
    # 이미 등록된 학번인지 검사
    if student_number in students_list:
        print("이미 등록된 학번입니다.")
        return
    
    student_name = input("이름 입력: ")
    korean_score = int(input("국어 성적 입력: "))
    english_score = int(input("영어 성적 입력: "))
    math_score = int(input("수학 성적 입력: "))
    
    total = korean_score + english_score + math_score
    average = round(total / 3, 2)
    # 딕셔너리에 해당 학번의 정보를 저장
    students_list[student_number] = {
        "이름" : student_name,
        "국어" : korean_score,
        "영어" : english_score,
        "수학" : math_score,
        "합계" : total,
        "평균" : average
    }
    print("성적이 저장되었습니다.")
    # 전체 성적 출력
def print_all_students(students_list):
    # 만약에 저장된 학생의 성적이 없다면 '저장된 학생 정보가 없습니다.'
    if not students_list:
        print("저장된 학생 정보가 없습니다.")
        return
    
    print("[ 전체 학생 성적 ]")
    print(f"{'학번':<8}{'이름':<6}{'국어':<5}{'영어':<5}{'수학':<5}{'합계':<6}{'평균':<6}")

    for number, info in students_list.items():
        print(f"{number:<10}{info['이름']:<6}{info['국어']:<7}{info['영어']:<7}{info['수학']:<7}{info['합계']:<8}{info['평균']:<.2f}")

def search_student(students_list):
    track_student_number = int(input("조회할 학번 입력: "))
    if track_student_number not in students_list:
        print("해당 학번의 학생 정보가 없습니다.")
        return
    
    information = students_list[track_student_number]
    print("\n[ 학생 정보 ]")
    print(f"학번: {track_student_number}")
    print(f"이름: {information['이름']}")
    print(f"국어: {information['국어']}")
    print(f"영어: {information['영어']}")
    print(f"수학: {information['수학']}")
    print(f"합계: {information['합계']}")
    print(f"평균: {information['평균']:.2f}")
    
def delete_student(students_list):
    delete_student_number = int(input("삭제할 학번 입력: "))
    if delete_student_number not in students_list:
        print("해당 학번의 학생 정보가 없습니다.")
        return
    del students_list[delete_student_number]
    print("학생 정보가 삭제되었습니다.")
    
students_list = {} 
# 메뉴를 반복적으로 출력
while True:
    print("""\n===== 학생 성적 관리 프로그램 =====
1. 학생 성적 입력
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제
5. 종료          """)
    choice_menu = input("메뉴 선택 (1 ~ 5): ")    
    # 종료
    # 학생 성적 입력 학번 (정수), 이름(문자열), 국어/영어/수학 성적(정수) 입력
    # 합계와 평균 (소수점 2자리) 계산 및 저장
    if choice_menu == "1":
        input_student(students_list)
    # 이미 등록된 학번일 경우 저장하지 않고 오류 메세지 출력
    elif choice_menu == "2":
        print_all_students(students_list)
    elif choice_menu == "3":
        search_student(students_list)
        # 삭제 함수
    elif choice_menu == "4":
        delete_student(students_list)
    elif choice_menu == "5":
        print("프로그램을 종료합니다.")
        break
    # 그 외
    else:
        print("잘못된 입력입니다. 1~5 사이의 숫자를 선택하세요.")