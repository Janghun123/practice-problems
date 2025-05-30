import random

scores = [random.randint(1, 101) for _ in range(20)]

grades = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "F": []
    }

def grade_classify(scores):
    for score in scores:
        if score >= 90:
            grades["A"].append(score)
        elif score >= 80:
            grades["B"].append(score)
        elif score >= 70:
            grades["C"].append(score)
        elif score >= 60:
            grades["D"].append(score)
        else:
            grades["F"].append(score) 

grade_classify(scores)

print("등급 분포 및 평균 점수: ")
for grade in ["A", "B", "C", "D", "F"]:
    count = len(grades[grade])
    stars = '*' * count
    if count > 0:
        avg = sum(grades[grade]) / count
        print(f"{grade} 등급: 평균 점수 = {avg:.2f}")
        print(f"{stars} ({count}명)")
    else:
        print(f"{grade} 등급: 없음 (0명)")