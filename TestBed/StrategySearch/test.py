open('weightTotal.txt', 'w').close()
with open('weight.txt', 'r') as f:
    for line in f:
        with open('weightTotal.txt', 'a') as a:
            a.write(line)