counter=1
while [ $counter -le 50 ]
do
    echo iteration ---- $counter

    dotnet ../../../SabberStone/core-extensions/SabberStoneCoreConsole/bin/Release/netcoreapp2.0/SabberStoneCoreConsole.dll
    start cmd /k dotnet bin/StrategySearch.dll config/rogue_me_exp.tml
    sleep 3
    start cmd /k dotnet bin/DeckEvaluator.dll 1
    start cmd /k dotnet bin/DeckEvaluator.dll 2
    start cmd /k dotnet bin/DeckEvaluator.dll 3
    start cmd /k dotnet bin/DeckEvaluator.dll 4
    slepp 3
    wait cmd1
    ((counter++))
done