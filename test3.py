import random

w = [random.randint(1, 100) for val in range(100)]
print(w)
list_dictionally = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "F": []
}

for i in w:
        if i >= 90:
            list_dictionally["A"].append(i)
        elif i >= 80:
            list_dictionally["B"].append(i)
        elif i >= 70:
            list_dictionally["C"].append(i)
        elif i >= 60:
            list_dictionally["D"].append(i)
        else:
            list_dictionally["F"].append(i)
            
for grade, values in list_dictionally.items():
    print(f"등급: {grade}, 점수: {values}")