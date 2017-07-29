API?=000

default: test

do:
	python main.py $(API)

test:
	rm data-test/*
	python test.py
