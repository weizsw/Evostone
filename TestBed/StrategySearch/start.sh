#!/bin/bash

echo "Start"

python3 ../../Preprocessing/Read.py
cp ../../Preprocessing/metaDecks.tml resources/decks/pools
dotnet bin/DeckEvaluator.dll 3

