#! /bin/sh
export DISPLAY=:0
cd $(dirname $0)
rm -f images/*
#Runs python3 if that is your command, otherwise tries python
if hash python3>/dev/null; then
	python3 randomImage.py
else
	python randomImage.py
fi
firefox --new-window file:$(dirname $0)/images/$(date +"%m-%d-%Y").png
