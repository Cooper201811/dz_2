with open('text.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.upper()
        print(line)