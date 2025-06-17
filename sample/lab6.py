def warp_in_tag(tag, msg):
    return f"<{tag}>{msg}<{tag}>"

print(warp_in_tag('p', 'hello'))
print(warp_in_tag('b', 'world'))