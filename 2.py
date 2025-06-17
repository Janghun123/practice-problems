bar = [val for val in range(1, 11, 2)]
for val in range(2, 11, 2):
    print(val, end="\t")
    
print(bar[2:11:2])
print(bar[0:5:1])
print(bar[0:])
print(bar[2:])
print(bar[2:4])
print(bar[2:3])
print(bar[2:-1])
print(bar)

print("\n", bar[-1:-4:-1])
print(bar[-3:])
print(bar[::-1][:3])