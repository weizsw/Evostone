import os
import subprocess

i = 1
path = "C:/Users/weizsw/iCloudDrive/Documents/Ai for Games/EvoStone/TestBed/StrategySearch/resources/decks/pools/tml"

print("=========== Generating Decks ===========")
p = subprocess.Popen("dotnet ../../../SabberStone/core-extensions/SabberStoneCoreConsole/bin/Release/netcoreapp2.0/SabberStoneCoreConsole.dll")
p.wait()
open('win.txt', 'w').close()
open('winTotal.txt', 'w').close()
for file in os.listdir(path):

    print("=========== Moving file ===========")
    cp = subprocess.Popen("mv " + file + " ../" + "metaDecks.tml", cwd = path)
    cp.wait()

    print("=========== Start evaluation ===========")
    p1 = subprocess.Popen("dotnet bin/StrategySearch.dll config/rogue_me_exp.tml")
    p2 = subprocess.Popen("sleep 5")
    p2.wait()

    print("=========== Nodes started working ===========")
    subprocess.Popen("dotnet bin/DeckEvaluator.dll 1")
    subprocess.Popen("dotnet bin/DeckEvaluator.dll 2")
    subprocess.Popen("dotnet bin/DeckEvaluator.dll 3")
    subprocess.Popen("dotnet bin/DeckEvaluator.dll 4")
    p1.wait()

    with open('win.txt', 'r') as f:
        for line in f:
            with open('winTotal.txt', 'a') as a:
                a.write(line)

