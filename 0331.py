# 3개의 정수를 받아 평균 계산
num1 = int(input("정수 1: "))
num2 = int(input("정수 2: "))
num3 = int(input("정수 3: "))

avg = (num1 + num2 + num3) / 3
print(f"평균: {avg}")

# 정수와 실수를 각각 하나씩 입력 받아 두수의 차를 계산 결과값과 그 자료형 출력

num1 = int(input("정수를 입력하세요: "))
num2 = float(input("실수를 입력하세요: "))

minus = num1 - num2

print(f"차: {minus}")
print(f"자료형: {type(minus)}")