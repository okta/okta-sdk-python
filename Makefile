install:
	npm install
	pip install tox

test:
	tox

push-and-tag:
	python setup.py push-and-tag