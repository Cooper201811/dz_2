with open('referat.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
    print(len(content))

    words = content.split()
    print(len(words))

with open('referat2.txt', 'w', encoding='UTF-8') as f2:
    content2 = ''
    for i in content:
        if i != '.':
            content2 += i
        else:
            content2 += '!'
    f2.write(content2)