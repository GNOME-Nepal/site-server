init:
	pip freeze | grep poetry || pip install poetry
	# Activate poetry shell
	poetry install || echo "Poetry environment not found."
	# make reqyured directory
	mkdir staticfiles logs
	touch logs/django_error.log
	# Copy environment files
	cp env.example .env && cp env.example docker.env

create_admin:
	DJANGO_SUPERUSER_USERNAME=$(DJANGO_ADMIN_USERNAME) \
	DJANGO_SUPERUSER_EMAIL=$(DJANGO_ADMIN_EMAIL) \
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_ADMIN_PASSWORD) \
	python manage.py createsuperuser --noinput || echo "Superuser creation failed." && echo "Super user $(DJANGO_ADMIN_USERNAME) created successfully"

build_dev:
	docker buildx build --target development -t gnome_nepal:dev .

build:
	docker buildx build --target production -t gnome_nepal:latest .

freeze:
	rm requirements.txt && pip freeze > requirements.txt

dev:
	python manage.py migrate --noinput
	make create_admin
	python manage.py runserver 0.0.0.0:8000

cleanup:
	## make a cleanup code

prod:
	python manage.py migrate --noinput
	python manage.py collectstatic --no-input
	make create_admin
	python -m gunicorn core.wsgi:application \
		--bind 0.0.0.0:8000 -w 2 --log-level info \
		--access-logfile ./logs/gunicorn.access.log \
		--error-logfile ./logs/gunicorn.error.log
