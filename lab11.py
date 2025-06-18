def add_numbers(*args, **kwargs):
    # 옵션을 따로 만듦.
    option = ['abs', 'only_even', 'unique']
    # 정의 되지 않은 옵션 None
    if kwargs not in option:
        return None
# 정수는 args 키워드는 kwargs 생략시 False
print(add_numbers(1, -2, 2, -3))
# abs: True 모든 숫자를 절댓값으로 변환
add_numbers(1, -2, 2, -3, abs = True, only_even = True)
# only_even: True 일 경우 짝수만 합산
add_numbers(1, 2, 2, 3, 3, 4, unique = True)
# unique: True 일 경우 중복 제거 합산
add_numbers(1, 2, 3, round = True)