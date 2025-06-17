def calculate_average(*args):
    hohohun = len(args)
    
    sum = 0
    for i in args :
        sum += i
        
    result = sum/hohohun
    print(f'입력 개수 : {hohohun}, 총합{sum}, 평균:{result}' )

calculate_average(70, 80, 90)
calculate_average(70, 80, 90, 100, 200)