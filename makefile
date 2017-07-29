API?=000

default: test

do:
	python main.py $(API)

test:
	python test.py
