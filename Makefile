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
