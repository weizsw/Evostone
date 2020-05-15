import json
def outTojson():
    f = open("weight.txt", "r")
    dict1 = {}
    dict2 = {}
    i = 1
    for line in f:
        if not line:
            continue
        if 'weight' in line:
            tmp, weight = line.split('=')
            wCost, wAOE, wHQ, wRemove = weight.strip().split(',')
            weightList = [wCost, wAOE, wHQ, wRemove]
            dict2['weight'] = weightList
        elif 'ClassName' in line:
            tmp, className = line.strip().split('=')
            dict2['class'] = className
        elif 'CardList' in line:
            tmp, cardList = line.split('=')
            cardList = cardList.strip().split(',')
            dict2['cards'] = cardList
        elif 'win' in line:
            tmp, win = line.split('=')
            win = win.lstrip().rstrip().split(',')
            win.remove('')
            dict2['win'] = win
        if len(dict2) == 4:
            test = 'test' + str(i)
            i += 1
            dict1[test] = dict2
            dict2 = {}

    # with open('bao.json', 'w') as out:
    #     json_object = json.dump(dict1, out)
    with open('bao.json', 'r') as json_file:
        json_object = json.load(json_file)


