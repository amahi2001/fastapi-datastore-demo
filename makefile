.ONESHELL:
.DEFAULT_GOAL := run

#initiate the virtual environment
init:
	pyenv local 3.11
	virtualenv -p 3.11 env
ifeq ($(findstring MINGW64_NT,$(shell uname -s)),MINGW64_NT)
	source env/Scripts/activate
else
	source env/bin/activate
endif
	python -m pip install -U pip
	pip install -Ur requirements.txt
	pip freeze > requirements.txt

#runs server
run: init
	uvicorn main:app --reload

deploy: requirements.txt
	gcloud app deploy -q --project=<project-ID>