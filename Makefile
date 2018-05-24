init:
	pip install -r requirements.txt

test:
	nosetests

run:
	python thermo

.PHONY: init test run
