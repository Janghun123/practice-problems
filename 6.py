def sum_numbers(a, b):
    return a + b

print(sum_numbers(3, 5))

def greet_user(name):
    print(f"Hello, {name}!")
    
greet_user('alice')

def max_of_three(a, b, c):
    m = []
    m.append(a)
    m.append(b)
    m.append(c)
    return max(m)

print(max_of_three(10, 20, 15))

def is_even(num):
    if num == 0:
        return False
    elif num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(4))
print(is_even(0))
print(is_even(5))

def wrap_in_tag(tag, msg):
    return f"<{tag}>{msg}</{tag}>"
    

print(wrap_in_tag('p', 'hello'))

def contains(list_box, find):
    var = 0
    while var < len(list_box):
        if list_box[var] == find:
            return True
        else:
            var += 1
    return False  
              
print(contains([1, 2, 3, 4], 3))

def calculate_average(*args):
    return sum(args) / len(args)
    
print(calculate_average(1, 2, 3, 4, 5))
print(calculate_average(6, 7, 8))
print(calculate_average(10, 20))