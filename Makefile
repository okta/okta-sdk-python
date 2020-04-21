install:
	npm install

test:
	tox

push-and-tag:
	python setup.py push-and-tag