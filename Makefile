run:
	docker-compose up --build

manage:
	docker-compose run web python manage.py $(CMD)

test:
	docker-compose run web python manage.py test

coverage:
	docker-compose run web python manage.py test --with-coverage

flake:
	docker-compose run web flake8
