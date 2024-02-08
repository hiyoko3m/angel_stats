.PHONY:\
	makemigrations\
	migrate\
	run\

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

run:
	poetry run python manage.py runserver

format:
	poetry run black .
	poetry run isort .

lint:
	poetry run flake8
