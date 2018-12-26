build:
	docker build -t autocomplete_restapi .

runapp:
	docker-compose up --remove-orphans autocomplete_restapi

runappd:
	docker-compose up -d --remove-orphans autocomplete_restapi

runapplocal:
	python ./src/run.py

runtests:
	docker-compose up --remove-orphans autocomplete_restapi_test

runtestslocal:
	python ./src/test_cases.py

stop:
	docker-compose down

installdependencies:
	pip install -r requirements.txt