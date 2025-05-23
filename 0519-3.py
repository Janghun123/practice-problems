text = "apple banana orange apple kiwi apple apple"

target = input("검색할 단어를 입력하세요: ")

word = ""
words = []

for i in range(len(text)):
    ch = text[i]
    if ch != " ":
        word += ch
    else:
        words.append(word)
        word = ""
        
if word != "":
    words.append(word)
    
    
count = 0
indexes = []
for i in range(len(words)):
    if words[i] == target:
        count += 1
        indexes.append(i)
        
print(f"'{target}'은(는) {count}번 등장합니다.")
print(f"등장 위치 인덱스: {indexes}")
