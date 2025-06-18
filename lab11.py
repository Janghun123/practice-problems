def add_numbers(*args, **kwargs):
    # 옵션을 따로 만듦.
    option = ['abs', 'only_even', 'unique']
    # 정의 되지 않은 옵션 None
    for key in kwargs:
        if key not in option:
            return None
    # args 가변 인자의 값을 리스트로 저장
    values = list(args)
    
    if "abs" in kwargs and kwargs["abs"] == True:
        for idx, val in enumerate(values):
          if val < 0:
              values[idx] = -val 
              
    if "only_even" in kwargs and kwargs["only_even"] == True:
        values = [v for v in values if v % 2 == 0]
        
    if "unique" in kwargs and kwargs["unique"] == True:
        temp = []
        for val in values:
            if val not in temp:
                temp.append(val)
        values = temp
        
    total = 0
    for val in values:
        total += val
        
    print(f"합계는 {total}입니다")
     
# 정수는 args 키워드는 kwargs 생략시 False
add_numbers(1, -2, 2, -3)
# abs: True 모든 숫자를 절댓값으로 변환
add_numbers(1, -2, 2, -3, abs = True, only_even = True)
# only_even: True 일 경우 짝수만 합산
add_numbers(1, 2, 2, 3, 3, 4, unique = True)
# unique: True 일 경우 중복 제거 합산
add_numbers(1, 2, 3, round = True)