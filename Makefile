install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

build:
	docker build -t myfastapiapp .

run:
	docker run -p 8080:8080 myfastapiapp

deploy: build run

all: install lint test format deploy
