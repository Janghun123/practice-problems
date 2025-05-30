import random
import math

n = int(input("리스트의 개수를 입력하세요. (5~20개): "))

if n < 5 or n > 20:
    print("오류: 리스트 개수는 5 이상 20 이하여야 합니다.")
    
else:
    data = [random.randint(1, 100) for _ in range(n)]
    
    total = 0
    for val in data:
        total += val
    mean = total / n
    
    deviations = []
    for val in data:
        deviations.append(val - mean)
        
    variance = 0
    for d in deviations:
        variance += d**2
    variance /= n
    
    std_dev = math.sqrt(variance)
    
    print("\n생선된 리스트: ", data)
    print("평균: ", round(mean, 2))
    print("편차: ", [round(d, 2) for d in deviations])
    print("분산: ", round(variance, 2))
    print("표준편차: ", round(std_dev, 2))