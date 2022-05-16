include Makefile.env

all: test

.PHONY: test
test:
	pipenv run python -m unittest discover
