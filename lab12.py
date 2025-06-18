# 가변 인자 , 가변 키워드 인자
def generate_profile(name, age, gender = "미정", *interests, **metadata):
    print("[고객 프로필]")
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"성별: {gender}")
    
    if len(interests) > 0:
        print("관심사: ", end = "")
        last_idx = len(interests) - 1
        for idx, val in enumerate(interests):
            print(f"{val}{"," if idx != last_idx else "\n"}", end = "")
    
    if len(metadata) > 0:
        print("추가 정보: ", end="")
        last_idx = len(metadata) - 1
        for idx, (key, val) in enumerate(metadata.items()):
            print(f"{val}{"," if idx != last_idx else "\n"}", end = "")
            
generate_profile("홍길동", 30)
generate_profile("지민", 26, "여성", *["여행", "사진", "독서"], job = "디자이너", country = "한국")
    

# 출력:
# [ 고객 프로필 ]
# 이름: --
# 나이: --
# tjdquf: --