SHELL := /bin/bash

run:
	sudo docker-compose up

stop:
	sudo docker-compose down

clear:
	rm -rf database
	docker volume rm sinwo-group2_appdb
