id = "admin" # 아이디 정의
pw = "1234" # 비밀번호 정의

id_chance = 5 # 틀렸을 경우 기회
pw_chance = 0 # 비밀번호 틀릴 경우 횟수 카운트
while id_chance != 0: # 기회가 0이 아니면 반복문 반복
    user_input_id = input("ID를 입력하세요: ")
    user_input_pw = input("비밀번호를 입력하세요: ")
    id_chance -= 1 # 기회 차감
    if id_chance == 0: # 기회 소진 시 
        print("계정이 잠금되었습니다.")
        break # 의미는 없으나 추가
    elif pw_chance == 3: # 암호를 연속으로 3번 틀릴 경우
        print("비밀 번호를 재설정하세요.")
        break # 반복문 종료
    elif user_input_id != id: # 아이디가 틀린 경우
        print(f"등록되지 않은 ID 입니다. (남은 시도 {id_chance}회)")
        pw_chance == 0 # 비밀번호 카운트 리셋
    elif user_input_id == id and user_input_pw != pw: # 아이디가 맞는데 비밀번호가 틀린 경우
        print(f"비밀번호 오류입니다. (남은 시도 {id_chance}회)")
        pw_chance += 1 # 비밀번호 카운트 추가
    else: # 맞출 경우
        print("로그인 성공!")
        break # 반복문 종료

    
