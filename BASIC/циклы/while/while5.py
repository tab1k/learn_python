count = 0
found = None

for i in 'hello':
    if i == 'l':
        count += 1
        found = True
    else:
        found = False

print(found, count)



