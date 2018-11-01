build:
	docker-compose build

up:
	docker-compose up -d

publish:
	docker-compose up -p

up-tail:
	docker-compose up

start:
	docker-compose start

down:
	docker-compose down

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti NGINXDOCKERNAME bash

shell-web:
	docker exec -ti DJANGOXDOCKERNAME bash

shell-db:
	docker exec -ti MSQLDOCKERNAME bash

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs db

collectstatic:
	docker exec DJANGOXDOCKERNAME /bin/sh -c "python manage.py collectstatic --noinput"  