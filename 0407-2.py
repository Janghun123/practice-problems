# 점수를 기반으로 우수합격/ 합격/ 불합격 판정 내리는 프로그램

def calculate_grade_judge(korea, english, math):
    avg = (korea + english + math) / 3
    if avg >= 90 and korea >= 80 and english >= 80 and math >= 80:
        return avg, "우수 합격"
    elif avg >= 70 and korea >= 40 and english >= 40 and math >= 40:
        return avg, "합격"
    else:
        return avg, "불합격"
    

korea = int(input("국어 점수: "))
english = int(input("영어 점수: "))
math = int(input("수학 점수: "))

avg, msg = calculate_grade_judge(korea, english, math)

print(f"평균: {avg}")
print(f"결과: {msg}")
