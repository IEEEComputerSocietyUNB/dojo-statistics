API?=000

default: test

do:
	python3 main.py $(API)

test:
	python3 test.py
